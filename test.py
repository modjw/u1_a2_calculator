import unittest
from calculator import *

class CalculateTest(unittest.TestCase):
    def test_add(self):
        valueList = [2, 3]
        opList = ["+"]
        calc = Calculator("Test")

        result = calc.calculate(valueList, opList)

        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
