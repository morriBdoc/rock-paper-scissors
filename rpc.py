import random
import os
import platform

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        print('We do not recognise your system. Only Windows and Linux are supported. Exiting...')
        quit

options = ["rock", "paper", "scissors"]
human_score = 0
computer_score = 0

while True:
    human_choice = input("Rock, Paper or Scissors [R][P][S]\n-> ").lower()
    while (human_choice != "r") and (human_choice != "p") and (human_choice != "s"):
        print("Please choose a valid option [R][P][S]")
        human_choice = input("Rock, Paper or Scissors [R][P][S]\n-> ").lower()

    match human_choice:
        case "r":
            human_choice = 'rock'
        case "p":
            human_choice = 'paper'
        case "s":
            human_choice = 'scissors'

    computer_choice = random.choice(options)

    print("Your choice was: " + human_choice)
    print("Computer's choice was: " + computer_choice + '\n')

    if ((human_choice == 'rock') and (computer_choice == 'rock')) or ((human_choice == 'paper') and (human_choice == 'paper')) or ((human_choice == 'scissors') and human_choice == 'scissors'):
        print('It is a tie')
        human_score += 1
        computer_score += 1
    elif ((human_choice == 'rock') and (computer_choice == 'paper')) or ((human_choice == 'paper') and (computer_choice == 'scissors')) or ((human_choice == 'scissors') and (computer_choice == 'rock')):
        print('You lose')
        human_score -= 5
        computer_score += 5
    elif ((human_choice == 'rock') and (computer_choice == 'scissors')) or ((human_choice == 'paper') and (computer_choice == 'rock')) or ((human_choice == 'scissors') and (computer_choice == 'paper')):
        print('You win')
        human_score += 5
        computer_score -= 5

    print('\nYour score is: ' + str(human_score))
    print('Computer\'s score is: ' + str(computer_score))
    
    input('[Enter to play again] [CTRL + C to quit]')
    clear()