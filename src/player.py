from .tile import Tiles
from .board import board
from .utils import *


class Player(object):

    tiles = None

    def __init__(self, name: str):
        if not self.tiles: self.tiles = Tiles()
        self.name = name
        self.hand = {}
        self.score = 0
        self.msg = ""

        self.draw_to_initial_hand()

    def __str__(self):
        s = "+" + ("-" * 38) + "+\n"
        s+= "|{:^38}|\n".format(self.get_name())

        hand = "".join(self.get_letters())
        hand = hand.replace("[BLANK]", "\u001b[43;1m*\u001b[0m")

        s+= "|{:<19}{:>19}|\n".format(
            f"HAND: {hand}",
            f"SCORE: {self.get_score()}"
        )

        s += "+" + ("-" * 38) + "+\n"
        return s

    def get_name(self):
        return self.name

    def print_msg(self):
        if self.msg:
            print(self.msg)
            self.msg = ""

    def draw_tile(self):
        if len(self.hand.keys()) > 7:
            print(red("Attempted to draw more than one tile"))
        return self.tiles.draw_tile()

    def add_points(self, num_points: int):
        self.score += num_points

    def draw_to_initial_hand(self):
        while len(self.hand) < 7:
            tile = self.draw_tile()
            self.hand[tile.get_letter()] = tile

    def letter_in_hand(self, letter: str):
        """determine if we have this letter ot play"""
        return letter.upper() in self.hand.keys()

    def invalid_word(self, word: str) -> bool:
        """
        Determine whether all the letters on <word> are in the player's hand.
        """

        bad = []
        for char in word:
            if not char in self.hand.keys():
                bad.append(char)
        if bad:
            return bad
        else:
            return False

    def get_hand(self):
        return self.hand

    def get_score(self):
        return self.score

    def play_word(self, word,  x_pos, y_pos, vertical = False):

        missing = self.invalid_word(word)
        if missing:
            self.msg = red(f"Couldn't play word - missing letters {', '.join(missing)} from your hand!")
            return False


        cb = board.play_horizontal_word
        if vertical:
            cb = board.play_vertical_word


        holding = list(self.get_hand().keys())
        points = 0
        need_pop = []


        points = cb(self, word, x_pos, y_pos)

        if not points:
            return False

        self.add_points(points)

        for n in need_pop:
            print("Popping: ", self.hand[n])
            self.hand.pop(n)

        return True

    def get_letters(self):
        letters = []

        for k in self.hand.keys():
            letters.append(k)
        return letters


