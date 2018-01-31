import Board
import Player
import Bot


class Arena:
    def __init__(self, name="Default", inp_players = []):
        self.board = Board.ultimateBoard()
        self.players = inp_players

    def play(self):
        recent_move = ()
        print(self.board)
        counter = 0
        flag = False
        while not flag:
            inp_move = input(self.players[counter % 2].get_name() + " please enter your move (super_row super_col inner_row inner_col): ")
            l_moves = [int(s) for s in inp_move.split() if s.isdigit()]
            if len(l_moves) == 4:
                super_row = l_moves[0]
                super_col = l_moves[1]
                inner_row = l_moves[2]
                inner_col = l_moves[3]
                recent_move = (super_row, super_col, inner_row, inner_col)
                flag = self.board.add_move(recent_move, (counter) % 2)
                print(str(self.board) + "\n\n")
                counter += 1

        while counter < 81:
            prev_move = recent_move
            if self.board.get_arr()[recent_move[-2]][recent_move[-1]].get_status() != " ":
                prev_move = (200, 200, 200, 200)
            recent_move = self.players[counter % 2].get_move(self.board, prev_move, counter)
            if self.board.add_move(recent_move, counter%2):
                print(str(self.board) + "\n\n")
                counter += 1
                flag = self.board.check_win(recent_move)
                if flag:
                    print(str(self.players[(counter-1) % 2]) + " Won")
                    return
        print ("Game Over! No One Won")
        return

def main():
    name = input("Hi there. Please Enter you name ")
    flag = False
    while not flag:
        choice = input("Would you like to play v/s player or v/s computer. Enter 'P' for player and 'C' for computer ")
        if choice in ["P", "p"]:
            name_second = input("Hi there. Please Enter the name for the second player ")
            arena = Arena(name, [Player.Player(name), Player.Player(name_second)])
            flag = True
        elif choice in ["C", "c"]:
            arena = Arena(name, [Player.Player(name), Bot.Bot("Computer Bot!")])
            flag = True
        else:
            print("Please enter the choice from 'P' or 'C'")
    arena.play()


main()
