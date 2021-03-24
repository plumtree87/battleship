from Board import Board, P1Board, P2Board

class Game:
    def __init__(self):
        self.end = False

    def game_start(self):
        player1 = P1Board()
        player2 = P2Board()
        player1.board = player1.generate_board(player1.y_axis, player1.x_axis)
        print("\n                        ----------BATTLESHIP-----------")
        player1.print_board(player1.board)
        print("\n Player 1 what is your name?")
        self.create_player(player1)
        print("Player 2 what is your name?")
        self.create_player(player2)
        print(player1.player, "Place your battleships")
        player1.battleship_locations = self.place_destroyer(player1)
        player1.print_board(player1.board)

    def create_player(self, player):
        name = input("_ ")
        player.player = name

    def place_destroyer(self, player):
        print
        print("First, place your destroyer. It is 2 spaces in size.")
        print("\n Choose where on the Y-axis you will place your destroyer.")
        print("Example A1 or F11")
        xy_choice = input("Choose the coordinate you want to place your first battleship._ ")
        self.place_xy(player, xy_choice, player.battleship1)



    def fix1_9(self, x_choice):
        if x_choice < 10:
            x = str(x_choice)
            space = " "
            x_useful_choice = x + space
            print(x_useful_choice)
            return x_useful_choice

    def place_x(self, player, x_choice):
        while x_choice not in player.x_axisNum:
            if x_choice in player.x_axisNum:
                return x_choice
            else:
                while True:
                    try:
                        x_choice = int(input("1-10 X-axis choice?  "))
                        return x_choice
                    except ValueError:

                        print("Invalid input. Please choose a number 1-10 for the X-axis")
        else:
            return x_choice

    def place_y(self, player, y_choice):
        while y_choice not in player.y_axis:
            if y_choice in player.y_axis:
                return y_choice
            else:
                y_choice = input("Please use the CAP letter of your choice_ ")
        if y_choice in player.y_axis:
            return y_choice

    def place_xy(self, player, xy_choice, ship_type):
        i = 0
        j = 0
        P = "\033[35m"
        while i < len(player.board):
            while j < len(player.board[i]):
                if xy_choice == player.board[i][j]:
                    print("FOUND IT", player.board[i][j])
                    player.board[i][j] = "***"
                    print(player.board[i][j])
                    choice = "NothingYet"
                    print(
                        "As a player, you're solely responsible to put your pieces on the board right.\n So stick within bounds. No letting half your ship hang off the board.\n Dont break my game! I didnt' know how to prevent it easiliy....")
                    print("This ship is", ship_type, "coordinates long")
                    print(
                        "Do you want it's length to go up, down, left or right from here? To answer, use u, d, l, or r")
                    while choice != "u" or choice != "d" or choice != "l" or choice != "r":
                        if choice == "u":
                            while ship_type > 0:
                                i -= 1
                                ship_type -= 1
                                player.board[i][j] = "***"
                            break
                        if choice == "d":
                            while ship_type > 0:
                                i += 1
                                ship_type -= 1
                                player.board[i][j] = "***"
                            break
                        if choice == "l":
                            while ship_type > 0:
                                ship_type -= 1
                                j -= 1
                                player.board[i][j] = "***"
                            break
                        if choice == "r":
                            while ship_type > 0:
                                ship_type -= 1
                                j += 1
                                player.board[i][j] = "***"
                            break
                        else:

                            choice = input("u d l or r  ??")

                j += 1
            i += 1
            j -= 20

        print("DONE")


