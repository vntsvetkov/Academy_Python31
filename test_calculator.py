from calculator import Calculator
import unittest
import time

class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2), 3.5)
        self.assertEqual(self.calc.add(-1, 2), 1)

    def test_div_1(self):
        self.assertEqual(self.calc.div(1, 2), 0.5)
        self.assertEqual(self.calc.div(-5, 5), -1)

    def test_div_2(self):
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)

    def tearDown(self) -> None:
        del self.calc

    # def tearDownClass(cls) -> None:
    #     del cls.calc


if __name__ == "__main__":
    unittest.main()
