import Board
import Player
import Bot


class Arena:
    def __init__(self, name="Default", inp_players = []):
        self.board = Board.TraditionalBoard()
        self.players = inp_players

    '''def draw_board(self, t):
        ########################
        t.penup()
        t.goto(0, 100)
        t.pendown()
        t.pensize(10)
        t.goto(300, 100)
        ########################
        t.penup()
        t.goto(0, 200)
        t.pendown()
        t.goto(300, 200)
        ########################
        t.penup()
        t.goto(100, 0)
        t.pendown()
        t.goto(100, 300)
        ########################
        t.penup()
        t.goto(200, 0)
        t.pendown()
        t.goto(200, 300)

    def draw_o(self, y, x):
        x = 100 * x + 50
        y = 100 * y + 50
        turtle.penup()
        turtle.goto(x, y - 40)
        turtle.pendown()
        turtle.pensize(2)
        turtle.pencolor("red")
        turtle.circle(40)

    def draw_x(self, y, x):
        x = 100 * x + 50
        y = 100 * y + 50
        turtle.pensize(2)
        turtle.pencolor("blue")
        turtle.penup()
        turtle.goto(x - 40, y - 40)
        turtle.pendown()
        turtle.setheading(45)
        turtle.fd(80 * 1.414)
        turtle.penup()
        turtle.goto(x - 40, y + 40)
        turtle.pendown()
        turtle.setheading(-45)
        turtle.fd(80 * 1.414)
        turtle.setheading(0)'''

    def play(self):
        print(self.board)
        counter = 0
        while counter < 9:
            move = self.players[counter % 2].get_move(self.board, (counter)%2)
            if self.board.move(move, counter % 2):
                print(self.board)
                if counter >= 4:
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