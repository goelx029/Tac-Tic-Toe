import Board
import Player
import Bot
import turtle


class Arena:
    def __init__(self, name="Default", inp_players = []):
        self.board = Board.TraditionalBoard()
        self.players = inp_players

    def play(self):
        print(self.board)
        counter = 0
        flag = False
        while not flag:
            recent_move = self.players[counter % 2].update_moves(self.board, (counter)%2)
            self.board.reset_board()
            self.board.update_board(self.players[counter % 2].get_moves(), (counter)%2)
            self.board.update_board(self.players[(counter+1) % 2].get_moves(), (counter+1)%2)
            print(self.board)
            counter += 1
            if counter >= 4:
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
