#!/usr/bin/env python3

from src.board import board
from src.tile import Tiles, Tile
from src.player import Player
from src.word import Word


"""
words.py: A WordsWithFriends knockoff.
"""

def spaghetti_test():

    player_1 = Player(input("Player 1 Name?: "))
    player_2 = Player(input("Player 2 Name?: "))


    print(f"{player_1.get_name():<30} {player_2.get_name():>30}")
    print(f"{player_1.get_score():<30} {player_2.get_score():>30}")
    print(f"{player_1.get_letters()} {player_2.get_letters()}")



    def get_x_y_v(player):
        print("Your letters: ", player.get_letters())
        print("Your score: ", player.get_score())

        rets = []
        for typecheck in [input("X: "), input("Y: ")]:
            try:
                typecheck = int(typecheck)
                rets.append(typecheck)
            except (TypeError, ValueError) as e:
                print(e)
                print(f"Bad {typecheck}")
                return False
        v = None
        while v not in [True, False]:
            yn = input("Vertical: ")
            yes = ["y", "Y", "YES", "yes"]
            no = ["n", "N", "No", "no"]
            if yn in yes:
                v = True
            elif yn in no:
                v = False
            else:
                print("Bullshit value entered. Yes or no.")



        rets.append(v)
        return rets[0], rets[1], rets[2]

    while True:
        inner_break = False

        for player in [player_1, player_2]:
            if inner_break:
                inner_break = False
                continue
            board.print_board()
            t = len(player.get_name()) * "="
            s = f"+{t}+"
            print(s)
            print("|" + player.get_name() + "|")
            print(s)

            coords = get_x_y_v(player)
            if coords is False:
                print("Bad coordinates given!")
                continue


            x, y, v = coords

            p = ""

            while not p:
                try:
                    p = input("Word:")
                except KeyboardInterrupt:
                    inner_break = True
                    continue


            if not player.play_word(p, int(y), int(x), vertical=v):
                inner_break = True
                continue

            player.draw_to_initial_hand()



if __name__ == '__main__':
    # test the spaghetti
    spaghetti_test()