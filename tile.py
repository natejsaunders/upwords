# File to contain a tile object
# I started by just using characters but there were too many issues with Qu and blank spaces etc.

class Tile:

    def __init__(self, letter = ''):

        self.blank = False

        if letter == '':
            self.blank = True

        self.letter = letter

    def get_letter(self):
        return self.letter
    
    def get_printout(self):
        return self.letter
    
    def __str__(self) -> str:
        return self.letter