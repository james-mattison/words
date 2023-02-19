from .tile import Tiles
from .board import board
from .word import Word


class Player(object):

    def __init__(self, name: str):
        self.name = name
        self.hand = {}
        self.score = 0

        self.draw_to_initial_hand()

    def get_name(self):
        return self.name

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

    def get_score(self):
        return self.score
    def play_word(self,word,  x_pos, y_pos, vertical = False):
        cb = board.play_horizontal_word
        if vertical:
            cb = board.play_vertical_word

        holding = list(self.get_hand().keys())
        need_pop = []

        for i, letter in enumerate(word):
            valid = False


            in_h = board.tile_in_horizontal_word(x_pos, y_pos, vertical)
            in_v = board.tile_in_vertical_word(x_pos, y_pos)

            if in_h is not False or in_v is not False:
                valid = True
            elif letter in self.hand.keys():
                valid = True
                need_pop.append(letter)

            if not valid:
                print(f"Cannot play {word}. Missing letter {letter} in hand: {', '.join(holding)}")
                return False


        points = cb(word, x_pos, y_pos)
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


