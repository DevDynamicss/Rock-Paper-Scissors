import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'rock', 'paper', or 'scissors'. Type 'quit' to end the game.")

    # Initialize scores
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        # Get player choice
        player_choice = input("\nYour choice: ").strip().lower()
        if player_choice == 'quit':
            print("\nGame Over!")
            if rounds == 0:
                print("You didn't play any rounds. See you next time!")
            else:
                print(f"\nFinal Score after {rounds} rounds: You {player_score} - {computer_score} Computer")
                if player_score > computer_score:
                    print("Congratulations! You won the game!")
                elif player_score < computer_score:
                    print("Sorry, the computer won the game!")
                else:
                    print("It's a tie game!")
            break

        # Validate input
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        rounds += 1
        print(f"Score: You {player_score} - {computer_score} Computer")
