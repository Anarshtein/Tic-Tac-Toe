# Tic-Tac-Toe

This is a Python-based implementation of the classic Tic-Tac-Toe game, with a graphical interface using **Pygame** and an AI opponent powered by the **Minimax algorithm**. 

## Features

- **Player vs AI**: Choose to play as either "X" or "O" and let the AI play as the other player.
- **AI opponent**: The AI uses the minimax algorithm to play optimally, ensuring a challenging game for any player.
- **Graphical Interface**: The game uses Pygame to render a visually appealing interface.
- **Reset Option**: After a game ends, you can click "Play Again" to restart a new game.
- **Detects Wins and Draws**: The game accurately detects when a player wins or if the game ends in a draw.

## Table of Contents

- [Installation](#installation)
- [How to Play](#how-to-play)
- [Minimax Algorithm](#minimax-algorithm)
- [Code Structure](#code-structure)
- [Directory Structure](#directory-structure)

## Installation

### Prerequisites
Before you can run this project, you need to have the following installed:
- **Python 3.x**: You can download it [here](https://www.python.org/downloads/).
- **Pygame**: A Python library for game development.

### Installing Dependencies
1. First, clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/Anarshtein/Tic-Tac-Toe.git

2. Move to the directory
   
   ```bash
   cd Tic-Tac-Toe

3. Install the required dependencies: Use pip to install Pygame and other dependencies.
   
   ```bash
   pip3 install -r requirements.txt
   
4. Run the game: Now you can start the game by running the following command:
 
  ```bash
  python3 runner.py
```


## How to Play

1. When you start the game, you will be presented with an option to play as either "X" or "O". Click on the button to choose your side.
2. The game will then begin with an empty 3x3 grid. You will either make the first move (if you choose "X") or the AI will go first (if you choose "O").
3. Click on an empty cell to make your move. The AI will then make its move.
4. The game continues until there is a winner or the game ends in a tie.
5. After the game ends, click "Play Again" to start a new game.


## Minimax Algorithm

The AI opponent is powered by the **Minimax** algorithm, a popular decision rule in game theory and AI. The algorithm evaluates all possible moves, simulating the game until its conclusion, and chooses the optimal move to maximize the chances of winning (or minimize loss) for the AI.

### Key Concepts:

**Maximizing Player (X):** The AI plays as "X" when it wants to maximize the score.

**Minimizing Player (O):** The AI plays as "O" when it wants to minimize the score.

**Recursion:** The algorithm evaluates the board recursively, predicting every possible future move, and assigns scores based on the outcomes.

**Pruning:** The game ends as soon as it detects a winner or a draw, stopping further unnecessary evaluations.


## Code Structure

The code is structured into two main components:

### 1. `tictactoe.py`

This file contains the game logic, including the implementation of the minimax algorithm. Key functions include:

* `initial_state`: Returns the starting 3x3 empty board.
* `player`: Returns whose turn it is (X or O).
* `actions`: Returns all possible moves.
* `result`: Applies a move to the board and returns the updated board.
* `winner`: Checks if there's a winner on the board.
* `terminal`: Checks if the game is over.
* `utility`: Returns the score of the board (1 if X wins, -1 if O wins, 0 for a draw).
* `minimax`: The core AI function that determines the best move for the current player.


### 2. `runner.py`

This file handles the graphical user interface (GUI) using Pygame and manages the game loop:

* It draws the Tic-Tac-Toe grid and renders moves on the board.
* Handles user inputs, such as selecting X or O, making moves, and resetting the game.
* Calls the minimax algorithm to determine the AI's moves.


## Directory Structure
```bash
Tic-Tac-Toe/
├── .gitignore            # Files and directories to ignore in Git
├── OpenSans-Regular.ttf   # Font used in the game
├── README.md             # Readme file
├── requirements.txt      # List of dependencies (Pygame)
├── runner.py             # Main game loop and graphical interface
└── tictactoe.py          # Game logic and AI (Minimax algorithm)

