import random
import time


class Bot:
    def __init__(self, name="Default Computer Bot"):
        self.name = name

    def set_name(self, input_name):
        self.name = input_name

    def get_name(self):
        return self.name

    '''def attacking(self, board, inp_choice):
        choice = board.get_choice((inp_choice)%2)
        arr = board.get_arr()
        # check diagonally
        diag_1 = []
        diag_2 = []
        for i in range(len(arr)):
            diag_1.append(arr[i][i])
            diag_2.append(arr[i][len(arr) - 1 - i])

        diag_1_count = 0
        diag_2_count = 0

        for i in range(len(diag_1)):
            if diag_1[i] == choice:
                diag_1_count += 1

        if diag_1_count == 2:
            for i in range(len(diag_1)):
                if diag_1[i] == " ":
                    return (i, i)

        for i in range(len(diag_2)):
            if diag_2[i] == choice:
                diag_2_count += 1

        if diag_2_count == 2:
            for i in range(len(diag_2)):
                if diag_2[i] == " ":
                    return (i, len(arr) - 1 - i)


        for i in range(len(arr)):
            hor_count = 0
            ver_count = 0
            for j in range(len(arr[i])):
                if arr[i][j] == choice:
                    hor_count += 1
                if arr[j][i] == choice:
                    ver_count += 1
            if hor_count == 2:
                for j in range(len(arr[i])):
                    if arr[i][j] == " ":
                        return (i, j)
            elif ver_count == 2:
                for j in range(len(arr[i])):
                    if arr[j][i] == " ":
                        return (j, i)

        return (len(arr), len(arr))


    def defensive(self, board, inp_choice):
        choice = board.get_choice((inp_choice-1)%2)
        arr = board.get_arr()
        # check diagonally
        diag_1 = []
        diag_2 = []
        for i in range(len(arr)):
            diag_1.append(arr[i][i])
            diag_2.append(arr[i][len(arr) - 1 - i])

        diag_1_count = 0
        diag_2_count = 0

        for i in range(len(diag_1)):
            if diag_1[i] == choice:
                diag_1_count += 1

        if diag_1_count == 2:
            for i in range(len(diag_1)):
                if diag_1[i] == " ":
                    return (i, i)

        for i in range(len(diag_2)):
            if diag_2[i] == choice:
                diag_2_count += 1

        if diag_2_count == 2:
            for i in range(len(diag_2)):
                if diag_2[i] == " ":
                    return (i, len(arr) - 1 - i)


        for i in range(len(arr)):
            hor_count = 0
            ver_count = 0
            for j in range(len(arr[i])):
                if arr[i][j] == choice:
                    hor_count += 1
                if arr[j][i] == choice:
                    ver_count += 1
            if hor_count == 2:
                for j in range(len(arr[i])):
                    if arr[i][j] == " ":
                        return (i, j)
            elif ver_count == 2:
                for j in range(len(arr[i])):
                    if arr[j][i] == " ":
                        return (j, i)

        return (len(arr), len(arr))

    def strategy(self, board, inp_choice):
        choice = board.get_choice(inp_choice)
        arr = board.get_arr()
        if arr[(len(arr) - 1)//2][(len(arr[0]) - 1)//2] == " ":
            return ((len(arr) - 1)//2, (len(arr[0]) - 1)//2)

        elif (arr[0][0] == choice and arr[len(arr)-1][len(arr)-1] == choice) or (arr[0][len(arr)-1] == choice and arr[len(arr)-1][0] == choice):
            help_arr = [(1, 0), (0, 1), (1, 2), (2, 1)]
            legal = False
            while not legal:
                ret_move = help_arr[random.randint(0, 3)]
                if arr[ret_move[0]][ret_move[1]] == " ":
                    return ret_move

        elif arr[0][0] != " " and arr[0][len(arr[0])-1] != " " and arr[len(arr)-1][0] != " " and arr[len(arr)-1][len(arr[0])-1] != " ":
            help_arr = [(1, 0), (0, 1), (1, 2), (2, 1)]
            legal = False
            while not legal:
                ret_move = help_arr[random.randint(0, 3)]
                if arr[ret_move[0]][ret_move[1]] == " ":
                    return ret_move
        else:
            help_arr = []
            if arr[0][0] == " ":
                help_arr.append((0, 0))
            if arr[0][len(arr)-1] == " ":
                help_arr.append((0, len(arr)-1))
            if arr[len(arr)-1][0] == " ":
                help_arr.append((len(arr)-1, 0))
            if arr[len(arr)-1][len(arr)-1] == " ":
                help_arr.append((len(arr)-1, len(arr)-1))
            ret_move = help_arr[random.randint(0, len(help_arr)-1)]
            return ret_move


    def is_illegal_move(self, arr, move, inp_choice):
        choice = board.get_choice((inp_choice) % 2)
        i = move[0]
        j = move[1]
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            print ("Illegal Move!! Out of Bounds")
            return True
        else:
            if arr[i][j] == " " or arr[i][j] == choice:
                return False
            else:
                print ("Illegal Move!! Cannot Move here")
                return True'''


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
        arr = board.get_arr()

        legal = False

        self.pass_time(3)
        while not legal:
            bot_move = (int(random.random()*len(arr)), int(random.random()*len(arr)), int(random.random()*len(arr)))
            if not self.is_illegal_move(board.get_arr(), bot_move):
                legal = True
                return bot_move


    # a simple function to display that the bot is thinking while passing time.
    def pass_time(self, time_in_sec):
        print ("Bot is thinking its next move! ")
        for i in range(time_in_sec):
            start = time.time()
            while time.time() - start < 1:
                a = 1
            print (".", " ")


    def __str__(self):
        return self.name + "!"
