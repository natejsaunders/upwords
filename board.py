from PyDictionary import PyDictionary

# Class to store board data in, and also ensure goes are legal
class upwords_board:

    def __init__(self, size):
        # Generating tiles - stored as a 3d array, the inner inner arrays store the current letter on the square and the height
        self.tiles = []             #[[['_', 0]] * size] * size  <- better way of generating list but python doesn't like it :(
        for i in range(size):
            row = []
            for ii in range(size):
                row.append(['_', 0])
            self.tiles.append(row)
        self.size = size

        # Initialise possible words
        with open('wordlist.txt', 'r') as wl:
            self.wordlist = [line[:-1] for line in wl.readlines()]


    # Used to check if a given string is allowed
    def is_allowed_word(self, word):
        return word in self.wordlist
    
    # Used to add letters to the board, updating it and checking the go is legal
    def place(self, word, x, y, dir):

        # Directions (vertical or horizontal)
        directions = {
            'v' : [1, 0],
            'h' : [0, 1]
        }
        dir = directions[dir]

        # Place the word - then check all words on the board are valid
        old_tiles = self.tiles

        for i in range(len(word)):

            # I know this is lazy deal with it
            try:
                tile = self.tiles[x + dir[0] * i][y + dir[1] * i]
            except IndexError:
                return False
            
            tile[0] = word[i].upper()
            tile[1] += 1

            # Check if the square has too many tiles
            if tile[1] > 5:
                return False


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