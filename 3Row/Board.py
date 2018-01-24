# a board is defined as a 3X3 array with each spot being a string (" ", "O", "X")


class TraditionalBoard:
    def __init__(self):
        self.arr = [[" " for i in range(3)] for i in range(3)]
        self.choice = ["X", "O"]
        self.helper = [[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]
        self.all_x = ["X" for i in range(3)]
        self.all_o = ["O" for i in range(3)]

    def get_arr(self):
        return self.arr

    def get_choice(self, num):
        return self.choice[num%2]

    def check_out_of_bounds(self, move):
        #print (move)
        i = move[0]
        j = move[1]
        if i < 0 or j < 0 or i >= len(self.arr) or j >= len(self.arr[0]):
            #print ("Illegal Move!! Out of Bounds")
            return True
        else:
            return False

    def reset_board(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                self.arr[i][j] = " "

    def update_board(self, moves, choice):
        for i in range(len(moves)):
            if not self.check_out_of_bounds(moves[i]):
                self.arr[moves[i][0]][moves[i][1]] = self.choice[choice%2]

    def check_win(self, move):
        i = move[0]
        j = move[1]
        if len(self.arr) - 1 == i + j or i == j:
            diag1 = []
            diag2 = []
            for k in range(len(self.arr)):
                diag1.append(self.arr[k][k])
                diag2.append(self.arr[k][len(self.arr) - 1 - k])
            if diag1 == self.all_x or diag1 == self.all_o:
                return True
            elif diag2 == self.all_x or diag2 == self.all_o:
                return True
        # check_vertically
        ver = []
        for k in self.helper[i]:
            ver.append(self.arr[i + k][j])
        if ver == self.all_x or ver == self.all_o:
            return True
        # check_horizontally
        hor = []
        for k in self.helper[j]:
            hor.append(self.arr[i][j + k])
        if hor == self.all_x or hor == self.all_o:
            return True
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