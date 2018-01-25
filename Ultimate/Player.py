# a player class


class Player:
    def __init__(self, input_name="Default"):
        self.name = input_name

    def set_name(self, input_name):
        self.name = input_name

    def get_name(self):
        return self.name

    def is_illegal_move(self, arr, move):
        i = move[0]
        j = move[1]
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            print ("Illegal Move!! Out of Bounds")
            return True
        else:
            if arr[i][j] != " ":
                print ("Illegal Move!! Cannot Move here. This place is already occupied!")
                return True
            else:
                return False

    def is_illegal_move_ultimate(self, arr, move):
        i = move[0]
        j = move[1]
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            print ("Illegal Move!! Out of Bounds")
            return True
        else:
            if arr[i][j].get_status() != " ":
                print ("Illegal Move!! The Board in the section specified already is completed")
                return True
            else:
                return False


    def get_move(self, board, prev_move, inp_choice):
        while True:
            if prev_move[2:4] == (200, 200):
                inp_move = input(self.get_name() + " please enter your move (super_row super_col inner_row inner_col): ")
                l_moves = [int(s) for s in inp_move.split() if s.isdigit()]
                if len(l_moves) == 4:
                    super_row = l_moves[0]
                    super_col = l_moves[1]
                    inner_row = l_moves[2]
                    inner_col = l_moves[3]
                    recent_move = (super_row, super_col, inner_row, inner_col)
                    if not self.is_illegal_move_ultimate(board.get_arr(), recent_move[:-2]):
                        if board.get_arr()[super_row][super_col].get_status() == " " and not self.is_illegal_move(board.get_arr()[super_row][super_col].get_arr(), recent_move[2:4]):
                            return recent_move
            else:
                print ("Using previous move your SuperRow = " + str(prev_move[2]) + " SuperCol = " + str(prev_move[3]))
                inp_move = input(self.get_name() + "please enter your move (inner_row inner_col): ")
                l_moves = [int(s) for s in inp_move.split() if s.isdigit()]
                if len(l_moves) == 2:
                    inner_row = l_moves[0]
                    inner_col = l_moves[1]
                    recent_move = (prev_move[2], prev_move[3], inner_row, inner_col)
                    if not self.is_illegal_move(board.get_arr()[prev_move[2]][prev_move[3]].get_arr(), recent_move[2:4]):
                            return recent_move

    def __str__(self):
        return self.name + "!"
