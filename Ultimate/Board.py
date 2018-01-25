# a board is defined as a 3X3 array with each spot being a string (" ", "O", "X")


class simpleBoard:
    def __init__(self):
        self.arr = [[" " for i in range(3)] for i in range(3)]
        self.helper = [[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]
        self.all_x = ["X" for i in range(3)]
        self.all_o = ["O" for i in range(3)]
        #board_status is in [" ". "X", "O", "XO"]
        self.board_status = " "
        self.counter = 0

    def get_arr(self):
        return self.arr

    def get_status(self):
        return self.board_status

    def is_illegal_move(self, arr, move):
        i = move[0]
        j = move[1]
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            #print ("Illegal Move!! Out of Bounds")
            return True
        else:
            if arr[i][j] != " ":
                #print ("Illegal Move!! Cannot Move here")
                return True
            else:
                return False

    def reset_board(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                self.arr[i][j] = " "

    def add_move(self, move, choice):
        if not self.is_illegal_move(self.arr, move):
            self.counter += 1
            self.arr[move[0]][move[1]] = choice
            if self.counter >= 3:
                self.update_status(move, choice)
            return True
        return False


    def update_status(self, move, choice):
        i = move[0]
        j = move[1]
        if len(self.arr) - 1 == i + j or i == j:
            diag1 = []
            diag2 = []
            for k in range(len(self.arr)):
                diag1.append(self.arr[k][k])
                diag2.append(self.arr[k][len(self.arr) - 1 - k])
            if diag1 == self.all_x or diag1 == self.all_o:
                self.board_status = choice
                return True
            elif diag2 == self.all_x or diag2 == self.all_o:
                self.board_status = choice
                return True
        # check_vertically
        ver = []
        for k in self.helper[i]:
            ver.append(self.arr[i + k][j])
        if ver == self.all_x or ver == self.all_o:
            self.board_status = choice
            return True
        # check_horizontally
        hor = []
        for k in self.helper[j]:
            hor.append(self.arr[i][j + k])
        if hor == self.all_x or hor == self.all_o:
            self.board_status = choice
            return True

        if self.counter == 9:
            self.board_status = "XO"

        return False

    def __str__(self):
        retstr = "\n"
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                retstr += " " + self.arr[i][j] + " |"
            retstr = retstr[:-2]
            retstr += "\n-----------\n"
        retstr = retstr[:-12]
        return retstr

    def get_row_str(self, row_no):
        retstr = ""
        for j in range(len(self.arr[row_no])):
            retstr += " " + self.arr[row_no][j] + " |"
        retstr = retstr[:-2]
        return retstr


class ultimateBoard:
    def __init__(self):
        self.arr = [[simpleBoard() for i in range(3)] for i in range(3)]
        self.choice = ["X", "O"]
        self.helper = [[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]
        self.all_x = ["X" for i in range(3)]
        self.all_o = ["O" for i in range(3)]

    def get_arr(self):
        return self.arr

    def get_choice(self, choice_no):
        return self.choice[choice_no%2]

    def is_illegal_move(self, arr, move):
        i = move[0]
        j = move[1]
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            print ("Illegal Move!! Out of Bounds")
            return True
        else:
            if arr[i][j].get_status() != " ":
                print ("Illegal Move!! Cannot Move here")
                return True
            else:
                return False

    def reset_board(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                self.arr[i][j] = simpleBoard()

    def add_move(self, move, choice_no):
        #move should be a tuple/list of len 4 with u_i, u_j, s_i, s_j
        u_i = move[0]
        u_j = move[1]
        s_i = move[2]
        s_j = move[3]
        if not self.is_illegal_move(self.arr, (u_i, u_j)):
            if self.arr[u_i][u_j].add_move((s_i, s_j), self.get_choice(choice_no)):
                return True
        return False


    def check_win(self, move):
        # move should be a tuple/list of len 4 with u_i, u_j, s_i, s_j
        i = move[0]
        j = move[1]
        if len(self.arr) - 1 == i + j or i == j:
            diag1 = []
            diag2 = []
            for k in range(len(self.arr)):
                diag1.append(self.arr[k][k].get_status())
                diag2.append(self.arr[k][len(self.arr) - 1 - k].get_status())
            if diag1 == self.all_x or diag1 == self.all_o:
                return True
            elif diag2 == self.all_x or diag2 == self.all_o:
                return True
        # check_vertically
        ver = []
        for k in self.helper[i]:
            ver.append(self.arr[i + k][j].get_status())
        if ver == self.all_x or ver == self.all_o:
            return True
        # check_horizontally
        hor = []
        for k in self.helper[j]:
            hor.append(self.arr[i][j + k].get_status())
        if hor == self.all_x or hor == self.all_o:
            return True
        return False


    def __str__(self):
        retstr = ""
        for i in range(len(self.arr)):
            for k in range(len(self.arr[i][0].get_arr())):
                for j in range(len(self.arr[i])):
                    retstr = retstr + self.arr[i][j].get_row_str(k) + "  || "
                retstr = retstr[:-5]
                retstr += "\n----------- || ----------- || -----------\n"
            retstr = retstr[:-43]
            retstr += "\n\n-----------------------------------------\n\n"
        return retstr[:-44]