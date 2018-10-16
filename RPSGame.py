
# import the random package so that wec an generate random numbers
from random import randint

# choose the rock paper scissors options
# arrays are 0 - based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]

# make teh computer chose a weapon from the random
computer_choice = choices[randint(0,2)]

# print the choise to the terminal window
print("Computer chooses: ", computer_choice)