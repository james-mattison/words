from .word import Dictionary
from .player import Player
from .board import board


class Game:

    def __init__(self,
                 player1_name: str = None,
                 player2_name: str = None,
                 ):
        self.dictionary = Dictionary()
        player1_name = player1_name or input("Player1 Name: ")
        player2_name = player2_name or input("Player2 Name: ")
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def get_play(self, player: Player, x_pos: int = None, y_pos: int = None, vertical = None):
        print(f"Score: {player.get_score()}")
        print(f"Letters: {player.get_letters()}")

        if not x_pos:
            x_pos = input("X: ")
        if not y_pos:
            y_pos = input("Y: ")
        if vertical is None:
            vertical =  not input("Vertical? ").upper() in ["Y", "YES"]

        for n, point in {"x": x_pos, "y": y_pos}.items():
            try:
                int(point)
            except (TypeError, ValueError) as e:
                print(e)
                print(f"{n} invalid value {point}, expecting an int")

        return x_pos, y_pos, vertical


    def run_game(self):
        inner_break = False
        while True:
            print(f"Outer loop")
            if inner_break:
                inner_break = False
                continue


            for player in [self.player1, self.player2]:
                board.print_board()

                print(player)

                x, y, v = word_pos = self.get_play(player)

                played = False
                while played is False:
                    word = input("WORD: ")
                    played = player.play_word(word, x, y, v)
                    player.print_msg()
                player.draw_to_initial_hand()
                inner_break = True

