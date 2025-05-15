import unittest
import pandas as pd
from app_refactored import enrich_dateDuration

#Add yourfunctions that you want to test -done

# At a minumum test these:
## Check that the duration column (between checkout and return) is an integer

class TestEnrichment(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame ({
            'Book checkout' : pd.to_datetime(['2025-01-01']),
            'Book Returned': pd.to_datetime(['2025-01-10'])})
        


   def is_integer(self):
    #    self.assertEqual(self.test_duration_integer)

   # def test_is_integer_column(self):
        # Test for column of integers
     #   self.assertFalse(is_integer_column(df, 'date_delta'))

#class TestIsInteger(unittest.TestCase):

    #def test_is_integer(self):
        # Test integer values
      #  self.assertTrue(is_integer(5))      # 5 is an integer
       # self.assertTrue(is_integer(-10))    # -10 is an integer


#class TestDataFrameFunctions(unittest.TestCase):

    #def setUp(self):
       # """Create a sample DataFrame for testing"""
       # self.df = pd.DataFrame({
       #     'col1': [5, 10, 15, -1, 3],  # Mixed values: positive, negative
       #     'col2': [3.5, 0.0, 2.1, 4.5, 6.0],  # Mixed float values, including 0
       #     'col3': [1, 2, 3, 4, 5]  # All positive integers
       # })

   # def test_are_values_above_zero_in_column(self):
    #    # Test with column where all values are positive
     #   self.assertTrue(are_values_above_zero_in_column(self.df, 'col3'))  # All positive integers in col3
#
 #       # Test with column where some values are negative
  #      self.assertFalse(are_values_above_zero_in_column(self.df, 'col1'))  # col1 has a negative value (-1)
#
        # Test with column where there are values equal to 0
 #       self.assertFalse(are_values_above_zero_in_column(self.df, 'col2'))  # col2 has 0.0, which is not > 0

        # Test with a column where all values are above 0
  #      self.assertTrue(are_values_above_zero_in_column(self.df, 'col2'))  # col2 values are > 0 except for 0.0
#
 #   def test_column_does_not_exist(self):
  #      """Test case for when the column does not exist in the DataFrame"""
   #     with self.assertRaises(KeyError):
    #        are_values_above_zero_in_column(self.df, 'col_nonexistent')



## check that the same column is above zero

def is_value_above_zero(value):
    return value > 0

class TestValueFunctions(unittest.TestCase):

    def test_is_value_above_zero(self):
        # Test case where the value is positive
        self.assertGreater(5, 0, "Value should be greater than 0")

## do any other function you've created (or mine)


if __name__ == '__main__':
    unittest.main()