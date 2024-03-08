from rnastructure_wrapper import RNAstructure
from test import testCase1, testCase2, testCase3, testCase4
import tqdm

rna = RNAstructure()
testcases = [testCase1, testCase2, testCase3, testCase4]
n = 1000
N = 1

if __name__ == "__main__":
    for testcase in testcases:
        for nproc in [1, 2, 4, 8]:
            for _ in tqdm.tqdm(range(N), total=N, desc=f"testcase={testcase}, nproc={nproc}"):
                rna.fold(sequence=[testcase.sequence]*n, dms = [testcase.dms]*n, shape = [testcase.shape]*n, nproc=nproc)