import uuid
import numpy as np
from os.path import join
import os
import subprocess
import multiprocessing
from typing import List

def run_command(command):
    """
    Run a command in the shell
    """
    subprocess.call(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def dotbracket2basepairs(dotbracket):
    """
    Converts a dotbracket string to a list of basepairs. The output is 1-indexed.
    """
    stack = []
    basepairs = []
    for i, char in enumerate(dotbracket):
        if char == "(":
            stack.append(i+1)
        elif char == ")":
            basepairs.append((stack.pop(), i+1))
    return sorted(basepairs, key=lambda x: x[0])

def dotbracket2matrix(dotbracket):
    """
    Converts a dotbracket string to a matrix
    """
    matrix = np.zeros((len(dotbracket), len(dotbracket)))
    stack = []
    for i, char in enumerate(dotbracket):
        if char == "(":
            stack.append(i)
        elif char == ")":
            j = stack.pop()
            matrix[i, j] = 1
            matrix[j, i] = 1
    return matrix

dotbracket2_factory = {
    "basepairs": dotbracket2basepairs,
    "matrix": dotbracket2matrix,
    'dotbracket': lambda x: x,
}


class Files:
    def __init__(self, id_, temp_folder):
        self.fasta = join(temp_folder, f"{id_}.fasta")
        self.ct = join(temp_folder, f"{id_}.ct")
        self.dms = join(temp_folder, f"{id_}.dms")
        self.shape = join(temp_folder, f"{id_}.shape")
        self.dotbracket = join(temp_folder, f"{id_}.dotbracket")
        
    def _remove_file(self, file):
        if os.path.exists(file):
            os.remove(file)
        
    def __del__(self):
        for f in [self.fasta, self.dms, self.shape, self.dotbracket, self.ct]:
            self._remove_file(f)


class RNAstructure:
    def __init__(self, temp_folder='temp', path='') -> None:
        """Wrapper for the RNAstructure executable
        
        Args:
            temp_folder (str, optional): The folder to store temporary files. Defaults to 'temp'.
            path (str, optional): The path to the RNAstructure executable. Defaults to ''. If empty, it assumes the executable is in the PATH.
        """
        self.temp = temp_folder
        self.path = path

    def fold(self, sequence, dms=None, shape=None, output_format="dotbracket", mfe_only=True, nproc=1):
        """
        Predict the structure for a sequence or a list of sequences
        
        Args:
            sequence: Nucleotide sequence(s) to predict the structure of. A string or a list of strings.
            dms: input for the --DMS flag in Fold. Should be a list of floats with the same length as the sequence, or a list of list of floats.
            shape: input for the --shape flag in Fold. Should be a list of floats with the same length as the sequence, or a list of list of floats.
            output_format: the format of the output. One of "dotbracket", "basepairs", "matrix". Basepairs are 1-indexed.
            mfe_only: sets the -mfe flag in Fold. Returns only the MFE structure. Default is True.
            nproc: number of processes to use for parallelization. Default is 1 (no parallelization).
        """
        assert output_format in ["dotbracket", "basepairs", "matrix"]
        
        # if multiple sequences are provided
        if isinstance(sequence, list) or isinstance(sequence, np.ndarray):
            if dms is None: dms = [None] * len(sequence)
            if shape is None: shape = [None] * len(sequence)
            
            if nproc > 1: # parallelize
                chunks = [(sequence[start:end], dms[start:end], shape[start:end]) for start, end in zip(np.linspace(0, len(sequence), nproc+1, dtype=int)[:-1], np.linspace(0, len(sequence), nproc+1, dtype=int)[1:])]
                with multiprocessing.Pool(nproc) as p:
                    return [pred for process in p.starmap(self.fold, [(seq, dm, sh, output_format, mfe_only) for seq, dm, sh in chunks])\
                            for pred in process]
            else:
                return [self._fold(seq, dm, sh, output_format, mfe_only) for seq, dm, sh in zip(sequence, dms, shape)]
        
        return self._fold(sequence, dms, shape, output_format, mfe_only)

    def _fold(self, sequence, dms, shape, output_format, mfe_only):
        """
        Compute the structure for a single sequence.
        """
        # sanity checks
        if dms is not None:
            assert len(dms) == len(sequence), "The DMS signal should have the same length as the sequence."
        if shape is not None:
            assert len(shape) == len(sequence), "The SHAPE signal should have the same length as the sequence."
        if (dms is not None and np.max(dms) <0.2) or (shape is not None and np.max(shape) < 0.2):
            print("The DMS or SHAPE signal seems to be very low (max < 0.2). Are you sure they are normalized?")
        assert type(sequence) in [str, np.str_], "The sequence should be a string. It is {}, {}, {}".format(type(sequence), len(sequence), sequence)

        id_ = str(uuid.uuid4())
        files = Files(id_, self.temp)        
        fold_path = join(self.path, "Fold")
        cmd = ' '.join([fold_path, files.fasta, files.dotbracket])
        
        # make a temp folder if it doesn't exist
        os.makedirs(self.temp, exist_ok=True)

        # export the sequence to a fasta file
        with open(files.fasta, 'w') as f:
            f.write(f">reference\n{sequence}\n")

        # if shape / dms is provided, export the shape to a file
        for signal, signal_type in zip([dms, shape], ['dms', 'shape']):
            if signal is not None:
                with open(getattr(files, signal_type), 'w') as f:
                    for idx, s in enumerate(signal):
                        f.write(f"{idx+1}\t{s}\n")
                cmd += f" --{signal_type} {getattr(files, signal_type)}"

        # if mfe_only is set, add the flag. Then run
        if mfe_only:
            cmd += " -mfe"
        cmd += " --bracket"
        run_command(cmd)
        
        # read the dotbracket file
        stack = DotBracketReader(files.dotbracket, output_format).read()
        return stack[0] if mfe_only else stack


class DotBracketReader:
    def __init__(self, path, output_format):
        self.path = path
        self.output_format = output_format

    def read(self):
        with open(self.path, 'r') as f:
            lines = f.readlines()
            stack = []
            for line in lines:
                if line[0] == '>':
                    energy = float(line.split(' ')[2]) if '>ENERGY' in line else None
                    stack.append({'energy': energy})
                else:
                    if not '.' in line and not '(' in line and not ')' in line:
                        continue
                    dotbracket = line.strip()
                    stack[-1][self.output_format] = dotbracket2_factory[self.output_format](dotbracket)
        return stack