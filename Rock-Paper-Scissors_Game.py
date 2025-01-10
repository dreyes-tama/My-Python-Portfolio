#Diana Reyes Tamayo
#Rock Paper Scissors
#1/6/2025

#Init
import random
losses = 0
wins = 0
ties = 0

#Functions
def game():
    global losses
    global ties
    global wins
    print("Welcome to the Rock-Paper-Scissors game!")
    player = input("Please select rock, paper, or scissors: ")
#Computer's choice
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "rock"
        print("Computer chose rock.")
    elif computer == 2:
        computer = "paper"
        print("Computer chose paper.")
    else:
        computer = "scissors"
        print("Computer chose scissors.")

#Determine the outcome
    if computer == "rock" and player == "rock":
        print("Tie Game!")
        ties = ties + 1

    elif computer == "paper" and player == "rock":
        print ("You lost!")
        losses = losses + 1

    elif computer == "scissors" and player == "rock":
        print ("You won!")
        wins = wins + 1

    elif computer == "rock" and player == "paper":
        print ("You won!")
        wins = wins + 1

    elif computer == "paper" and player == "paper":
        print ("Tie game!")
        ties = ties + 1

    elif computer == "scissors" and player == "paper":
        print("You lost!")
        losses = losses + 1

    elif computer == "rock" and player == "scissors":
        print("You lost!")
        losses = losses + 1

    elif computer == "paper" and player == "scissors":
        print("You won!")
        wins = wins + 1
    else:
        print("Tie Game!")
        ties = ties + 1

    print("Here is your scoreboard: Wins: " + str(wins) + "/ Losses: " + str(losses) + "/ Ties: " + str(ties))

def whole_game():
    game()
    while True:
        playagain = input("Would you like to play another game?")
        if playagain == "yes":
            print("Restarting....")
            game()
        elif playagain == "no":
            print("Thank you for playing the game! Play again soon, bye!")
            break


#Main
whole_game()
