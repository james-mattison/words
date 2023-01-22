from .tile import LETTER_SCORES


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

