# a player class


class Player:
    def __init__(self, input_name="Default"):
        self.name = input_name

    def set_name(self, input_name):
        self.name = input_name

    def get_name(self):
        return self.name

    def is_illegal_move(self, arr, move):

        '''
        move is a tuple with 3 elements. (i, j, k)
        i -> board_no
        j -> row_no
        k -> col_no
        '''

        board_no = move[0]
        row_no = move[1]
        col_no = move[2]

        if (board_no < 0 or row_no < 0 or col_no < 0) or (
                    board_no >= len(arr) or row_no >= len(arr[0]) or col_no >= len(arr[0][0])):
            print ("Illegal Move!! Out of Bounds")
            return True
        else:
            if arr[board_no][row_no][col_no] != " ":
                print ("Illegal Move!! Place Already Filled!!!")
                return True
            return False


    def get_move(self, board):
        # board is used to get the state of the array for checking illegal move

        legal = False

        while not legal:
            inp_move = input(self.name + " please enter your move (board_no row_no col_no): ")
            l_moves = [int(s) for s in inp_move.split() if s.isdigit()]
            if len(l_moves) == 3:
                board_no = l_moves[0]
                row_no = l_moves[1]
                col_no = l_moves[2]
                if not self.is_illegal_move(board.get_arr(), (board_no, row_no, col_no)):
                    legal = True
                    return (board_no, row_no, col_no)
                else:
                    print("Wrong Format")


    def __str__(self):
        return self.name + "!"
