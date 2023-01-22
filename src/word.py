from .tile import LETTER_SCORES

class Word:

    @staticmethod
    def compute_points(word):
        points = 0
        for i in range(len(word)):
            v = LETTER_SCORES[word[i]]['worth']
            print(f"{word[i]} -> {v} points")
            points += v
        return points
