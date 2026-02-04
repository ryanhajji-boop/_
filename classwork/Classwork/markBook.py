
def menu():
    while True:
        user_input = input("What would you like to do? \n 1. Add a new score  \n 2. Display all scores \n 3. Exit \n")
        
        try:
            welcome = int(user_input)
            
            if welcome == 1:
                print('new score')
            elif welcome == 2:
                print('display all')
            elif welcome == 3:
                print("Exiting...")
                break
            else:
                print("Please enter a number between 1 and 3.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
menu()