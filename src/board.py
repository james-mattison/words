from .tile import Tile, Tiles

#
# board.py
#   This file contains the Board class, which is used to represent the grid for the game
#   and the position of tiles relative to it.
#

class Board:
<<<<<<< HEAD
=======
    ""
>>>>>>> 0d15f7500ee4eb0a0540b8e685e017bba24e4254
    """
    Class representing the grid that is used to play the game.
    
    This class implements methods to manage the placement of tiles on the game board.
    
    Methods:
      set_letter_placement <letter> <xpos> <ypos>
        Place a Tile object that represents <letter> on the board at (xpos, ypos)
    """
<<<<<<< HEAD

    _played_coordinates = []
=======
>>>>>>> 0d15f7500ee4eb0a0540b8e685e017bba24e4254

    def __init__(self, x_limit = 15, y_limit = 15):
        self.x = [n for n in range(15)]
        self.y = [n for n in range(15)]
        self.grid = []
        for i in range(15):
            self.grid.append([])
            for p in range(15):
                self.grid[i].append(' ')

    def set_letter_position(self, letter: str or Tile, y: int, x: int) -> bool or int:
        """
        Given <letter>, create a Tile object and then place this tile on the game board.
        <x>, <y> must be between 0 and 15

        This function modifies the grid object.

        If the letter is being placed on a square in the grid that does not contain any Tiles,
        then returns the number of points - without modification (ie, no triple word/letter scoring)
        for the placement of that letter.

        If there is already a Tile there and that tile represents a _different_ letter, then returns
        False.

        A retrun of False from this function means that the letter placement was invalid.
        """
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

        if not isinstance(letter, Tile):
            letter = Tile(letter)
        self.grid[y][x]= letter
        if not letter.is_played():
            letter.set_location(x, y)
        return letter.get_points()

    def print_board(self, silent: bool = False) -> str:
        """
        Print a string representation of the board.
        """
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

<<<<<<< HEAD
=======
    def play_horizontal_word(self, word: str, x_start, y_pos):
        """
        Iteratively call set_letter_position for each letter in a word that is being placed horizontally.

        <word> needs to be a string representing a word to play.
        <x_start> represents the X-axis position for the start of the word. This is where the first letter
                  will be placed. Letters will be successively placed starting at this position until the end of
                  the word is reached.
        <y_pos>   The y-axis value for the whole word (since this is a horizonal word, this value will not change)

        """
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

>>>>>>> 0d15f7500ee4eb0a0540b8e685e017bba24e4254
    def tile_in_horizontal_word(self, xpos, ypos, vertical = False):
        """
        Given <xpos> and <ypos>, does the tile that these coordinates represent on the board
        contain a Tile object? Or a blank space?

        If this (x, y) pair contains a valid Tile object (ie, there's a letter here)
        then it returns a dictionary with the following keys:
        { "x": <the X axis on the game board>
          "y": <the Y axis on the game board>
          "tile": <the Tile object that is currently assigned to this (x, y) position on the game board
          "letter": <The literal character that the Tile represents.
          "word": <The entire word, horizontally, that contains this Tile
          "index": <The letter position that xpos/ypos represents. For example, if the word is HEY, and
                   the x,y pair points to 'E', then the index is 1 (indexed by zero).>
        }

        If this tile contains a blank (ie, no letter played here), then this function returns false.

        If <vertical> is set to true, then the rows along the Y axis are queried to find the word (ie, it is a vertical
                      word)
        """

        idx = 0  # What position is this letter in? ie, if we are looking at the middle of a word, what number is
                 # this character?


        letter = self.grid[ypos][xpos] # The current contents of the square in the gird. Should be either a Tile object
                                       # or " ".


        word = ""
        if vertical:                   # If we are dealing with a vertical word, then swap the x and y positions.
            xpos, ypos = ypos, xpos

        # Is there a Tile already played here?
        if self.grid[ypos][xpos] != " ":
            # Yes, there is. Get the character that this tile represents...
            word += self.grid[ypos][xpos].get_letter()

        # Is there a Tile directly to the left of the tile at xpos, ypos? If so then that means
        # that there is a word already played. We need to decrement along the X axis to find the start
        # of the word.
        #
        # In practice:
        # if xpos, ypos matches the "R" in the word "ART", then we move to the left to get the "A".
        # After this conditional, our word will be [ "R", "A" ] (since we added the A to the end of the array)
        if xpos > 0:
            # Move left along the X axis
            x = xpos - 1

            if self.grid[ypos][x] not in ['', ' ']:
                # We have a literal letter one square to the left.
                word += self.grid[ypos][x].get_letter()

                # Sinde we have a letter to the left, continue looking along the X axis to the left to
                # find the start of the word.
                # If vertical == Ture, then iterate DOWN the column on the Y axis until the start of the
                # word is found.

                while x >= 0:
                    # shift one square to the left (or down)
                    x -= 1

                    # blank - means that the previous square is the beginning of the word.
                    if self.grid[ypos][x] == " " or self.grid[ypos][x] == "":
                        break

                    # the x'th letter of the word, represented by xpos, ypos on the grid?
                    idx += 1

                    # Get the tile object...
                    tile = self.grid[ypos][x]

                    # ... and then retrieve the letter that this tile represents.
                    word += self.grid[ypos][x].get_letter()

        # Reverse the word order. This makes the [ "R", "A" ] in "ART" above start with "A"
        if word:
            word = word[::-1]

        # Now we will move to the right (or up, if vertical == True) of the Tile represented by xpos, ypos...
        if xpos < 15: # 15 squares == end of the board
            x = xpos + 1 # Letter to the right (or above, if vertical == True)

            # If it's a blank square then we have reached the end of the word.
            if self.grid[ypos][x] != " ":
                # If it's not blank, then add it to word. This part of the conditional will catch the "T" in the
                # word "ART" above"
                word += self.grid[ypos][x].get_letter()

                # Do we have more letters after this?
                while x <= 15 and self.grid[ypos][x + 1] != " ":
                    x += 1
                    word += self.grid[ypos][x].get_letter()
        # in the first conditional, starting with "R" in "ART", we have AR
        # in the second conditional, starting with "R" in "ART", we have "RT"
        # Concatenate this together to form the representive word...
        if word: # We have at least one non-blank tile...
            for i in range(len(word)):
                # Find the index where this letter appears in a word...
                # A  R  T
                # ^  ^  ^
                # 0  1  2
                # ... in the example of ART, the index is "1"
                if word[i] == self.grid[ypos][xpos].get_letter():
                    idx = i
                    break
            return {
                "x": xpos, # input, X
                "y": ypos, # input, Y
                "tile": self.grid[ypos][xpos], # Tile object
                "letter": self.grid[ypos][xpos].get_letter(), # Letter that the Tile represents
                "word": word, # The complete word, horizontally... if <vertical> == True, then the complete word, vertically
                "index": idx # the position  this letter appears int he word
            }
        else:
            # We got jadk shit - this square is blank and hasn't been played.
            return False

    def tile_in_vertical_word(self, xpos, ypos):
        """
        Is this tile in a vertical word? See above function for more.
        """
        return self.tile_in_horizontal_word(xpos, ypos, vertical = True)

    def play_vertical_word(self, word: str, x_pos: int, y_start: int):
        """
        play <word> vertically.
        x_pos represents the starting position on the X axis, y_start represents the position on the Y.
        Iteratively adds tiles down the Y axis until the end of the word is found.
        """
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

<<<<<<< HEAD
    def play_horizontal_word(self, word: str, x_start, y_pos):
        """
        Iteratively call set_letter_position for each letter in a word that is being placed horizontally.

        <word> needs to be a string representing a word to play.
        <x_start> represents the X-axis position for the start of the word. This is where the first letter
                  will be placed. Letters will be successively placed starting at this position until the end of
                  the word is reached.
        <y_pos>   The y-axis value for the whole word (since this is a horizonal word, this value will not change)

        """
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

=======
>>>>>>> 0d15f7500ee4eb0a0540b8e685e017bba24e4254
    def get_board(self) -> list:
        """
        Return the matrix representing the board.
        """
        return self.grid

    def __str__(self) -> str:
        """
        Print the board as a 15x15 square, with each letter played represented.
        """
        return self.print_board(silent = True)

<<<<<<< HEAD
=======
#
# def test():
#     b = Board()
#     b.play_horizontal_word("FART", 7, 7)
#     b.play_vertical_word("FACT", 7, 7)
#
#     def inword(o):
#         if o is False:
#             print("Not in word")
#         else:
#             print(o)
#
#     inword(b.tile_in_horizontal_word(7, 7))
#     inword(b.tile_in_vertical_word(7, 7))
#     inword(b.tile_in_horizontal_word(5, 7))
#     inword(b.tile_in_vertical_word(5, 7))
#     inword(b.tile_in_horizontal_word(5, 8))
#     inword(b.tile_in_vertical_word(7, 8))
#     inword(b.tile_in_vertical_word(7, 9))
#     inword(b.tile_in_horizontal_word(7, 10))
#     inword(b.tile_in_vertical_word(10, 7))
>>>>>>> 0d15f7500ee4eb0a0540b8e685e017bba24e4254
