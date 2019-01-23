""" 
This is a Game of Rock,Paper,Scissors
Developer: Srayan
"""

from random import randint
from time import sleep

options = ["ROCK","PAPER","SCISSOR"]
message = {
  "tie": "its a tie",
  "won": "You Win",
  "lost": "You lose"
}

def decide_winner(user_choice,computer_choice):
  sleep(1)
  print("You have chosen : {}".format(user_choice))
  sleep(2)
  print("Computer chose: {}".format(computer_choice))
  if user_choice == computer_choice:
    sleep(1)
    print(message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    sleep(1)
    print(message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    sleep(1)
    print (message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    sleep(1)
    print(message["won"])
  else:
    sleep(1)
    print(message["lost"])

def play_RPS():
  print("Let's Play Rock-Paper-Scissors!! Enter your Choice: ")
  user_choice = input()
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice,computer_choice)

play_RPS()
