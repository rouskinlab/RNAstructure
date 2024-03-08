import pytest

class TestCase:
    def __init__(self, name, sequence, energy, dotbracket, shape=None, dms=None, basepairs=None, matrix=None):
        self.name = name  
        self.sequence = sequence  
        self.energy = energy  
        self.dotbracket = dotbracket  
        self.shape = shape  
        self.dms = dms  
        self.basepairs = basepairs
        self.matrix = matrix
        
    def __repr__(self):  
        return f"TestCase(name={self.name})"
    
    
# created using the RNAstructure server    
testCase1 = TestCase(
    name="test1",
    sequence="ATCCCGTGAAGGCTCATGAAAGAATGGACTTAGGTTGGTAAGTCGGCACCAAGCTCGTGTACCGGGGAATCACACGTTGTTGCTGTGTGCTGTGTGCAATGCTGGCTTCCACAACATATTTCTCGTATCAGCTTGGCTTGGTGGACGATGTTAGATGCAACCCTTCGGTCCGACGAAGCG",
    energy=-52.9,
    dotbracket = ".((.(((((....)))))...)).((((((.((((((....((((.(((((((((.((((((.(((((((.....(((((.(((((((((.....)).)))).)))....)))))..)))))))))))..))..)))))))))..))))........))).)))..))))))........"
)

# created using the RNAstructure server    
testCase2 = TestCase(
    name="test2",
    sequence="TAGGTTATTCATGACCAGGTCTGATCCTAACTGATCCCTGCACCTGAGACAATTGTCAGTAAAATTCCCCCGCCGGACGGTGAAATCTTAGACACTGATGCGCACTTGCCTTCATCCACCGCAGATCGGCCGCACTAGGTACCGGATTCAAATTGCAATATAATGTGGATCGAGTTGCTC",
    energy=-38.0,
    dotbracket="..(((((....))))).((......))((((((((((.((((.((((........))))...........((((....)))).(((((...((.(((.(((((..((((...........))))....).)))).)))))...))))).....)))).........))))).)))))...",
)

# created using the RNAstructure server    
testCase3 = TestCase(
    name="test3",
    sequence="ACATTATACTCCTATGAAGTAAGACACCTAACCATTTCCGGGCCTGGATGATCACCGCGTGCAAAGTTAGAGGTAAGGCCTCACGAAGTGGGGTGATTCGAACGGATGCAGTCGCAGCATTCCGGTTGCCGGTGTCGTATAATTACTAAGATGAGAAGCACGATCCAGTGAATGATCTCA",
    energy=-44.9,
    dotbracket = "......((((.......)))).((((((...(((((((.((((((...(((((((...)))....))))......))))))...)))))))(((((((.(((....(((....)))...))).)))))))))))))...............(((((..(((......))).....)))))",
    shape = [0.08790393, 0.59169479, 0.78596169, 0.25924044, 0.99868452,0.29877943, 0.20166952, 0.21634581, 0.27314175, 0.48068955,0.51707264, 0.62907244, 0.60135849, 0.48611358, 0.41001222,0.12584532, 0.73765472, 0.81217906, 0.20030639, 0.71022525,0.18506476, 0.03744511, 0.39579902, 0.61726879, 0.51534006,0.01105952, 0.05732633, 0.34179386, 0.04104552, 0.8727425 ,0.53805143, 0.45525382, 0.47232103, 0.24588502, 0.09297534,0.79142496, 0.32578463, 0.66378218, 0.77174714, 0.35199207,0.22782617, 0.34847102, 0.72857544, 0.64124326, 0.17927047,0.9178987 , 0.46994386, 0.25858784, 0.71286342, 0.53560414,0.75806769, 0.73066562, 0.50963022, 0.53520109, 0.36915339,0.10430766, 0.86544251, 0.62756061, 0.51223588, 0.04355492,0.27549522, 0.63979693, 0.30769356, 0.07163917, 0.09316816,0.87264071, 0.15733805, 0.27718375, 0.28661951, 0.16209325,0.53928329, 0.88508914, 0.86695723, 0.1812102 , 0.60884479,0.03009661, 0.85129558, 0.34045229, 0.0914664 , 0.26166524,0.22375086, 0.94915735, 0.56146187, 0.36091465, 0.41886521,0.24829202, 0.0450906 , 0.40043535, 0.67516626, 0.67443255,0.37709923, 0.46761512, 0.08007055, 0.58376378, 0.94742094,0.30827327, 0.03387245, 0.27880587, 0.28588335, 0.01035131,0.24891456, 0.35556865, 0.24800608, 0.91411834, 0.99446641,0.25058339, 0.20452149, 0.34458689, 0.90620602, 0.27421895,0.00858696, 0.49241278, 0.22448847, 0.92498285, 0.06061497,0.84126495, 0.82558944, 0.58099745, 0.86148785, 0.64778445,0.34690563, 0.23167383, 0.90761071, 0.04411843, 0.42662202,0.46104583, 0.7041058 , 0.7747546 , 0.70086098, 0.70373165,0.14498417, 0.27290397, 0.9721281 , 0.22465228, 0.62269321,0.57559218, 0.4632312 , 0.30621746, 0.37489712, 0.05449654,0.74787768, 0.25271558, 0.54872713, 0.98930614, 0.84135919,0.60684939, 0.62543596, 0.10723675, 0.78579402, 0.95438189,0.44884302, 0.23381187, 0.52957587, 0.13828921, 0.96351886,0.84062831, 0.76896063, 0.78374443, 0.30345874, 0.14335399,0.83421968, 0.68717312, 0.10808132, 0.07570458, 0.05529121,0.79186381, 0.61362558, 0.15987663, 0.58155248, 0.30422373,0.21757841, 0.83615568, 0.26044954, 0.43653622, 0.3405041 ,0.21923875, 0.05596624, 0.43018119, 0.1945814 , 0.17625313],
)

# created using local Fold command
testCase4 = TestCase(
    name="test4",
    sequence="GAGACAATAGTGGTAGTATACTCTGGTGGCGTTATGTCTGAGCAGTAATAGGACCCGCGCGAGGACTTCTCGTATTTGGTCAGAGACCTCGCGAGCGCTTCATTTATACTGGTGGTGTAGTGCACACGTGCGAGCCGATGTGCGGGTTTAGATAAGAGCTTGTAACCCCTTTGAAAGATC",
    energy=-4.8,
    dotbracket = "..................................................((.(.(......)).)).(((...........))).................................................((........))..................................",
    dms = [0.6105299 , 0.89888459, 0.17117937, 0.84086908, 0.55656341,0.99646008, 0.8024766 , 0.61818125, 0.53768608, 0.33272965,0.99457169, 0.16555241, 0.14948307, 0.29023935, 0.49552044,0.26554421, 0.23141357, 0.74709504, 0.29078709, 0.12262972,0.14062573, 0.97152923, 0.19528534, 0.92289679, 0.5274221 ,0.34185385, 0.76808432, 0.72181056, 0.44191722, 0.22594273,0.45964555, 0.08820266, 0.12865591, 0.52748561, 0.90200248,0.72543137, 0.19618161, 0.09135574, 0.88527834, 0.99726941,0.60524428, 0.75935159, 0.78514916, 0.41813968, 0.43188096,0.70984241, 0.83368117, 0.83030491, 0.10316471, 0.85580948,0.43369179, 0.14003059, 0.36933068, 0.67124175, 0.10051351,0.29559898, 0.92928365, 0.22141157, 0.27827048, 0.94964506,0.27603176, 0.53802936, 0.79921231, 0.7116258 , 0.53916852,0.10214217, 0.05349944, 0.18496622, 0.02155608, 0.1050996 ,0.01707484, 0.93371821, 0.88125981, 0.23777578, 0.65142976,0.46150881, 0.61224824, 0.41025738, 0.9010259 , 0.36735353,0.93368493, 0.4180233 , 0.76964619, 0.29962814, 0.08806589,0.6976643 , 0.62940908, 0.71507263, 0.85837339, 0.95940113,0.29449704, 0.86353489, 0.56412381, 0.84017233, 0.78468956,0.61945113, 0.60469911, 0.49148347, 0.21827709, 0.99692485,0.51132062, 0.03196343, 0.52461159, 0.69154268, 0.26303068,0.03616547, 0.55126056, 0.37911513, 0.61305617, 0.3074702 ,0.23939092, 0.34045863, 0.66292226, 0.48334319, 0.02038468,0.68361913, 0.26827366, 0.76152468, 0.10471912, 0.1582595 ,0.3906462 , 0.83962354, 0.10506492, 0.58541917, 0.7586444 ,0.65648897, 0.40566096, 0.70254802, 0.88510657, 0.88764678,0.83991889, 0.14514486, 0.29481539, 0.87709102, 0.62643219,0.01563399, 0.12652087, 0.55699738, 0.49852767, 0.98761321,0.01823552, 0.92872348, 0.20206057, 0.96432774, 0.43615311,0.10613862, 0.08077244, 0.16353101, 0.21472412, 0.85324849,0.62709381, 0.27077598, 0.68850448, 0.10312839, 0.0366705 ,0.75827955, 0.52969778, 0.97803062, 0.00492726, 0.22194221,0.92776029, 0.88877908, 0.60158447, 0.12223381, 0.26455867,0.93476354, 0.93577426, 0.39721119, 0.72421233, 0.29922743,0.9831314 , 0.4006679 , 0.8891919 , 0.75703811, 0.48280271,0.04341307, 0.89035317, 0.54183438, 0.77434678, 0.16471551]
)

# created using local Fold command
testCase5 = TestCase(
    name="test5",
    sequence='GGGAAAUCC',
    energy=-1.1,
    dotbracket='(((...)))',
    basepairs= [(1, 9), (2, 8), (3, 7)],
    matrix = [[0., 0., 0., 0., 0., 0., 0., 0., 1.], [0., 0., 0., 0., 0., 0., 0., 1., 0.], [0., 0., 0., 0., 0., 0., 1., 0., 0.], [0., 0., 0., 0., 0., 0., 0., 0., 0.], [0., 0., 0., 0., 0., 0., 0., 0., 0.], [0., 0., 0., 0., 0., 0., 0., 0., 0.], [0., 0., 1., 0., 0., 0., 0., 0., 0.], [0., 1., 0., 0., 0., 0., 0., 0., 0.], [1., 0., 0., 0., 0., 0., 0., 0., 0.]])

from rnastructure_wrapper import RNAstructure

@pytest.mark.parametrize("testCase", [testCase1, testCase2])
def test_single_sequence(testCase):
    rna = RNAstructure()
    prediction = rna.fold(testCase.sequence)
    dotbracket, energy = prediction['dotbracket'], prediction['energy']
    assert dotbracket == testCase.dotbracket
    assert energy == testCase.energy
    
# test single sequence with dms and shape
@pytest.mark.parametrize("testCase", [testCase3, testCase4])
def test_single_sequence_with_dms_shape(testCase):
    rna = RNAstructure()
    prediction = rna.fold(testCase.sequence, dms=testCase.dms, shape=testCase.shape)
    dotbracket, energy = prediction['dotbracket'], prediction['energy']
    assert dotbracket == testCase.dotbracket
    assert energy == testCase.energy

# test multiple sequences
@pytest.mark.parametrize("listTestCases", [(testCase1, testCase2)])
def test_multiple_sequences(listTestCases):
    rna = RNAstructure()
    sequences = [testCase.sequence for testCase in listTestCases]
    predictions = rna.fold(sequences)
    for i, testCase in enumerate(listTestCases):  
        assert predictions[i]['dotbracket'] == testCase.dotbracket, f"Expected {testCase.dotbracket} but got {predictions[i]['dotbracket']} for case {testCase.name}"  
        assert predictions[i]['energy'] == testCase.energy, f"Expected {testCase.energy} but got {predictions[i]['energy']} for case {testCase.name}"  

# test mutliple sequences with dms and shape
@pytest.mark.parametrize("listTestCases", [(testCase1, testCase2, testCase3, testCase4)])
def test_multiple_sequences_with_dms_and_shape(listTestCases):
    rna = RNAstructure()
    sequences = [testCase.sequence for testCase in listTestCases]
    dms = [testCase.dms for testCase in listTestCases]
    shape = [testCase.shape for testCase in listTestCases]
    predictions = rna.fold(sequences, dms=dms, shape=shape)
    for i, testCase in enumerate(listTestCases):  
        assert predictions[i]['dotbracket'] == testCase.dotbracket, f"Expected {testCase.dotbracket} but got {predictions[i]['dotbracket']} for case {testCase.name}"  
        assert predictions[i]['energy'] == testCase.energy, f"Expected {testCase.energy} but got {predictions[i]['energy']} for case {testCase.name}"

# test multiple sequences with multiprocessing
@pytest.mark.parametrize("listTestCases", [(testCase1, testCase2)])
def test_multiple_sequences_with_multiprocessing(listTestCases):
    rna = RNAstructure()
    sequences = [testCase.sequence for testCase in listTestCases]
    predictions = rna.fold(sequences, nproc=4)
    for i, testCase in enumerate(listTestCases):  
        assert predictions[i]['dotbracket'] == testCase.dotbracket, f"Expected {testCase.dotbracket} but got {predictions[i]['dotbracket']} for case {testCase.name}"  
        assert predictions[i]['energy'] == testCase.energy, f"Expected {testCase.energy} but got {predictions[i]['energy']} for case {testCase.name}"  

# test mutliple sequences with multiprocessing and dms and shape
@pytest.mark.parametrize("listTestCases", [(testCase1, testCase2, testCase3, testCase4)])
def test_multiple_sequences_with_dms_and_shape_and_multiprocessing(listTestCases):
    rna = RNAstructure()
    sequences = [testCase.sequence for testCase in listTestCases]
    dms = [testCase.dms for testCase in listTestCases]
    shape = [testCase.shape for testCase in listTestCases]
    predictions = rna.fold(sequences, dms=dms, shape=shape, nproc=2)
    for i, testCase in enumerate(listTestCases):  assert predictions[i]['dotbracket'] == testCase.dotbracket, f"Expected {testCase.dotbracket} but got {predictions[i]['dotbracket']} for case {testCase.name}"  
    assert predictions[i]['energy'] == testCase.energy, f"Expected {testCase.energy} but got {predictions[i]['energy']} for case {testCase.name}"  

# test with alternative structures
@pytest.mark.parametrize("listTestCases", [(testCase1, testCase2)])
def test_alternative_structures(listTestCases):
    rna = RNAstructure()
    sequences = [testCase.sequence for testCase in listTestCases]
    predictions = rna.fold(sequences, mfe_only=False)
    for i, testCase in enumerate(listTestCases):  assert predictions[i][0]['dotbracket'] == testCase.dotbracket, f"Expected {testCase.dotbracket} but got {predictions[i][0]['dotbracket']} for case {testCase.name}"  
    assert len(predictions[i]) > 1, f"Expected more than 1 structure but got {len(predictions[i])} for case {testCase.name}"  

# test other output formats
@pytest.mark.parametrize("output_format", ["basepairs", "matrix"])
def test_other_output_formats(output_format):
    rna = RNAstructure()
    prediction = rna.fold(testCase5.sequence, output_format=output_format)
    assert output_format in prediction, f"Expected {output_format} in prediction but got {prediction}"
    if output_format == "basepairs":  
        assert prediction[output_format] == testCase5.basepairs, f"Expected {output_format} but got {prediction[output_format]}"
    elif output_format == "matrix":
        assert (prediction[output_format] == testCase5.matrix).all(), f"Expected {output_format} but got {prediction[output_format]}"
        
        
# test performances
@pytest.mark.parametrize("listTestCases", [(testCase1, testCase2, testCase3, testCase4)])
def test_speed(listTestCases):
    import time
    rna = RNAstructure()
    sequences = [testCase.sequence for testCase in listTestCases]
    dms = [testCase.dms for testCase in listTestCases]
    shape = [testCase.shape for testCase in listTestCases]
    start = time.time()
    for i in range(10):  rna.fold(sequences, dms=dms, shape=shape, nproc=2)
    end = time.time()
    assert end - start < 10, f"Expected less than 10 seconds but got {end - start} seconds"
    print(f"Time taken for 40 runs: {end - start} seconds")
    
    