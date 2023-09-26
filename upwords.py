# Upwords THE GAME
# See rules at https://winning-moves.com/images/UPWORDS_rulesv2.pdf
# By Nate Saunders 14/9/23
# V1.0

from board import upwords_board
from game import upwords_game

def main():
    # New board that is 8x8 (default size)
    board = upwords_board(8)
    game = upwords_game(2, board)

    game.start()

if __name__ == "__main__":
    main()