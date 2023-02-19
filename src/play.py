from .tile import Tiles
from .board import board

class Player(object):

    def __init__(self):
        self.hand = {}
        self.score = 0

    def draw_tile(self):
        if len(self.hand.keys()) > 7:
            print("Attempted to draw more than one tile")
        tiles = Tiles()
        return tiles.draw_tile()

    def add_points(self, num_points: int):
        self.score += num_points

    def draw_to_initial_hand(self):
        while len(self.hand) < 7:
            tile = self.draw_tile()
            self.hand[tile.get_letter()] = tile

    def get_hand(self):
        return self.hand

    def play_word(self,word,  x_pos, y_pos, vertical = False):
        cb = board.play_horizontal_word
        if vertical:
            cb = board.play_vertical_word

        holding = list(self.get_hand().keys())
        for letter in word:
            if not letter in holding:
                print(f"Cannot play {word}. Missing letter {letter} in hand: {', '.join(holding)}")
                return False

        points = cb(word, x_pos, y_pos)
        self.add_points(points)

        for letter in word:
            if letter in self.hand.keys():
                self.hand.pop(letter)

        self.draw_to_initial_hand()



