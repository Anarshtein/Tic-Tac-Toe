import pygame
import sys
import time

import tictactoe as ttt

# Initializing the pygame module
pygame.init()
# Setting the window size whcich opens when runner.py is executed
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Creating a window which will contain the game with the previously set sise
screen = pygame.display.set_mode(size)

# Adding fonts
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

# Game variables
user = None # Defining the player X or O
board = ttt.initial_state() # Calling initial_state() function to create the initial board
ai_turn = False # Boolean value which controls AI's turn

# Looping the game for window not be closed after game is over
while True:

    # Checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() # Closing window and exiting game if user chooses to end the game

    screen.fill(black)

    # Let user choose a player if not chosen yet.
    if user is None:

        # Draw title at the top of the window
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Adding button for choosing player X
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        # Adding button for choosing player O
        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as O", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed() # For detecting mouse click
        if click == 1: # If mouse if clicked
            mouse = pygame.mouse.get_pos() # Determining the position of the mouse
            if playXButton.collidepoint(mouse): # Determining if clicked button is for X
                time.sleep(0.2) # Adding sleep time to overcome doubleclick
                user = ttt.X # Assigning user to be X
            elif playOButton.collidepoint(mouse): # Determining if clicked button is for X
                time.sleep(0.2) # Adding sleep time to overcome doubleclick
                user = ttt.O # Assigning user to be O

    else:

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3): # Looping over rows
            row = []
            for j in range(3): # Looping over columns
                # Creating rectangles
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)


                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, white) # Getting X or O
                    moveRect = move.get_rect()
                    moveRect.center = rect.center # Centering the move in the cell 
                    screen.blit(move, moveRect) # Displaying
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board) # Checking if the game ended
        player = ttt.player(board) # Determining which player's turn it is

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board) # Getting the best move for AI by calling minimax() function
                board = ttt.result(board, move) # Add the move to board
                ai_turn = False # Reseting 
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed() 
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    # Checking if the clicked cell is empty
                    if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = ttt.result(board, (i, j)) # Add user's move to corresponding cell of the board

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip()
