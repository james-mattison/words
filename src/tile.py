import random


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

    def __init__(self, character):
        self.character = character
        self.points = LETTER_SCORES[character]['worth']
        self.xpos = None
        self.ypos = None

    def get_points(self):
        return self.points

    def get_letter(self):
        return self.character

    def set_location(self, x, y):
        self.xpos = x
        self.ypos = y

    def is_played(self):
        if self.xpos is not None and self.ypos is not None:
            return True
        else:
            return False

    def __str__(self):
        return self.get_letter()

class Tiles:

    def __init__(self):
        self._tiles = []
        for key, value in LETTER_SCORES.items():
            for instance in range(value['num']):
                tile = Tile(key)
                self._tiles.append(tile)

    def draw_tile(self):
        idx = random.randint(0, len(self._tiles))
        return self._tiles.pop(idx)
