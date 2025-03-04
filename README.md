# Snake and Ladder Game 🐍🎲

## Overview
This is a simple implementation of the classic Snake and Ladder board game in Python. The game allows two players to take turns rolling a dice, moving across the board, and encountering snakes and ladders that can help or hinder their progress.

## Features
- Two-player turn-based gameplay
- Random dice rolling
- Predefined board with snakes and ladders
- Win condition at square 30

## How to Play
1. Each player starts at square 0
2. Players take turns rolling a dice
3. Move forward the number of squares shown on the dice
4. If you land on a ladder, move up to the higher square
5. If you land on a snake, slide down to the lower square
6. First player to reach square 30 wins!

## Game Rules
- Dice rolls range from 1-6
- If a roll would take you beyond square 30, you stay at your current position
- Snakes and ladders automatically move you to their corresponding squares

## Requirements
- Python 3.x
- Random module (included in standard library)

## Running the Game
Simply run the script:
```python
python snake_and_ladder.py
