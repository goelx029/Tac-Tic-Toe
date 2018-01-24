# a board is defined as a 3X3 array with each spot being a string (" ", "O", "X")


class threeDimensionalBoard:
    def __init__(self, num_len = 4):
        self.arr = [[[" " for i in range(num_len)] for i in range(num_len)] for i in range(num_len)]
        self.len = num_len
        self.choice = ["X", "O"]
        self.helper = [[0, 1, 2, 3], [-1, 0, 1, 2], [-2, -1, 0, 1], [-3, -2, -1, 0]]
        self.all_x = ["X" for i in range(self.len)]
        self.all_o = ["O" for i in range(self.len)]

    def get_arr(self):
        return self.arr

    def get_choice(self, num):
        return self.choice[num%2]

    def is_illegal_move(self, move):

        '''
        move is a tuple with 3 elements. (i, j, k)
        i -> board_no
        j -> row_no
        k -> col_no
        '''

        board_no = move[0]
        row_no = move[1]
        col_no = move[2]

        if (board_no < 0 or row_no < 0 or col_no < 0) or (board_no >= self.len or row_no >= self.len or col_no >= self.len):
            print ("Illegal Move!! Out of Bounds")
            return True
        else:
            if self.arr[board_no][row_no][col_no] != " ":
                print ("Illegal Move!! Place Already Filled!!!")
                return True
            return False

    def reset_board(self):
        for i in range(self.len):
            for j in range(self.len):
                for k in range(self.len):
                    self.arr[i][j] = " "

    def add_move(self, move, choice):
        self.arr[move[0]][move[1]][move[2]] = self.choice[choice%2]
        return True

    def check_win_2d(self, move, arr):

        '''
        move is a tuple with 3 elements. (i, j, k)
        i -> board_no
        j -> row_no
        k -> col_no
        '''

        i = move[1]
        j = move[2]

        if len(arr) - 1 == i + j or i == j:
            diag1 = []
            diag2 = []
            for k in range(len(arr)):
                diag1.append(arr[k][k])
                diag2.append(arr[k][len(arr) - 1 - k])
            if diag1 == self.all_x or diag1 == self.all_o:
                return True
            elif diag2 == self.all_x or diag2 == self.all_o:
                return True
        # check_vertically
        ver = []
        for k in self.helper[i]:
            ver.append(arr[i + k][j])
        if ver == self.all_x or ver == self.all_o:
            return True
        # check_horizontally
        hor = []
        for k in self.helper[j]:
            hor.append(arr[i][j + k])
        if hor == self.all_x or hor == self.all_o:
            return True
        return False


    def check_on_cubic_diag(self, move):
        if move[0] == move[1] and move[0] == move[2]:
            return 0
        elif move[0] == move[1] and move[1] + move[2] == self.len - 1:
            return 1
        elif move[0] == move[2] and move[1] + move[2] == self.len - 1:
            return 2
        elif move[1] == move[2] and move[0] + move[1] == self.len - 1:
            return 3
        else:
            return 4

    def check_cubic_diag(self, flag):
        if flag == 0:
            diag1 = []
            for k in range(self.len):
                diag1.append(self.arr[k][k][k])
            if diag1 == self.all_x or diag1 == self.all_o:
                return True
        elif flag == 1:
            diag2 = []
            for k in range(self.len):
                diag2.append(self.arr[k][k][self.len - 1 - k])
            if diag2 == self.all_x or diag2 == self.all_o:
                return True
        elif flag == 2:
            diag3 = []
            for k in range(self.len):
                diag3.append(self.arr[k][self.len - 1 - k][k])
            if diag3 == self.all_x or diag3 == self.all_o:
                return True
        elif flag == 3:
            diag4 = []
            for k in range(self.len):
                diag4.append(self.arr[self.len - 1 - k][k][k])
            if diag4 == self.all_x or diag4 == self.all_o:
                return True
        return False

    def check_vertical(self, move):
        arr = self.helper[move[0]]
        ver = []
        for k in arr:
            ver.append(self.arr[move[0]+k][move[1]][move[2]])
        return (ver == self.all_o or ver == self.all_x)


    def in_plane_diagonals(self, move):
        if move[0] == 0 or move[0] == self.len - 1:
            return not (move[1] in [1, 2] and move[2] in [1, 2])
        elif move[0] == 1 or move[0] == 2:
            return not (move[1] in [0, self.len - 1] and move[2] in [0, self.len - 1])
        return False


    def check_plane_diagonals(self, move):
        if self.in_plane_diagonals(move):
            #check sidewards plane
            for i in range(self.len):
                diag1 = []
                diag2 = []
                for j in range(self.len):
                    diag1.append(self.arr[j][i][j])
                    diag2.append(self.arr[j][i][self.len - 1 - j])
                if diag1 == self.all_x or diag1 == self.all_o or diag2 == self.all_x or diag2 == self.all_o:
                    return True

            # check incoming plane
            for i in range(self.len):
                diag1 = []
                diag2 = []
                for j in range(self.len):
                    diag1.append(self.arr[j][j][i])
                    diag2.append(self.arr[j][self.len - 1 - j][i])
                if diag1 == self.all_x or diag1 == self.all_o or diag2 == self.all_x or diag2 == self.all_o:
                    return True

            return False

        else:
            return False


    def check_win(self, move):
        '''
        move is a tuple with 3 elements. (i, j, k)
        i -> board_no
        j -> row_no
        k -> col_no
        '''

        board_no = move[0]

        if self.check_win_2d(move, self.arr[board_no]):
            # covers 40 cases
            return True

        elif self.check_cubic_diag(self.check_on_cubic_diag(move)):
            # coves 4 cases
            return True

        elif self.check_vertical(move):
            # covers 16 cases
            return True

        elif self.check_plane_diagonals(move):
            #covers 16 cases
            return True
        return False


    def get_str_board(self, ind):
        retstr = "\n"
        for i in range(len(self.arr[ind])):
            for j in range(len(self.arr[ind][i])):
                retstr += " " + self.arr[ind][i][j] + " |"
            retstr = retstr[:-2]
            retstr += "\n---------------\n"
        retstr = retstr[:-16]
        return retstr

    def __str__(self):
        retstr = "\n"
        for i in range(len(self.arr)):
            retstr += self.get_str_board(i)
        return retstr