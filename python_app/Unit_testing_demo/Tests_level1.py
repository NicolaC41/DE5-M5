import unittest 
from calculator_app import Calculator

class TestOperations(unittest.TestCase):

    #test logic - for you to come up with!
    ## the functions must be named test_<something>
    def test_sum(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_sum(),10, 'The sum is wrong!')

    # Test the diff, product, division
    def test_diff(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_subtract(),6, 'The sum is wrong!')

    def test_product(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_product(),16, 'The sum is wrong!')

    def test_division(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.do_divide(),4, 'The sum is wrong!')
    

if __name__ == '__main__':
    unittest.main()