
# import the random package so that wec an generate random numbers
from random import randint

# choose the rock paper scissors options
# arrays are 0 - based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

# make teh computer chose a weapon from the random
computer_choice = choices[randint(0,2)]

# Player Lives with two variables
compLives = 3
playerLives = 3


# print the choise to the terminal window
print("Computer chooses: ", computer_choice)


# set up our loop 
while compLives > 0 and playerLives > 0:
    #set player to True by making a selection
    print("Choose your weapon!")
    player=input("Rock, Paper or Scissors?\n")

    print(player, "\n")

    if player == computer_choice:
       print("Tie! You live to shoot another day")
    elif player == "Rock":
       	 if computer_choice == "Paper":
       	    print("You Lose! Paper covers Rock")

         else:
       	    print("Yon Win!", player, "smashes", computer_choice,)
            compLives = compLives - 1

    elif player == "Paper":
        if computer_choice == "Scissors":
         print("You Lose!", computer_choice, "cut", player,)
        else:
            print("You Won!", player, "covers", computer_choice,)
            compLives = compLives - 1

    elif player == "Scissors":
         if computer_choice == "Rock":
            print ("You Lose!", computer_choice, "smashes", player,)
         else:
             print("You Win!", player, "cut", computer_choice,)
    elif player ==  "quit":
       exit()
    else:
         print("Check your spelling...that's not a valid choice\n")

    # reset the game loop and start over again.     