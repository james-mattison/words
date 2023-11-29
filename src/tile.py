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
    },
    "[BLANK]": {
        "num": 10,
        "worth": 1
    },
    " ": {
        "num": 0,
        "worth": 0
    }
}

TILE_MODIFIERS = {
    "0": {
        "0": {
            "y": 0,
            "x": 0,
            "val": "TW"
        },
        "3": {
            "y": 0,
            "x": 3,
            "val": "DL"
        },
        "7": {
            "y": 0,
            "x": 7,
            "val": "TW"
        },
        "11": {
            "y": 0,
            "x": 11,
            "val": "DL"
        },
        "14": {
            "y": 0,
            "x": 14,
            "val": "TW"
        }
    },
    "1": {
        "1": {
            "y": 1,
            "x": 1,
            "val": "DW"
        },
        "5": {
            "y": 1,
            "x": 5,
            "val": "TL"
        },
        "9": {
            "y": 1,
            "x": 9,
            "val": "TL"
        },
        "13": {
            "y": 1,
            "x": 13,
            "val": "DW"
        }
    },
    "2": {
        "2": {
            "y": 2,
            "x": 2,
            "val": "DW"
        },
        "6": {
            "y": 2,
            "x": 6,
            "val": "DL"
        },
        "8": {
            "y": 2,
            "x": 8,
            "val": "DL"
        },
        "12": {
            "y": 2,
            "x": 12,
            "val": "DW"
        }
    },
    "3": {
        "0": {
            "y": 3,
            "x": 0,
            "val": "DL"
        },
        "3": {
            "y": 3,
            "x": 3,
            "val": "DW"
        },
        "7": {
            "y": 3,
            "x": 7,
            "val": "DL"
        },
        "11": {
            "y": 3,
            "x": 11,
            "val": "DW"
        },
        "14": {
            "y": 3,
            "x": 14,
            "val": "DL"
        }
    },
    "4": {
        "4": {
            "y": 4,
            "x": 4,
            "val": "DW"
        },
        "10": {
            "y": 4,
            "x": 10,
            "val": "DW"
        }
    },
    "5": {
        "1": {
            "y": 5,
            "x": 1,
            "val": "TL"
        },
        "5": {
            "y": 5,
            "x": 5,
            "val": "TL"
        },
        "9": {
            "y": 5,
            "x": 9,
            "val": "TL"
        },
        "13": {
            "y": 5,
            "x": 13,
            "val": "TL"
        }
    },
    "6": {
        "2": {
            "y": 6,
            "x": 2,
            "val": "DL"
        },
        "6": {
            "y": 6,
            "x": 6,
            "val": "DL"
        },
        "8": {
            "y": 6,
            "x": 8,
            "val": "DL"
        },
        "12": {
            "y": 6,
            "x": 12,
            "val": "DL"
        }
    },
    "7": {
        "0": {
            "y": 7,
            "x": 0,
            "val": "TW"
        },
        "3": {
            "y": 7,
            "x": 3,
            "val": "DL"
        },
        "7": {
            "y": 7,
            "x": 7,
            "val": "**"
        },
        "11": {
            "y": 7,
            "x": 11,
            "val": "DL"
        },
        "14": {
            "y": 7,
            "x": 14,
            "val": "TW"
        }
    },
    "8": {
        "2": {
            "y": 8,
            "x": 2,
            "val": "DL"
        },
        "6": {
            "y": 8,
            "x": 6,
            "val": "DL"
        },
        "8": {
            "y": 8,
            "x": 8,
            "val": "DL"
        },
        "12": {
            "y": 8,
            "x": 12,
            "val": "DL"
        }
    },
    "9": {
        "1": {
            "y": 9,
            "x": 1,
            "val": "TL"
        },
        "5": {
            "y": 9,
            "x": 5,
            "val": "TL"
        },
        "9": {
            "y": 9,
            "x": 9,
            "val": "TL"
        },
        "13": {
            "y": 9,
            "x": 13,
            "val": "TL"
        }
    },
    "10": {
        "4": {
            "y": 10,
            "x": 4,
            "val": "DW"
        },
        "10": {
            "y": 10,
            "x": 10,
            "val": "DW"
        }
    },
    "11": {
        "0": {
            "y": 11,
            "x": 0,
            "val": "DL"
        },
        "3": {
            "y": 11,
            "x": 3,
            "val": "DW"
        },
        "7": {
            "y": 11,
            "x": 7,
            "val": "DL"
        },
        "11": {
            "y": 11,
            "x": 11,
            "val": "DW"
        },
        "14": {
            "y": 11,
            "x": 14,
            "val": "DL"
        }
    },
    "12": {
        "2": {
            "y": 12,
            "x": 2,
            "val": "DW"
        },
        "6": {
            "y": 12,
            "x": 6,
            "val": "DL"
        },
        "8": {
            "y": 12,
            "x": 8,
            "val": "DL"
        },
        "12": {
            "y": 12,
            "x": 12,
            "val": "DW"
        }
    },
    "13": {
        "1": {
            "y": 13,
            "x": 1,
            "val": "DW"
        },
        "5": {
            "y": 13,
            "x": 5,
            "val": "TL"
        },
        "9": {
            "y": 13,
            "x": 9,
            "val": "TL"
        },
        "13": {
            "y": 13,
            "x": 13,
            "val": "DW"
        }
    },
    "14": {
        "0": {
            "y": 14,
            "x": 0,
            "val": "TW"
        },
        "3": {
            "y": 14,
            "x": 3,
            "val": "DL"
        },
        "7": {
            "y": 14,
            "x": 7,
            "val": "TW"
        },
        "11": {
            "y": 14,
            "x": 11,
            "val": "DL"
        },
        "14": {
            "y": 14,
            "x": 14,
            "val": "TW"
        }
    }
}


class Modifiers:

    @staticmethod
    def get_modifier(x, y):
        if TILE_MODIFIERS.get(str(y)):
            if TILE_MODIFIERS[str(y)].get(str(x)):
                return TILE_MODIFIERS[str(y)][str(x)]



class Tile:
    """
    This represents a single tile, that has a letter assigned.

    If the tile has an x, y position then we can asusme that the tile is aready in play.

    If it does not, then this tile is in the user's hand.
    """

    def __init__(self, character):

        self.character = character.upper()
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

    def get_location(self):
        """
        Return the X, Y coordinates of this tile.
        """
        return self.xpos, self.ypos

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

    _tiles = []
    _played = []
    def __init__(self):
        if not self._tiles:
            for key, value in LETTER_SCORES.items():
                for instance in range(value['num']):
                    tile = Tile(key)
                    self._tiles.append(tile)

    def draw_tile(self):
        """
        Draw a new Tile, popping it off of the potential in-game tiles.
        """
        if len(self._tiles) == 0:
            print("Drew all the tiles. Game over.")
            return False
        idx = random.randint(0, len(self._tiles)) - 1
        tile = self._tiles.pop(idx)
        self._played.append(tile)
        return tile
