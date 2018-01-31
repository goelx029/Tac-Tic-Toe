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



    def attacking(self, u_board, board, inp_choice):
        choice = u_board.get_choice((inp_choice)%2)
        arr = board.get_arr()

        # check diagonally
        diag_1 = [arr[i][i] for i in range(len(arr))]
        diag_2 = [arr[i][len(arr) - 1 - i] for i in range(len(arr))]

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


    def defensive(self, u_board, board, inp_choice):
        choice = u_board.get_choice((inp_choice-1)%2)
        arr = board.get_arr()


        # check diagonally
        diag_1 = [arr[i][i] for i in range(len(arr))]
        diag_2 = [arr[i][len(arr) - 1 - i] for i in range(len(arr))]

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


    def strategy(self, u_board, board, inp_choice):
        choice = u_board.get_choice(inp_choice)
        user_choice = u_board.get_choice(inp_choice-1)
        arr = board.get_arr()
        super_arr = u_board.get_arr()

        succ_d = {(i, j): self.get_succ_rate(super_arr[i][j].get_arr(), choice, user_choice) for i in range(len(arr)) for j in range(len(arr[i])) if arr[i][j] == " "}

        return list(succ_d.keys())[list(succ_d.values()).index(max(succ_d.values()))]

    def strategy_ultimate(self, u_board, inp_choice):
        choice = u_board.get_choice(inp_choice)
        user_choice = u_board.get_choice(inp_choice-1)
        super_arr = u_board.get_arr()
        succ_d = {(i, j): self.get_succ_rate(super_arr[i][j].get_arr(), choice, user_choice) for i in range(len(super_arr)) for j in range(len(super_arr[i])) if super_arr[i][j].get_status() == " "}

        return list(succ_d.keys())[list(succ_d.values()).index(max(succ_d.values()))]

    def get_succ_rate(self, arr, bot_choice, user_choice):
        bot_choice_freq = 0
        user_choice_freq = 0

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == bot_choice:
                    bot_choice_freq += 1
                elif arr[i][j] == user_choice:
                    user_choice_freq += 1

        return (bot_choice_freq - user_choice_freq)

    def get_move(self, board, prev_move, inp_choice):
        if not prev_move[:2] == (200, 200):
            self.pass_time(5)
        if prev_move[2:4] == (200, 200):
            return self.get_move(board, (200, 200)+self.strategy_ultimate(board, inp_choice), inp_choice)
        else:
            '''first get the attack and defense. If they dont work then in strategy think about the place you want the player to go to'''
            arr = board.get_arr()

            attack = self.attacking(board, arr[prev_move[2]][prev_move[3]], inp_choice)
            if attack != (len(arr), len(arr)):
                return (prev_move[2], prev_move[3]) + attack

            defense = self.defensive(board, arr[prev_move[2]][prev_move[3]], inp_choice)
            if defense != (len(arr), len(arr)):
                return (prev_move[2], prev_move[3]) + defense

            return (prev_move[2], prev_move[3]) + self.strategy(board, arr[prev_move[2]][prev_move[3]], inp_choice)

    # a simple function to display that the bot is thinking while passing time.
    def pass_time(self, time_in_sec):
        print ("Bot is thinking its next move! ")
        for i in range(time_in_sec):
            start = time.time()
            while time.time() - start < 1:
                a = 1
            print (".")


    def __str__(self):
        return self.name + "!"
