# Author: Deanna Denny Baumer
# Date: 11/17/2021
# Description: A program that stimulates the game HasamiShogiGame. Uses variant 1 rules.

class HasamiShogiGame:
    """A class to represent an abstract board game HasamiShogiGame."""

    def __init__(self):
        """The constructor for HasamiShogiGame class.
        Takes no parameters. Initializes the required data members.
        All data members are private."""
        # count for total captures based on color side
        self._black_pieces_captured = 0
        self._red_pieces_captured = 0
        # init game state to start as Unfinished
        self._game_state = 'UNFINISHED'
        # init active player to start first as Black
        self._active_player = 'BLACK'
        # init board game matrix
        self._game_board = [['.' for x in range(9)] for y in range(9)]
        self._game_board[0] = ["R" for _ in range(9)]
        self._game_board[8] = ["B" for _ in range(9)]
        # two piece colors (black 'B' or red 'R')
        self._piece_black = 'BLACK'
        self._piece_red = 'RED'

    def get_game_state(self):
        """Returns current game state used by the HasamiShogi Game Class
           to determine if Red Won, Black Won, or Game is Unfinished"""

        if self._black_pieces_captured > 8:
            self._game_state = 'RED_WON'
        elif self._red_pieces_captured > 8:
            self._game_state = 'BLACK_WON'
        else:
            self._game_state = 'UNFINISHED'

        return self._game_state

    def get_active_player(self):
        """Gets the current active player turn used by the HasamiShogi Game Class
         used to determine if its player Black or player’s Red turn"""
        return self._active_player

    def get_num_captured_pieces(self, active_player):
        """Takes one parameter player represents the number of pieces
        of that color (Red or Black) that have been captured."""
        if active_player == 'BLACK':
            return self._red_pieces_captured
        if active_player == 'RED':
            return self._black_pieces_captured

    def game_board(self):
        """Displays current boardS"""
        letter = ord("a")
        # print(" ", [str(i + 1) for i in (range(9))])
        for row in self._game_board:
            # print(chr(letter), row)
            letter += 1

    def coord_convert_alg(self, x, y):
        """Takes a row and column  value (x, y)
         and converts it to algebraic notation"""
        col_num = [str(index) for index in range(1, 9)]
        row_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        row = row_letter[x]
        col = col_num[y]
        alg_notation = row + col
        return alg_notation

    def alg_convert_coor(self, string_tuple):
        """Takes an algebraic notation position, and converts it to (x, y) form."""
        row_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        row = string_tuple[0]
        col = string_tuple[1]
        if row in row_letters:
            row_1 = row_letters.index(row)
        col_1 = int(col) - 1
        coord_positions = (row_1, col_1)
        return coord_positions

    def get_square_occupant(self, occupant):
        """It’s a method that takes one parameter occupant
         and returns current square occupant"""
        if type(occupant) == str:
            occupant = self.alg_convert_coor(occupant)
            # print("The occupant", occupant)
        if self._game_board[occupant[0]][occupant[1]] == 'R':
            # print("RED OCCUPANT")
            return self._piece_red
        elif self._game_board[occupant[0]][occupant[1]] == 'B':
            # print("BLACK OCCUPANT")
            return self._piece_black
        else:
            if occupant in self._game_board == '.':
                return None

    def make_move(self, from_pos, to_pos):
        """Takes two parameters: from_pos and to_pos.
        From position—coordinates where the pieces are moving from
        To position—coordinates of where the pieces are moving to
        In algebraic notation."""

        valid_move = self.valid_move_helper(from_pos, to_pos)

        # print(valid_move)
        # print(self.get_game_state())
        if valid_move is True and self.get_game_state() == 'UNFINISHED':
            # print('moving from ', from_pos, 'to ', to_pos)
            from_pos = self.alg_convert_coor(from_pos)
            to_pos = self.alg_convert_coor(to_pos)
            # print('moving from ', from_pos, 'to ', to_pos)
            self._game_board[to_pos[0]][to_pos[1]], self._game_board[from_pos[0]][from_pos[1]] = self._game_board[from_pos[0]][from_pos[1]], self._game_board[to_pos[0]][to_pos[1]]

            # self.capture_check(to_pos)

            if self._active_player == 'BLACK':
                self._active_player = 'RED'
            else:
                self._active_player = 'BLACK'

            return True

        else:
            return False

    def capture_check(self, attack_piece):
        """Checks and stores captures"""

        # print('attack location', attack_piece)
        row = attack_piece[0]
        col = attack_piece[1]

        # print("attack row", row)
        # print("attack col", col)

        # pieces_in_row = [x for x in self._game_board[row]]
        # index_in_row = [[row, col] for col in range(len(self._game_board[row]))]

        # index_in_column = [[row, col] for row in range(len(self._game_board))]
        # pieces_in_column = [x[col] for x in self._game_board]

        # creates list of lists containing row and column format with x,y,value
        row_occupants = [[row, x[0], x[1]] for x in enumerate(self._game_board[row])]
        # col_occupants = [[x[0], col, x[1][col]] for x in enumerate(self._game_board)]

        # print(pieces_in_row)
        # print(index_in_row)

        # print(pieces_in_column)
        # print(index_in_column)

        # print(row_occupants)
        # print(col_occupants)

        # list for comparing pieces for while loops
        compare_list = [self.get_active_player(), None]

        # print("attacker is", self.get_active_player())
        # print("attacker row index is ", col)

        capture = []

        # check left
        col = attack_piece[1] - 1
        square = self.get_square_occupant(row_occupants[col])
        # print("value check", row_occupants[col])

        while square not in compare_list and col in range(1, 10):
            # print("index number is: ", col)
            # print('checking', row_occupants[col])
            square = self.get_square_occupant(row_occupants[col])
            if square not in compare_list:
                capture.append((row_occupants[col]))
            col -= 1

        # check down
        row = attack_piece[0] - 1
        square = self.get_square_occupant(row_occupants[row])
        while square not in compare_list and row in range(1, 10):
            # print("index number is: ", col)
            # print('checking', row_occupants[col])
            square = self.get_square_occupant(row_occupants[row])
            if square not in compare_list:
                capture.append((row_occupants[row]))
            row -= 1

        # check up
        row = attack_piece[0] + 1
        square = self.get_square_occupant(row_occupants[row])
        while square not in compare_list and row in range(0, 8):
            # print("index number is: ", col)
            # print('checking', row_occupants[col])
            square = self.get_square_occupant(row_occupants[row])
            if square not in compare_list:
                capture.append((row_occupants[row]))
            row += 1

        # check right
        index = attack_piece[1] + 1
        next_piece = self.get_square_occupant(row_occupants[index])

        # print('right of attack piece is:', row_occupants[index], 'with a value of: ', self.get_square_occupant(row_occupants[index]))
        # print("value check", row_occupants[index])

        while next_piece not in compare_list and index < 8:
            # print("index number is: ", index)
            # print('checking', row_occupants[index])
            if self.get_square_occupant(row_occupants[index + 1]) not in compare_list and self.get_square_occupant(row_occupants[index + 2]) in compare_list:
                capture.append(row_occupants[index])
            index += 1
            next_piece = self.get_square_occupant(row_occupants[index])

        # print(capture)

        self.piece_remover(capture)

    def piece_remover(self, capture_valid):
        """Removes pieces once captured"""
        for pieces in capture_valid:
            cap_row = pieces[0]
            cap_col = pieces[1]
            # print('to be removed row: ', cap_row, 'col: ', cap_col)
            if self.get_square_occupant((cap_row, cap_col)) == 'BLACK':
                self._black_pieces_captured += 1
            elif self.get_square_occupant((cap_row, cap_col)) == 'RED':
                self._red_pieces_captured += 1
            self._game_board[cap_row][cap_col] = '.'

    def valid_move_helper(self, from_pos, to_pos):
        """Helps make_move function with validation of moves"""

        if self.get_square_occupant(from_pos) == self.get_active_player():

            from_pos = self.alg_convert_coor(from_pos)
            to_pos = self.alg_convert_coor(to_pos)

            from_row = from_pos[0]
            from_col = from_pos[1]

            to_row = to_pos[0]
            to_col = to_pos[1]
            direction = None

            # print(from_row, from_col)
            # print(to_row, to_col)

            # check of move is along x-axis or y axis or returns false if its not valid
            if from_row == to_row:
                direction = 'horizontal'
            elif from_col == to_col:
                direction = 'vertical'
            else:
                return False

            # print(direction)

            path = ()

            # verify path of movement is empty
            if direction == 'vertical':
                if from_row < to_row:
                    start = from_pos[0] + 1
                    end = to_pos[0] + 1
                else:
                    start = to_pos[0]
                    end = from_pos[0]
                path = [[row, from_pos[1]] for row in range(start, end)]
            elif direction == 'horizontal':
                if from_col < to_col:
                    start = from_pos[1] + 1
                    end = to_pos[1] + 1
                else:
                    start = to_pos[1]
                    end = from_pos[1]
                path = [[from_pos[0], col] for col in range(start, end)]

            # print(path)

            occupant_list = []

            for item in path:
                value = self.get_square_occupant(item)
                occupant_list.append(value)

            return all(value is None for value in occupant_list)

# test code
# game = HasamiShogiGame()
# print(game.get_game_state())
# print(game.get_active_player())
# print(game.get_square_occupant("i1"))
# print(game.get_square_occupant([0,1]))
# print(game.make_move('a1`', 'a3'))
# print(game.make_move('i1', 'g1'))
# print(game.make_move('i1', 'i5'))
# print(game.alg_convert_coor('g1'))
# print('test', game.coord_convert_alg(6,0))
# print(game.get_square_occupant([6,0]))
# print(game.get_square_occupant('g1'))

# left remove test ------------------------------
# print(game.get_active_player())
# game.make_move('i1', 'd1')
# game.game_board()
# print(game.get_active_player())
# game.make_move('a2', 'd2')
# game.game_board()
# print(game.get_active_player())
# game.make_move('i7', 'd7')
# game.game_board()
# print(game.get_active_player())
# game.make_move('a3', 'd3')
# game.game_board()
# print(game.get_active_player())
# game.make_move('i4', 'd4')
# game.game_board()

# left test 2
# print(game.get_active_player())
# game.make_move('i1', 'd1')
# game.game_board()
# print(game.get_active_player())
# game.make_move('a2', 'd2')
# game.game_board()
# print(game.get_active_player())
# game.make_move('i3', 'd3')
# game.game_board()


# right remove test
# print(game.get_active_player())
# game.make_move('i1', 'd1')
# game.game_board()
# print(game.get_active_player())
# game.make_move('a5', 'd5')
# game.game_board()
# print(game.get_active_player())
# game.make_move('i4', 'd4')
# game.game_board()
# print(game.get_active_player())
# game.make_move('a3', 'd3')
# game.game_board()
# print(game.get_active_player())
# game.make_move('a9', 'd9')
# game.game_board()
# print(game.get_active_player())
# game.make_move('i3', 'd3')
# game.game_board()
# print(game.get_active_player())
# game.make_move('a2', 'd2')
# game.game_board()
