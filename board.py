from PyDictionary import PyDictionary
import copy
import time

# TODO Make scoring happen for all words and columns that have been played on, also check only these words on columns for changes

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
        with open('wordlist.txt', 'r') as wl: self.wordlist = [line[:-1] for line in wl.readlines()]

        # Used to determine whether it is the first go on this board
        self.first_go = True


    # Used to check if a given string is allowed (we also allow Qu because we need to)
    def is_allowed_word(self, word):
        if word == 'Qu': return True
        else: return word.lower() in self.wordlist
    
    # Check if a line (row or column) is valid
    def is_allowed_line(self, line):
        tiles = [t[0] for t in line]

        words = []
        word = ''
        for t in tiles:
            if t != self.empty_tile:
                word += t
            elif len(word) > 1:
                words.append(''.join(word))
                word = []
            else:
                word = []

        print(words)
        return all(map(self.is_allowed_word, words))
        
    
    # Used to add letters to the board, updating it and checking the go is legal
    def place(self, placement_data):
        word = placement_data['word']
        y =    placement_data['y']
        x =    placement_data['x']
        direction =  placement_data['direction']

        word = word.upper()
        # Directions (vertical or horizontal)
        directions = {
            'v' : [1, 0],
            'h' : [0, 1]
        }
        direction = directions[direction]

        # Managing the Qu tile
        try:
            q_loc = word.index('Q')
            if q_loc >= 0: word = word[:q_loc + 1] + word[q_loc + 2:]
        except ValueError:
            pass

        # Place the word - then check all words on the board are valid
        new_tiles = copy.deepcopy(self.tiles)

        score = 0

        # Place the tiles
        tiles_empty = True # Used to ensure that the word is being placed on top of another
        for i in range(len(word)):
            # I know this is lazy deal with it
            try:
                tile = new_tiles[x + direction[0] * i][y + direction[1] * i]
            except IndexError:
                return 0
            
            if tile[1] > 0:
                tiles_empty = False

            # Managing Qu tile, also checking placed tile is different
            if word[i] == ' ':
                pass
            elif word[i] == 'Q':
                if tile[0] == 'Qu': return 0
                tile[0] = 'Qu'
            else:
                if tile[0] == word[i]: return 0
                tile[0] = word[i]

            tile[1] += 1
            score += tile[1]

            # Check if the square has too many tiles
            if tile[1] > 5:
                return 0
            
        # If there is no word being played on and it isn't the first go: fail
        if tiles_empty and not self.first_go: return 0

        # Now check that every word on the board is valid (this may be more effecient if you only check modified rows and columns but i cba to try)
        for row in new_tiles:
            if not self.is_allowed_line(row): return 0

        for i in range(self.size):
            if not self.is_allowed_line([row[i] for row in new_tiles]): return 0
        
        # Update tiles to the changed tiles as the go is valid
        self.tiles = new_tiles

        self.first_go = False
        return score
            
    # Return a nice way of presenting the board
    def __str__(self):
        #print(self.tiles)

        board_return = ''

        board_return += '───' * self.size + '────\n'
        board_return += '|' + '   ' * self.size + '  |'
        
        for row in self.tiles:
            board_return += '\n|  '
            for tile in row:
                if tile[0] == 'Qu': board_return += tile[0] + ' '
                else: board_return += tile[0] + '  '
            board_return += '|\n'
            board_return += '|' + '   ' * self.size + '  |'

        board_return += '\n' + '───' * self.size + '────\n'

        return board_return