from .tile import Tile, Tiles

class Board:

    def __init__(self, x_limit = 15, y_limit = 15):
        self.x = [n for n in range(15)]
        self.y = [n for n in range(15)]
        self.grid = []
        for i in range(15):
            self.grid.append([])
            for p in range(15):
                self.grid[i].append(' ')

    def set_letter_position(self, letter: str or Tile, y: int, x: int):
        if x > 15 or x < 0:
            print("Invalid x")
            return False
        if y > 15 or y < 0:
            print("Invalid y")
            return False
        if isinstance(self.grid[y][x], str) and self.grid[y][x] != letter and self.grid[y][x] != " ":
            print(f"Already have letter {self.grid[x][y]}at {x},{y}")
            return False
        if isinstance(letter, Tile) and self.grid[y][x] != " " and self.grid[y][x].get_letter() != letter.get_letter():
            print(f"Already have tile {self.grid[y][x]} at x: {x}, y: {y}")
            return False
        # print(f"Placing {letter} at x: {x} and y: {y}"
        if not isinstance(letter, Tile):
            letter = Tile(letter)
        self.grid[y][x]= letter
        if not letter.is_played():
            letter.set_location(x, y)
        return letter.get_points()

    def print_board(self, silent = False):
        s = ""
        for i in range(len(self.grid)):
            for p in range(len(self.grid[i])):
                if self.grid[i][p] == ' ':
                    if not silent:
                        print("| ", end = "", flush = True)
                    s += "| "
                else:
                    if not silent:
                        print(f"|{self.grid[i][p]}", end = "", flush = True)
                    s += f"|{self.grid[i][p]}"
            s += "\n"
            if not silent:
                print()
        return s

    def play_horizontal_word(self, word: str, x_start, y_pos):
        points = 0
        if x_start + len(word) > 15:
            print(f"Word {word} too long to fit on board!")
            return False
        for i in range(len(word)):
            tile = Tile(word[i])
            self.set_letter_position(tile, x_start + i, y_pos)
            points += tile.get_points()
        print(f"Played '{word}' for {points} points.")
        return points

    def tile_in_horizontal_word(self, xpos, ypos, vertical = False):
        idx = 0
        letter = self.grid[ypos][xpos]

        word = ""
        if vertical:
            xpos, ypos = ypos, xpos
        if self.grid[ypos][xpos] != " ":
            word += self.grid[ypos][xpos].get_letter()
        # letter to the left?
        if xpos > 0:
            x = xpos - 1
            if self.grid[ypos][x] not in ['', ' ']:
                word += self.grid[ypos][x].get_letter()
                while x >= 0:
                    x -= 1
                    if self.grid[ypos][x] == " " or self.grid[ypos][x] == "":
                        break
                    idx += 1
                    tile = self.grid[ypos][x]
                    word += self.grid[ypos][x].get_letter()
        if word:
            word = word[::-1]
        # letter to the right?
        if xpos < 15:
            x = xpos + 1
            if self.grid[ypos][x] != " ":
                word += self.grid[ypos][x].get_letter()
                while x <= 15 and self.grid[ypos][x + 1] != " ":
                    x += 1
                    word += self.grid[ypos][x].get_letter()
        if word:
            for i in range(len(word)):
                if word[i] == self.grid[ypos][xpos].get_letter():
                    idx = i
                    break
            return {
                "x": xpos,
                "y": ypos,
                "tile": self.grid[ypos][xpos],
                "letter": self.grid[ypos][xpos].get_letter(),
                "word": word,
                "index": idx
            }
        else:
            return False

    def tile_in_vertical_word(self, xpos, ypos):
        return self.tile_in_horizontal_word(xpos, ypos, vertical = True)

    def play_vertical_word(self, word: str, x_pos, y_start):
        points = 0
        if y_start + len(word) > 15:
            print(f"Word {word} too long to fit on board!")
            return False
        for i in range(len(word)):
            tile = Tile(word[i])
            self.set_letter_position(tile, x_pos, y_start + i)
            points += tile.get_points()
        print(f"Played '{word}' for {points} points")
        return points

    def get_board(self):
        return self.grid

    def __str__(self):
        return self.print_board(silent = True)



def test():
    b = Board()
    b.play_horizontal_word("FART", 7, 7)
    b.play_vertical_word("FACT", 7, 7)

    def inword(o):
        if o is False:
            print("Not in word")
        else:
            print(o)

    inword(b.tile_in_horizontal_word(7, 7))
    inword(b.tile_in_vertical_word(7, 7))
    inword(b.tile_in_horizontal_word(5, 7))
    inword(b.tile_in_vertical_word(5, 7))
    inword(b.tile_in_horizontal_word(5, 8))
    inword(b.tile_in_vertical_word(7, 8))
    inword(b.tile_in_vertical_word(7, 9))
    inword(b.tile_in_horizontal_word(7, 10))
    inword(b.tile_in_vertical_word(10, 7))
