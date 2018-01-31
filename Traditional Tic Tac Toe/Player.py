# a Player class - Abstract away all the functionality required for the player in the game


class Player:
    def __init__(self, input_name="Default"):
        self.name = input_name

    '''getter and setters for the object variables'''

    def set_name(self, input_name):
        self.name = input_name

    def get_name(self):
        return self.name

    # get_move function is required to prompt the player to enter a move
    # parameters are really not necessary here however to make it easier to use the function for implementing the working
    # of the computer bot the parameters just stay here.
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
