"""
This is a Number-Guessing game 
The Player will guess a number. The computer will roll a pair of dice. If the guess is correct the player wins!!
Dev : Srayan
"""

from random import randint
from time import sleep


def get_user_guess():
  guess = int(input("Enter your guess: "))
  return guess


def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll =  randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print ("The maximum possible number is : %d"%(max_val))
  guess=get_user_guess()
  if guess > max_val:
    print("Error !! Entered value is larger than maximum possible value!!")
  else:
    print("Rolling....")
    sleep(2)
    print("First roll: %d"%(first_roll))
    sleep(1)
    print("Second roll: %d"%(second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print("Total value: %d"%(total_roll))
    print("Result...")
    sleep(2)
    if total_roll == guess:
      print("You have WON!!! :D ")
    else:
      print("You LOSE!! :(````` ")
    
    
roll_dice(6)
