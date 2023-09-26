# Upwords THE GAME
# See rules at https://winning-moves.com/images/UPWORDS_rulesv2.pdf
# By Nate Saunders 14/9/23
# V1.0

from board import Board
from game import Game

def main():
    # New board that is 8x8 (default size)
    board = Board(8)
    game = Game(2, board)

    game.start()

if __name__ == "__main__":
    main()