import copy
from tile import Tile

# TODO Make scoring happen for all words and columns that have been played on, also check only these words on columns for changes

# Class to store board data in, and also ensure goes are legal
class Board:

    def __init__(self, size):
        self.empty_tile = '_'

        self.size = size

        # Generating tiles - stored as a 3d array, the inner inner arrays store an array of tiles that have been placed
        self.tiles = []             #[[['_', 0]] * size] * size  <- better way of generating list but python doesn't like it :(
        for y in range(size):
            row = []
            for x in range(size):
                row.append([])

            self.tiles.append(row)

        # Initialise possible words
        with open('wordlist.txt', 'r') as wl: self.wordlist = [line[:-1] for line in wl.readlines()]

        # Used to determine whether it is the first go on this board
        self.first_go = True


    # Used to check if a given string is allowed (we also allow Qu because we need to)
    def is_allowed_word(self, word):
        return word.lower() in self.wordlist
    
    # Used to add letters to the board, updating it and checking the go is legal
    def place(self, placement_data):
        word =      placement_data['word']
        y =         placement_data['y']
        x =         placement_data['x']
        dir_in =    placement_data['direction']

        word = word.upper()
        # Directions (vertical or horizontal)
        directions = {
            'v' : [1, 0],
            'h' : [0, 1]
        }
        direction = directions[dir_in]
        opp_dir = direction.reverse()

        # Place the word - then check all words on the board are valid
        new_tiles = copy.deepcopy(self.tiles)

        score = 0

        # Place the tiles
        tiles_empty = True # Used to ensure that the word is being placed on top of another
        for i, tile in enumerate(word):
            this_x = x + direction[0] * i
            this_y = y + direction[1] * i
            # I know this is lazy deal with it
            try:
                grid_square = new_tiles[this_x][this_y]
            except IndexError:
                return 0
            
            if tiles_empty and len(grid_square) >= 1:
                tiles_empty = False

            check_line = [tile]
            for multiplier in (-1, 1):
                check_square = []
                while len(check_square) > 0:
                    check_square = new_tiles[this_x + opp_dir[0] * multiplier][this_y + opp_dir[1] * multiplier]
                if multiplier is -1:

                else:
            
        # If there is no word being played on and it isn't the first go: fail
        if tiles_empty and not self.first_go: return 0
        
        # Update tiles to the changed tiles as the go is valid
        self.tiles = new_tiles

        self.first_go = False
        return score
            
    # Return a nice way of presenting the board (i know the code isnt nice)
    def __str__(self):

        board_return = ''

        board_return += '───' * self.size + '────\n'
        board_return += '|' + '   ' * self.size + '  |'
        
        for row in self.tiles:
            board_return += '\n|  '
            for tile in row:
                board_return += tile[-1] + ' '
            board_return += '|\n'
            board_return += '|' + '   ' * self.size + '  |'

        board_return += '\n' + '───' * self.size + '────\n'

        return board_return