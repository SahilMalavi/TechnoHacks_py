import random

def rock_paper_scissors():
    moves = ["rock", "paper", "scissors"]

    user_move = input("---------------------------------------------\nEnter your move (rock, paper, scissors): ")

    computer_move = random.choice(moves)
    print("The computer's move is:", computer_move)
    print()
    if user_move == computer_move:
        print("•It's a tie!")
    elif user_move == "rock":
        if computer_move == "scissors":
            print("•You win!")
        else:
            print("•You lose!")
    elif user_move == "paper":
        if computer_move == "rock":
            print("•You win!")
        else:
            print("•You lose!")
    elif user_move == "scissors":
        if computer_move == "paper":
            print("•You win!")
        else:
            print("•You lose!")

if __name__ == "__main__":
    while True:
        rock_paper_scissors()
        print()
        answer = input("Would you like to play again? (Y/N): ")
        if answer.lower() == "n":
            break
