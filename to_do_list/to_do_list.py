"""
This program allows the user to create and manage a to-do list in the terminal.
"""

HELP = f"1. Add a task\n2. Remove a task\n3. View list\n4. Quit"
to_do_items = []

def user_input():
    print("\n" + HELP)
    print("Enter the number of the command you'd like to use.")
    user_enter = input("> ")
    print()
    return user_enter

"""
Action functions - based on user input
"""
def add_task(): # Add a task to the to-do list. Only adds one task
    task = input("Enter a task you'd like to add: ")
    to_do_items.append(task)
    print("Task has been added to list!")

def remove_task(): # Removes one task from the to-do list
    if len(to_do_items) == 0:
        print("No items to view. Add a task to get started!")
    else:
        print(to_do_items)

        try:
            index = int(input("Enter the number of task you'd like to remove: ")) - 1
            if 0 <= index < len(to_do_items):
                removed = to_do_items.pop(index)
                print(f"Task '{removed}' has been removed.")
            else:
                print("Invalid task number. Try again.")
        except ValueError:
            print("Invalid task number. Enter a valid task number.")

def quit_program(): # Exit the program
    print("Have a nice day!")
    print("Exited the program.")
    return False

"""
Safeguards - checks if input is valid
"""
def check_num(request): # Checks if input is an integer 1-4 inclusive
    if request.isdigit():
        command = int(request)
        if 0 < command < 5:
            return command
        else:
            return "Invalid input. Input should be a number 1-4"
    else:
        return "Invalid input. Input should be a number 1-4"

def verify_input(): # uses the check_num function to check if input is valid, and asks and checks until it is
    request = user_input()
    attempts = 10
    num = 1
    num_check = check_num(request)
    if type(num_check) == int:
        num = num_check
    return num

"""
Main program
"""
def main():
    # Intro to the program; shows initial task list (if any)
    print("Hello! Here is your to-do list:")
    if to_do_items:
        print(to_do_items)
    else:
        print("No items to view. Everything done!")

    running = True
    while running:
        # Get and verify input
        command = verify_input()

        # Go to corresponding action function
        match command:
            case 1:
                add_task()
            case 2:
                remove_task()
            case 3:
                print(to_do_items)
            case 4:
                quit_program()
                running = False

if __name__ == "__main__":
    main()