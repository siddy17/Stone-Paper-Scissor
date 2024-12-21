import random

def rock_paper_scissors():
    print("Welcome to rock paper scissors")
    print("The rules are simple")
    print("rock beats scissors, scissors beat paper, paper beats rock")
    
    choices = ["rock" , "paper" , "scissors"] #List of valid Choices
    computer_choice = random.choice(choices)
    
    while True:
        player_choice = input("Enter your choice(rock , paper , scissors)").lower()
        if player_choice in choices:
           break
        print("Invalid Choice! Please choose rockc, paper or scissor") 
    
    
    print(f"\nYou chose:{player_choice}")
    print(f"The computer chose:{computer_choice}")
    
    if player_choice == computer_choice:
        print("Its a tie")
    elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice== "paper") or
            (player_choice == "scissors" and computer_choice == "rock")
        ):
            print("You win")
            
    else:
        print("You lose")
        
rock_paper_scissors()