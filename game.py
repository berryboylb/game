from random import choice
while True:
    # take input from the user
    user_choice = input("Choose a Letter  'R', 'P' or 'S': ")

    #get user_choice from computer
    choices = ['R', 'S', 'P',]
    comp_choice = str(choice(choices))

    # check if user_choice is one of the four options
    if user_choice in ('R', 'P', 'S'):
        if (user_choice == 'R' and comp_choice == 'S') or (user_choice == 'S' and comp_choice == 'P') or (user_choice == 'P' and comp_choice == 'R'):
            print("You Win !!! " + " Player " + user_choice +
                  " and CPU " + comp_choice)
            break
        elif user_choice == comp_choice:
            print("It's a Draw !!! " + " Player " + user_choice +
                  " and  CPU " + comp_choice)
        else:
            print("You Lose !!! " + " Player " + user_choice +
                  " and  CPU " + comp_choice)
    else:
        print("Invalid Input")
