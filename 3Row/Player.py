# a player class


class Player:
    def __init__(self, input_name="Default"):
        self.name = input_name
        self.moves = [(200, 200), (200, 200), (200, 200)]
        self.counter = 0

    def set_name(self, input_name):
        self.name = input_name

    def get_name(self):
        return self.name

    def get_moves(self):
        return self.moves

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

    def update_moves(self, board, inp_choice):
        # board is used to get the state of the array for checking illegal move
        # inp_choice is the choice for the player itself. It is a number and needs to use the board.get_choice() function
        legal = False
        while not legal:
            inp_move = input(self.name + " please enter your move (x y): ")
            #try:
            l_moves = [int(s) for s in inp_move.split() if s.isdigit()]
            if len(l_moves) == 2:
                x_move = l_moves[0]
                y_move = l_moves[1]
                if not self.is_illegal_move(board.get_arr(), (x_move, y_move), inp_choice):
                    legal = True
                    self.moves[self.counter%3] = (x_move, y_move)
                    self.counter += 1
                    self.counter = self.counter % 3
                    return (x_move, y_move)
                else:
                    print("Wrong Format")
            '''except:
                pass
                print("Something Went wrong. Please Try Again!")'''

    def __str__(self):
        return self.name + "!"
