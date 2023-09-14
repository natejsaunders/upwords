# Upwords THE GAME
# See rules at https://winning-moves.com/images/UPWORDS_rulesv2.pdf
# By Nate Saunders 14/9/23
# V1.0

from board import upwords_board

# New board that is 8x8 (default size)
board = upwords_board(8)

print(board.place('frrfrij', 0, 0, 'v'))
print(board.place('boot', 0, 0, 'h', True))
print(board.place('fight', 0, 0, 'v'))

print(board)