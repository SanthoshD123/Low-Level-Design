import random

# Define the board with snakes and ladders
board = {
    3: 22,  # Ladder from 3 to 22
    5: 8,   # Ladder from 5 to 8
    11: 26, # Ladder from 11 to 26
    20: 29, # Ladder from 20 to 29
    17: 4,  # Snake from 17 to 4
    19: 7,  # Snake from 19 to 7
    21: 9,  # Snake from 21 to 9
    27: 1   # Snake from 27 to 1
}

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to play a single turn
def play_turn(player_position):
    dice_roll = roll_dice()
    print(f"Rolled a {dice_roll}")
    
    new_position = player_position + dice_roll
    if new_position > 30:  # Restrict max position for a demo board (1-30)
        print("Roll exceeds board limit, stay at current position.")
        return player_position
    
    # Check for snakes or ladders
    if new_position in board:
        print(f"Hit a {'Ladder' if board[new_position] > new_position else 'Snake'}! Moving to {board[new_position]}")
        new_position = board[new_position]
    
    return new_position

# Game function
def snake_and_ladder_game():
    player1 = 0
    player2 = 0
    target = 30  # Win condition

    while True:
        print("\nPlayer 1's turn")
        player1 = play_turn(player1)
        print(f"Player 1 is now on square {player1}")
        if player1 == target:
            print("Player 1 wins!")
            break

        print("\nPlayer 2's turn")
        player2 = play_turn(player2)
        print(f"Player 2 is now on square {player2}")
        if player2 == target:
            print("Player 2 wins!")
            break

# Start the game
snake_and_ladder_game()
