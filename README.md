# ConnectFour
A connect four game in python with pygame

- main.py - setup main window and initialize Game class
- game.py - main Game class - holds all game logic and has references to all objects
- board.py - Board class - handels drawing the board and pieces and adding pieces to the game board and has a reference to all the pieces
- piece.py - Piece class - holds Piece.draw method which draws the pieces and a referece to the piece's color
- player.py - Player class - mainly handels the coloring of the different pieces. simply a way to keep the alternating colors logical
- button.py - Button class - a clickable button, used in the menu after either player has won to ask whether to play again or quit
- constants.py - holds game hyperparameters such as window width & height, number of rows & columns, etc.
