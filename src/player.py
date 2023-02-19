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

        check_cb = board.tile_in_horizontal_word
        vertical_check_cb = board.tile_in_vertical_word

        holding = list(self.get_hand().keys())
        points = 0
        need_pop = []

        # for i, letter in enumerate(word):
        #
        #     x = x_pos
        #     y = y_pos
        #
        #     print(f"letter at {x_pos}, {y_pos}: {board.get_pos(x_pos, y_pos)}")
        #
        #     processed_words = []
        #
        #     in_h = board.tile_in_horizontal_word(x_pos, y_pos)
        #     in_v = board.tile_in_vertical_word(x_pos, y_pos)
        #
        #     h_points = 0
        #     v_points = 0
        #     if in_h:
        #         points += Word.compute_points(in_h['word'])
        #         processed_words.append(in_h['word'])
        #
        #     if in_v:
        #         points += Word.compute_points(in_v['word'])
        #         processed_words.append(in_h['word'])
        #
        #     if not points and letter in self.hand.keys():
        #         tile = self.hand.pop(letter)
        #         points += tile.get_points()
        #

        points += cb(word, x_pos, y_pos)
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


