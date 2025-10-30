"""
This class is responsible for storing all the information about current state of the chess game.
It will also be responsible for determining the valid moves in the current states.
It will also keep a move log.
"""

class GameState():
    def __init__(self):
        #board is 8*8 2d list and each element of the list has 2 characters.
        # The first letter represents the color of the pieces 'b' for black, 'w' for white.
        # The second character represents the piece notation 'K' for king 'q' for queen 'B' for bishop
        # and 'R' for rook and 'N' for Knight.
        # "--" represents an empty space in the board
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moves = []
