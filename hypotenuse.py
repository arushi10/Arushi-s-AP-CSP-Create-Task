def driver():
  # get user input for side lengths
  sidea = int(input("Length of side a: "))
  sideb = int(input("Length of side b: ")) 
  
  class Hypotenuse:
    def __init__(self):
      pass
        
  # finds hypotenuse using pythagorean theorem
    def __call__(self, sidea, sideb):
       hype = ((sidea**2) + (sideb**2))**0.5
       return hype
    
  def run():
    # object instantiation and run __init__ method
      hypotenuse_of = Hypotenuse() 
    # object running __call__ method
      print(hypotenuse_of(sidea, sideb)) 
    
  run()