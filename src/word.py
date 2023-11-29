from .tile import LETTER_SCORES, Modifiers
import os
import json

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Dictionary:

    def __new__(cls, *args, **kwargs):
        """
        Create this as a singleton. We only want to load all the dictionaries,
        which contain a little over 100,000 words total, ONLY time if we can.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    dictionaries = {}

    def __init__(self, dictionary_directory_path: str = None):
        if not dictionary_directory_path:
            dictionary_directory_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dictionaries")
        self.dictionaries_path = dictionary_directory_path
        if not os.path.exists(dictionary_directory_path):
            raise Exception(f"Dictionaries path {dictionary_directory_path} does not exist!")

        self._load_dictionaries()

    def _load_dictionaries(self):
        """
        Iterate self.dictionaries_path's contents, loading each letter sequentially.
        """
        if not self.dictionaries:
            for character in ALPHABET:
                letterfile = os.path.join(os.path.abspath(self.dictionaries_path), f"{character}.json")
                if not os.path.exists(letterfile):
                    raise Exception(f"FATAL: {letterfile} does not exist. Did you run bin/build_dicts.py to populate this dir?")

                with open(letterfile, "r") as _o:
                    self.dictionaries[character.upper()] = json.load(_o)

    def valid_word(self, word: str):
        key = word[0].upper()
        return word.lower() in self.dictionaries[key].keys()


class Word(Dictionary):
    """
    Methods to deal with the validity of a word that is played, and to determine
    the value of each word a player plays, less the value of points that were already on the board.
    """


    @staticmethod
    def compute_points(word: str):
        """
        Compute the number of points that are scored by a word.
        """
        points = 0
        for i in range(len(word)):
            v = LETTER_SCORES[word[i]]['worth']
            print(f"{word[i]} -> {v} points")
            points += v
        return points
