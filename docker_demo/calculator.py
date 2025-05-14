# calculator.py

#def multiply(a, b):
 #   return a * b

#if __name__ == '__main__':
    # Compute the result of 364 * 97
 #   result = multiply(364, 97)
 #   print(f"The result of 364 * 97 is: {result}")



#Build and run a docker image that uses our calculator from earlier to output the answer to 364*97.

class Calculator:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def do_sum(self):
        return self.a + self.b
    
    def do_product(self):
        return self.a * self.b

    def do_subtract(self):
        return self.a - self.b
    
    def do_divide(self):
        return round((self.a / self.b),2)

#myCalc = Calculator(11,6)
#print("the answer is....", myCalc.do_divide())
