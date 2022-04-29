# import math module to perform square root  
import math             

def driver():
  # get user input for Cartesian coordinates
  x1 = int(input("Enter first x-coordinate: "))
  y1 = int(input("Enter first y-coordinate: "))
  x2 = int(input("Enter second x-coordinate: "))
  y2 = int(input("Enter second y-coordinate: "))
  
  class Distance:
    def __init__(self):
      pass
        
  # finds distance using distance formula
    def __call__(self, x1, y1, x2, y2):
      answer = math.sqrt((x2-x1)**2 + (y2-y1)**2)
      return answer
    
  def run():
    # object instantiation and run __init__ method
      distance_of = Distance() 
    # object running __call__ method
      print(distance_of(x1, y1, x2, y2)) 
    
  run()
