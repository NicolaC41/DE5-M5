import unittest 
from calculator_app import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calculation=Calculator(8,2)
    
    def test_sum(self):
        self.assertEqual(self.calculation.do_sum(),10, 'The sum is wrong!')

    # Test the diff, product, division
    def test_diff(self):
        self.assertEqual(self.calculation.do_subtract(),6, 'The sum is wrong!')

    def test_product(self):
        self.assertEqual(self.calculation.do_product(),16, 'The sum is wrong!')

    def test_division(self):
        self.assertEqual(self.calculation.do_divide(),4, 'The sum is wrong!')
    

if __name__ == '__main__':
    unittest.main()