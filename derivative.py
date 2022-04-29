# import SymPy library to perform symbolic differentiation
import sympy as sp               

def driver():
  # get user input for expression to differentiate
  var = input("Enter expression to differentiate: ")
  
  class Derivative:
    def __init__(self):
      pass
        
  # finds derivative using symbolic differentiation
    def __call__(self, var):
      v_prime = sp.diff(var)
      return v_prime
    
  def run():
    # object instantiation and run __init__ method
      derivative_of = Derivative() 
    # object running __call__ method
      print(derivative_of(var)) 
    
  run()