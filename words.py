#!/usr/bin/env python3

from src.board import board
from src.tile import Tiles, Tile
from src.player import Player
from src.word import Word


"""
words.py: A WordsWithFriends knockoff.
"""

def setup():



    player_1 = Player("Adam")
    player_2 = Player("Eve")


    print(f"{player_1.get_name():<30} {player_2.get_name():>30}")
    print(f"{player_1.get_score():<30} {player_2.get_score():>30}")
    print(f"{player_1.get_letters()} {player_2.get_letters()}")
    p = input(" word")
    player_1.play_word(p, 7, 7)
    return locals()

if __name__ == '__main__':
    state = setup()
    print(board)