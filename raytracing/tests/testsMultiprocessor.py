import unittest
import env # modifies path
from raytracing import *

inf = float("+inf")

def multiplyBy2(value) -> float:
    return 2*value

class TestMultiProcessorSupport(unittest.TestCase):
    def testMultiPool(self):
        processes = 8
        inputValues = [1,2,3,4]
        with multiprocessing.Pool(processes=processes) as pool:
            outputValues = pool.map(multiplyBy2, inputValues)
        self.assertEqual(outputValues, list(map(multiplyBy2, inputValues)))


if __name__ == '__main__':
    unittest.main()