from .tile import LETTER_SCORES
import os
import json

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Dictionary:

    dictionaries = {}

    def __init__(self, dictionary_directory_path: str):
        self.dictionaries_path = dictionary_directory_path
        self.load_dictionaries()

    def load_dictionaries(self):
        if not self.dictionaries:
            for character in ALPHABET:
                letterfile = os.path.join(os.path.abspath(self.dictionaries_path), f"{character}.json")
                with open(letterfile, "r") as _o:
                    self.dictionaries[character.upper()] = json.load(_o)

    def valid_word(self, word: str):
        key = word[0].upper()
        return word.upper() in self.dictionaries[key]


class Word:
    """
    Methods to deal with the validity of a word that is played, and to determine
    the value of each word a player plays, less the value of points that were already on the board.
    """

    @staticmethod
    def compute_points(word: str):
        points = 0
        for i in range(len(word)):
            v = LETTER_SCORES[word[i]]['worth']
            print(f"{word[i]} -> {v} points")
            points += v
        return points

