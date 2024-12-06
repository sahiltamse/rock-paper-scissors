import random

def play_game():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid input. Please try again.")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
