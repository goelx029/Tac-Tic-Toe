# a player class


class Player:
    def __init__(self, input_name="Default"):
        self.name = input_name

    def set_name(self, input_name):
        self.name = input_name

    def get_name(self):
        return self.name

    def get_move(self, board, inp_choice):
        legal = False
        while not legal:
            move = input(self.name + " please enter your move (x y): ")
            try:
                moves = [int(s) for s in move.split() if s.isdigit()]
                if len(moves) == 2:
                    x_move = moves[0]
                    y_move = moves[1]
                    legal = True
                    return (x_move, y_move)
                else:
                    #print (moves)
                    print("Wrong Format")
            except:
                print("Something Went wrong. Please Try Again!")

    def __str__(self):
        return self.name + "!"
