import random
import time


# Bot class - Implements the functionality of a Computer Bot.
# This class includes all the functions required for the bot to play a move on the board


class Bot:
    def __init__(self, name="Default Computer Bot"):
        self.name = name
        self.helper = [[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]

    # setters and getters for the member variables
    def set_name(self, input_name):
        self.name = input_name

    def get_name(self):
        return self.name

    #function that returns a move based on possibility of winning in the next turn
    def attacking(self, board, inp_choice):
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


    # function that returns a move to stop the user from winning in their next turn
    def defensive(self, board, inp_choice):
        choice = board.get_choice(inp_choice)
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


    # function that implements a strategy behavior for a move on the tic-tac-toe board
    # Is more of like a heuristic method based on different types of strategies used.
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


    # a simple function to display that the bot is thinking while passing time.
    def pass_time(self, time_in_sec):
        print ("Bot is thinking its next move! ")
        for i in range(time_in_sec):
            start = time.time()
            while time.time() - start < 1:
                a = 1
            print (".", " ")


    # get_move function checks whether it should attack, defend, or just use plain strategy for its next move
    def get_move(self, board, inp_choice):
        arr = board.get_arr()

        attack = self.attacking(board, inp_choice)
        if attack != (len(arr), len(arr)):
            self.pass_time(3)
            return attack

        defense = self.defensive(board, inp_choice)
        if defense != (len(arr), len(arr)):
            self.pass_time(3)
            return defense

        self.pass_time(5)
        return self.strategy(board, inp_choice)

    def __str__(self):
        return self.name + "!"
