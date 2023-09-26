import random
from gui import upwords_gui

# Class for storing information about an upwords player

class Player:
    def __init__(self, name, tiles):
        self.name = name
        self.score = 0
        self.tiles = tiles

    def __str__(self):
        return self.name
    
    # Get a Player's Input on what and where to place, also make sure the go is valid
    def go(self):
        while True:
            x = input('Y-Coordinate to Place: ')
            y = input('X-Coordinate to Place: ')
            try:
                x = int(x)
                y = int(y)
                break
            except ValueError:
                print('Coordinates not numbers')
        
        while True:
            word = list(input('Word to place: ').upper())

            if  all(c in self.tiles or c == " " for c in word):
                word = "".join(word)
                break

            print('Word not possible with available tiles')
        
        while True:
            direction = input('Direction (H)orizontal or (V)ertical: ').lower()

            if direction == 'h' or direction == 'v':
                break

            print('Direction needs to be \'h\' or \'v\'')

        return {'word': word, 'y': y, 'x': x, 'direction': direction}

    
    def has_tiles(self):
        return len(self.tiles) != 0
    
# Class for storing information about a game of upwords

class Game:
    def __init__(self, num_of_players, game_board):

        self.gui = upwords_gui()

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
            self.players.append(Player(input(f'Player {str(i)} Name: '), self.tiles[-tile_rack_size:]))
            self.tiles = self.tiles[:-tile_rack_size]

    def get_valid_player_go(self, player):
        while True:
            print(self.board)
            print(f'{player} to go (score: {player.score}) with tiles: {player.tiles}')
            player_go = player.go()
            score = self.board.place(player_go)

            # If score is not 0 then the go is legal
            if score > 0:
                for placed_tile in player_go['word']:
                    if placed_tile != ' ': player.tiles.remove(placed_tile)

                for i in range(len(player_go['word'])):
                    if len(self.tiles) > 0: player.tiles.append(self.tiles.pop())

                player.score += score
                self.gui.update(self.board)
                break

            print('Go not valid, try again.')
                    
    def start(self):
        # Game loop 
        while len(self.tiles) != 0 or all(map(Player.has_tiles, self.players)): # Check that the tiles list has letters in or that all of the players tiles list has tiles in
            for player in self.players:
                self.get_valid_player_go(player)