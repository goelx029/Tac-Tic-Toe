import Board
import Player
import Bot


class Arena:
    def __init__(self, name="Default", inp_players = []):
        self.board = Board.threeDimensionalBoard()
        self.players = inp_players

    def play(self):
        print(self.board)
        counter = 0
        while counter < 27:
            move = self.players[counter % 2].get_move(self.board)
            if self.board.add_move(move, counter % 2):
                print(self.board)
                if counter >= 7:
                    if self.board.check_win(move):
                        print(str(self.players[counter % 2]) + "Won")
                        return 0
                counter += 1
        print ("Game Over! No One Won")
        return 1

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