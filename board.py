from PyDictionary import PyDictionary
import copy

# Class to store board data in, and also ensure goes are legal
class upwords_board:

    def __init__(self, size):
        self.empty_tile = '_'

        # Generating tiles - stored as a 3d array, the inner inner arrays store the current letter on the square and the height
        self.tiles = []             #[[['_', 0]] * size] * size  <- better way of generating list but python doesn't like it :(
        for i in range(size):
            row = []
            for ii in range(size):
                row.append([self.empty_tile, 0])
            self.tiles.append(row)
        self.size = size

        # Initialise possible words
        with open('wordlist.txt', 'r') as wl:
            self.wordlist = [line[:-1] for line in wl.readlines()]


    # Used to check if a given string is allowed
    def is_allowed_word(self, word):
        return word.lower() in self.wordlist
    
    # Check if a line (row or column) is valid
    def is_allowed_line(self, line):

        tiles = [t[0] for t in line]

        words = []
        word = ''
        for t in tiles:
            if t != self.empty_tile:
                word += t
            elif len(word) > 1:
                words.append(word)
                word = []
            else:
                word = []

        return all(map(self.is_allowed_word, words))
        
    
    # Used to add letters to the board, updating it and checking the go is legal
    def place(self, word, y, x, dir, first_go = False):

        # Directions (vertical or horizontal)
        directions = {
            'v' : [1, 0],
            'h' : [0, 1]
        }
        dir = directions[dir]

        # Place the word - then check all words on the board are valid
        new_tiles = copy.deepcopy(self.tiles)

        # Place the tiles
        tiles_empty = True # USed to ensure that the word is being placed on top of another
        for i in range(len(word)):
            # I know this is lazy deal with it
            try:
                tile = new_tiles[x + dir[0] * i][y + dir[1] * i]
            except IndexError:
                return False
            
            if tile[1] > 0:
                tiles_empty = False

            tile[0] = word[i].upper()
            tile[1] += 1

            # Check if the square has too many tiles
            if tile[1] > 5:
                return False
        # If there is no word being played on and it isn't the first go: fail
        if tiles_empty and not first_go: return False

        # Now check that every word on the board is valid (this may be more effecient if you only check modified rows and columns but i cba to try)
        for row in new_tiles:
            if not self.is_allowed_line(row): return False

        for i in range(self.size):
            if not self.is_allowed_line([row[i] for row in new_tiles]): return False
        
        self.tiles = new_tiles
        return True
            
    # Return a nice way of presenting the board
    def __str__(self):
        #print(self.tiles)

        board_return = ''

        board_return += '───' * self.size + '────\n'
        board_return += '|' + '   ' * self.size + '  |'
        
        for row in self.tiles:
            board_return += '\n|  '
            for tile in row:
                board_return += tile[0] + '  '
            board_return += '|\n'
            board_return += '|' + '   ' * self.size + '  |'

        board_return += '\n' + '───' * self.size + '────\n'

        return board_return