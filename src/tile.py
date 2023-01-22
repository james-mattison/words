import random

"""
tile.py: classes and methods reprenting the tiles that are already played
and the tiles that remain to be played.


"""


#
# Each letter has two values:
#  num: how many times does this letter appear in a standard game?
#  worth: how many points is this letter worth?
#
LETTER_SCORES = {
    "E": {
        "num": 12,
        "worth": 1
    },
    "A": {
        "num": 9,
        "worth": 1
    },
    "I": {
        "num": 9,
        "worth": 1
    },
    "O": {
        "num": 8,
        "worth": 1
    },
    "R": {
        "num": 6,
        "worth": 1
    },
    "N": {
        "num": 6,
        "worth": 1
    },
    "T": {
        "num": 6,
        "worth": 1
    },
    "L": {
        "num": 4,
        "worth": 1
    },
    "S": {
        "num": 4,
        "worth": 1
    },
    "U": {
        "num": 4,
        "worth": 1
    },
    "D": {
        "num": 4,
        "worth": 2
    },
    "G": {
        "num": 3,
        "worth": 2
    },
    "B": {
        "num": 2,
        "worth": 3
    },
    "C": {
        "num": 2,
        "worth": 3
    },
    "M": {
        "num": 2,
        "worth": 3
    },
    "P": {
        "num": 2,
        "worth": 3
    },
    "F": {
        "num": 2,
        "worth": 4
    },
    "H": {
        "num": 2,
        "worth": 4
    },
    "V": {
        "num": 2,
        "worth": 4
    },
    "W": {
        "num": 2,
        "worth": 4
    },
    "Y": {
        "num": 2,
        "worth": 4
    },
    "K": {
        "num": 1,
        "worth": 5
    },
    "J": {
        "num": 1,
        "worth": 8
    },
    "X": {
        "num": 1,
        "worth": 8
    },
    "Q": {
        "num": 1,
        "worth": 10
    },
    "Z": {
        "num": 1,
        "worth": 10
    }
}

class Tile:
    """
    This represents a single tile, that has a letter assigned.

    If the tile has an x, y position then we can asusme that the tile is aready in play.

    If it does not, then this tile is in the user's hand.
    """

    def __init__(self, character):
        self.character = character
        self.points = LETTER_SCORES[character]['worth']
        self.xpos = None
        self.ypos = None

    def get_points(self) -> int:
        """
        How many points is this letter worth?
        """
        return self.points

    def get_letter(self) -> str:
        """
        Whsat is the character associated with this Tile object?
        """
        return self.character

    def set_location(self, x, y):
        """
        Set the X, Y position in which this Tile hsa been played
        """
        self.xpos = x
        self.ypos = y

    def is_played(self) -> bool:
        """
        Return True if this Tile has already been played to the game board, False if not.\
        """
        if self.xpos is not None and self.ypos is not None:
            return True
        else:
            return False

    def __str__(self):
        return self.get_letter()

class Tiles:
    """
    Class that holds all the tiles that are playable in a game.

    There are a total of 100 tiles at play in a standard game.

    The _tiles array contains a tile object for every single one of them.

    As each player starts their turn, a Tile is popped from this array and added
    to the player's hand.
    """
    def __init__(self):
        self._tiles = []
        for key, value in LETTER_SCORES.items():
            for instance in range(value['num']):
                tile = Tile(key)
                self._tiles.append(tile)

    def draw_tile(self):
        """
        Draw a new Tile, popping it off of the potential in-game tiles.
        """
        idx = random.randint(0, len(self._tiles))
        return self._tiles.pop(idx)
