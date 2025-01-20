import random

def predict_player_move(player_moves):
    """Predict the player's next move based on previous moves."""
    if not player_moves:
        return random.choice(['rock', 'paper', 'scissors'])
    return random.choice(player_moves)  # Simple prediction based on player's history

def multiplayer_mode():
    """Multiplayer mode allowing two players to take turns."""
    print("Multiplayer Mode: Player 1 vs. Player 2")
    player1_score, player2_score = 0, 0
    rounds = 0

    while True:
        print("\nRound", rounds + 1)
        player1_choice = input("Player 1, enter your choice (rock/paper/scissors or 'quit' to end): ").strip().lower()
        if player1_choice == 'quit':
            break
        
        player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ").strip().lower()

        if player1_choice not in ['rock', 'paper', 'scissors'] or player2_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input! Try again.")
            continue

        print(f"Player 1 chose: {player1_choice}, Player 2 chose: {player2_choice}")

        if player1_choice == player2_choice:
            print("It's a tie!")
        elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
             (player1_choice == 'scissors' and player2_choice == 'paper') or \
             (player1_choice == 'paper' and player2_choice == 'rock'):
            print("Player 1 wins this round!")
            player1_score += 1
        else:
            print("Player 2 wins this round!")
            player2_score += 1

        rounds += 1
        print(f"Score: Player 1 {player1_score} - Player 2 {player2_score}")

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose a mode: 1. Single Player 2. Multiplayer 3. Quit")

    mode = input("Enter mode (1/2/3): ").strip()
    if mode == '3':
        print("Exiting the game. Goodbye!")
        return
    
    if mode == '2':
        multiplayer_mode()
        return

    print("Single Player Mode")
    print("Select difficulty level: 1. Easy 2. Medium 3. Hard")
    difficulty = input("Enter difficulty (1/2/3): ").strip()

    player_score = 0
    computer_score = 0
    rounds = 0
    player_moves = []

    while True:
        player_choice = input("\nYour choice (rock/paper/scissors or 'quit' to end): ").strip().lower()
        if player_choice == 'quit':
            print("\nGame Over!")
            print(f"Final Score: You {player_score} - {computer_score} Computer")
            return

        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        player_moves.append(player_choice)

        if difficulty == '1':
            computer_choice = random.choice(['rock', 'paper', 'scissors'])
        elif difficulty == '2':
            computer_choice = predict_player_move(player_moves)
        elif difficulty == '3':
            # Hard: Counter player's move
            if player_choice == 'rock':
                computer_choice = 'paper'
            elif player_choice == 'paper':
                computer_choice = 'scissors'
            else:
                computer_choice = 'rock'

        print(f"Computer chose: {computer_choice}")

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

# Run the game
rock_paper_scissors()
