import random
import time


class Bot:
    def __init__(self, name="Default Computer Bot"):
        self.name = name
        self.moves = [(200, 200), (200, 200), (200, 200)]
        self.counter = 0

    def set_name(self, input_name):
        self.name = input_name

    def get_name(self):
        return self.name

    def get_moves(self):
        return self.moves

    def attacking(self, board, inp_choice):
        choice = board.get_choice((inp_choice)%2)
        arr = board.get_arr()
        done_moves = [self.moves[i] for i in range(len(self.moves)) if i != self.counter and self.moves[i] != (200, 200)]

        # check diagonally
        diag_1 = [done_moves[i] for i in range(len(done_moves)) if done_moves[i][0] == done_moves[i][1]]
        diag_2 = [done_moves[i] for i in range(len(done_moves)) if done_moves[i][0] + done_moves[i][1] == len(arr) - 1]

        diag_1_count = len(diag_1)
        diag_2_count = len(diag_2)

        if diag_1_count == 2:
            for move in [(i, i) for i in range(len(arr))]:
                if move not in diag_1 and arr[move[0]][move[1]] == " ":
                    self.moves[self.counter%3] = move
                    return True

        if diag_2_count == 2:
            for move in [(i, len(arr) - 1 - i) for i in range(len(arr))]:
                if move not in diag_2 and arr[move[0]][move[1]] == " ":
                    self.moves[self.counter%3] = move
                    return True

        for i in range(len(arr)):
            #vertical
            if len(done_moves) > 1 and done_moves[0][1] == done_moves[1][1] and arr[len(arr) - (done_moves[0][0] + done_moves[1][0])][done_moves[0][1]] == " ":
                self.moves[self.counter%3] = (len(arr) - (done_moves[0][0] + done_moves[1][0]), done_moves[0][1])
                return True

            #horizontal
            elif len(done_moves) > 1 and done_moves[0][0] == done_moves[1][0] and arr[done_moves[0][0]][len(arr) - (done_moves[0][1] + done_moves[1][1])] == " ":
                self.moves[self.counter%3] = (done_moves[0][0], len(arr) - (done_moves[0][1] + done_moves[1][1]))
                return True

        return False


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
                    self.moves[self.counter%3] = (i, i)
                    return True

        for i in range(len(diag_2)):
            if diag_2[i] == choice:
                diag_2_count += 1

        if diag_2_count == 2:
            for i in range(len(diag_2)):
                if diag_2[i] == " ":
                    self.moves[self.counter%3] = (i, len(arr) - 1 - i)
                    return True


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
                        self.moves[self.counter%3] = (i, j)
                        return True

            elif ver_count == 2:
                for j in range(len(arr[i])):
                    if arr[j][i] == " ":
                        self.moves[self.counter%3] = (j, i)
                        return True

        return False

    def strategy(self, board, inp_choice):
        choice = board.get_choice(inp_choice-1)
        arr = board.get_arr()
        if arr[(len(arr) - 1)//2][(len(arr[0]) - 1)//2] == " ":
            self.moves[self.counter%3] = ((len(arr) - 1)//2, (len(arr[0]) - 1)//2)
            return True

        elif (arr[0][0] == choice and arr[len(arr)-1][len(arr)-1] == choice) or (arr[0][len(arr)-1] == choice and arr[len(arr)-1][0] == choice):
            help_arr = [(1, 0), (0, 1), (1, 2), (2, 1)]
            legal = False
            while not legal:
                ret_move = help_arr[random.randint(0, 3)]
                if arr[ret_move[0]][ret_move[1]] == " ":
                    print(ret_move)
                    self.moves[self.counter%3] = ret_move
                    return True

        elif arr[0][0] != " " and arr[0][len(arr[0])-1] != " " and arr[len(arr)-1][0] != " " and arr[len(arr)-1][len(arr[0])-1] != " ":
            help_arr = [(1, 0), (0, 1), (1, 2), (2, 1)]
            legal = False
            while not legal:
                ret_move = help_arr[random.randint(0, 3)]
                if arr[ret_move[0]][ret_move[1]] == " ":
                    self.moves[self.counter%3] = ret_move
                    print(ret_move)
                    return True
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
            print(ret_move)
            self.moves[self.counter%3] = ret_move
            return True

    def is_illegal_move(self, arr, move, inp_choice):
        i = move[0]
        j = move[1]
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            print ("Illegal Move!! Out of Bounds")
            return True
        else:
            if i == self.moves[self.counter][0] and j == self.moves[self.counter][1]:
                #When the move is the same place as the original move but not at any of the places already in use.
                print ("Cannot use the same move again!")
                return True
            elif arr[i][j] != " ":
                print ("Illegal Move!! Cannot Move here")
                return True
            else:
                return False

    def pass_time(self, time_in_sec):
        print ("Bot is thinking its next move! ")
        for i in range(time_in_sec):
            start = time.time()
            while time.time() - start < 1:
                a = 1
            print (".", " ")

    def update_moves(self, board, inp_choice):
        # board is used to get the state of the array for checking illegal move
        # inp_choice is the choice for the player itself. It is a number and needs to use the board.get_choice() function
        if self.attacking(board, inp_choice):
            self.pass_time(2)
            self.counter += 1
            self.counter = self.counter % 3
            return self.moves[(self.counter-1)%3]

        elif self.defensive(board, inp_choice):
            self.pass_time(2)
            self.counter += 1
            self.counter = self.counter % 3
            return self.moves[(self.counter-1)%3]

        else:
            self.pass_time(3)
            self.strategy(board, inp_choice)
            self.counter += 1
            self.counter = self.counter % 3
            return self.moves[(self.counter-1)%3]

    def __str__(self):
        return self.name + "!"
