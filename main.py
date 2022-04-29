# import Python files for menu options
import hypotenuse
import derivative
import distance

# menu options as a dictionary
menu_options = {
    1: 'Find Hypotenuse Length',
    2: 'Find the Derivative',
    3: 'Find the Distance',
    4: 'exit',
}

# print menu options from dictionary key/value pair
def print_menu() -> object:
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

    
# menu option 1
def option1():
    print('You chose \' 1 -  Hypotenuse\'')
    hypotenuse.driver()

# menu option 2
def option2():
    print('You chose \' 2 - Derivative\'')
    derivative.driver()

# menu option 3
def option3():
    print('You chose \'3 - Distance\'')
    distance.driver()

# call procedures based on user input
def runOptions():
  # setting while loop condition to be true
  n = 0
  # while loop to accept/process user menu choice
  while (n == 0):
    try:
      option = int(input('Enter your choice 1-4: '))
      if option == 1:
        option1()
      elif option == 2:
        option2()
      elif option == 3:
        option3()
      elif option == 4:
        # setting while loop condition to be false
        n = 1
      else:
        # reprompt user if input is not an integer between 1 and 4
        print('Invalid option. Please enter a number between 1 and 4.')
    except ValueError:
      # reprompt user if input is not an integer
      print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    print_menu()