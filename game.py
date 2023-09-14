import random

# Class for storing information about an upwords player

class player:
    def __init__(self, name, tiles):
        self.name = name
        self.score = 0
        self.tiles = tiles

    def __str__(self):
        return self.name
    
# Class for storing information about a game of upwords

class upwords_game:
    def __init__(self, num_of_players, game_board):
        self.players = []
        self.board = game_board

        self.tiles = ['F', 'J', 'Qu', 'V', 'W', 'X', 'Z',
                      'B', 'B', 'C', 'C', 'G', 'G', 'H', 'H', 'R', 'R', 'Y', 'Y',
                      'D', 'D', 'D', 'L', 'L', 'L', 'M', 'M', 'M', 'N', 'N', 'N', 'P', 'P', 'P', 'S', 'S', 'S', 'U', 'U', 'U',
                      'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'T', 'T', 'T', 'T',
                      'A', 'A', 'A', 'A', 'A', 
                      'E', 'E', 'E', 'E', 'E', 'E']
        
        random.shuffle(self.tiles)

        tile_rack_size = 7

        for i in range(num_of_players):
            self.players.append(player(input('Player ' + str(i) + ' Name: '), self.tiles[-tile_rack_size:]))
            self.tiles = self.tiles[:-tile_rack_size]

        # Game loop 
        while len(self.tiles == 0) and any(len(self.players.tiles) == 0):
            pass