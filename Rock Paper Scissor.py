import time
import os

while True:
    print("Get ready for Rock Paper Scissors")
    time.sleep(1.5)
    os.system('cls')
    choices = ["Rock", "Paper", "Scissor", "rock", "paper","scissor"]
    user_input = input("Enter your choice (Rock Paper Scissor): ")

    if user_input == "Rock":
        print("Computer: Paper")
        print("Computer: You are a noob")
    elif user_input == "Paper":
        print("Computer: Scissor")
        print("Computer: Nice Try, Dumbass")
    elif user_input == "Scissor":
        print("Computer: Rock")
        print("Computer: Still dumb")
    elif user_input == "rock":
        print("Computer: Paper")
        print("You Won")
    elif user_input == "paper":
        print ("Computer:Rock")
        print ("You Won!")
    elif user_input == "scissor":
        print("Computer:paper")
        print ("You Won!")
    else:
        print("invalid")

    play_again = input ("Do you want to play Again? (Y/N): ").strip().lower()
    if play_again != "y":
        break