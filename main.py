# import Python files for menu options
import hypotenuse
import derivative
import distance


# color codes used to change font color (this code segment was developed using an online resource)
class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


# menu options as a list [prompts, action]
# procedure references will be executed directly file.procedure()
main_menu = [
    [bcolors.OKBLUE + "Hypotenuse" + bcolors.ENDC, hypotenuse.driver],
    [bcolors.OKGREEN + "Derivative" + bcolors.ENDC, derivative.driver],
    [bcolors.OKCYAN + "Distance" + bcolors.ENDC, distance.driver],
]

# menu banner (this code segment was developed using an online resources)
border = "=" * 25
banner = f"\n{border}\nWelcome to the Easy Calculator! Please select an option\n{border}"


# creates main menu
def menu():
    title = "Calculator Home" + banner
    # copy() returns a shallow copy of the list
    menu_list = main_menu.copy()
    buildMenu(title, menu_list)


def buildMenu(title, menu_list):
    # menu banner
    print(title)
    # builds a dictionary from menu_list
    prompts = {0: ["Exit", None]}
    for row in menu_list:
        index = len(prompts)
        prompts[index] = row

    # print menu (dictionary)
    # items() returns a view object that contains key-value pairs
    for key, value in prompts.items():
        print(key, '->', value[0])

    while True:
        # get user choice
        choice = input("Type your choice: ")
        try:
            # convert choice to number
            choice = int(choice)
            break
        except ValueError:
            # reprompt user if input is not an integer
            print('Invalid input. Please enter an integer input.')
            # recursion, start menu over again
            buildMenu(title, menu_list)

    if choice == 0:
        # stop
        return
    elif (choice < 0 or choice > 3):
        # reprompt user if input is not an integer between 1 and 4
        print('Invalid option. Please enter a number between 0 and 3.')
    else:
        # get() returns the value of the item with the specified key
        action = prompts.get(choice)[1]
        action()
        # recursion, start menu over again
        buildMenu(title, menu_list)


if __name__ == "__main__":
    menu()
