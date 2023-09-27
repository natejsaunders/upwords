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


    # Used to check if a given string is allowed (word is a 2d array of tiles we need to check for the last one)
    def is_allowed_word(self, word):

        check_word = ''.join(map(str, word))

        return check_word.lower() in self.wordlist 
    
    # Used to check that a word in a given direction is allowed
    def check_line(self, tiles, tile_x, tile_y, direction):
        score = 0
        print(tiles)
        print(tile_y, tile_x, direction)
        check_line = [tiles[tile_x][tile_y][-1]]
        print(check_line)

        # We want to check in both + and - directions
        for multiplier in (-1, 1):
            check_square = []
            multiplier_index = multiplier
            while True:
                try:
                    check_square = tiles[tile_x + direction[0] * multiplier_index][tile_y + direction[1] * multiplier_index]
                except IndexError:
                    break

                if len(check_square) == 0:  
                    break
                
                if multiplier == -1:
                    check_line.insert(0, check_square[-1])
                else:
                    check_line.append(check_square[-1])

                score += len(check_square)
                multiplier_index += multiplier

        if len(check_line) <= 1: return -1
        elif self.is_allowed_word(check_line): return score
        else: return 0
    
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
        opp_dir = direction.copy()
        opp_dir.reverse()

        # Place the word - then check all words on the board are valid
        new_tiles = copy.deepcopy(self.tiles)

        score = 0

        # Place the tiles
        tiles_empty = True # Used to ensure that the word is being placed on top of another
        for i, tile in enumerate(word):
            
            #score -= len(tile)

            this_tile_x = x + direction[0] * i
            this_tile_y = y + direction[1] * i
            # I know this is lazy deal with it
            try:
                placement_square = new_tiles[this_tile_x][this_tile_y]
            except IndexError:
                return 0
            
            if tiles_empty and len(placement_square) >= 1:
                tiles_empty = False
            
            new_tiles[this_tile_x][this_tile_y].append(Tile(tile))
            this_line_score = self.check_line(new_tiles, this_tile_x, this_tile_y, opp_dir)

            if this_line_score < 0: pass
            elif this_line_score: score += this_line_score
            else: return 0

        this_line_score = self.check_line(new_tiles, x, y, direction)

        score += len(new_tiles[x][y])
        if this_line_score: score += this_line_score
        else: return 0
                    
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
                if tile:
                    board_return += tile[-1].get_printout() + '  '
                else:
                    board_return += '_  '
            board_return += '|\n'
            board_return += '|' + '   ' * self.size + '  |'

        board_return += '\n' + '───' * self.size + '────\n'

        return board_return