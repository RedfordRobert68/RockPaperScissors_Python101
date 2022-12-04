import random

while True:
    rps_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(rps_choices)

    user_choice = input("Do you choose Rock, Paper, or Scissors? ")

    if user_choice == computer_choice:
        outcome = "tie"
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
            outcome = "win"
            print("Rock smashes Scissors. You Win!")
        elif computer_choice == "paper":
            outcome = "lose"
            print("Ooh! Too bad so sad. Paper covers rock. You're a loser!")
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            outcome = "win"
            print("Paper covers Rock. You win!")
        elif computer_choice == "scissors":
            outcome = "lose"
            print("Scissors cut Paper. The computer has turned you into a bunch of smaller pieces of yourself. You lose!")
    elif user_choice.lower() == "scissors":
        if computer_choice == "paper":
            outcome = "win"
            print("Congratulations. You cut up the computer competition because Scissors cuts Paper. You win!")
        elif computer_choice == "rock":
            outcome = "lose"
            print("The computer just smashed your Scissors to pieces with its Rock. You lose!")
    elif user_choice.lower() != "rock" or user_choice.lower() != "paper" or user_choice.lower() !="scissors":
        outcome = ""
        print("Your input is not valid. You must enter Rock, Paper, or Scissors!")

    if outcome == "win":
        replay = input("Would you like to play again? (y/n)")
        if replay.lower() != "y":
            break