from Board import Board, P1Board, P2Board
import os
from time import sleep


class Game:
    def __init__(self):
        self.end = False

    def game_start(self):
        player1 = P1Board()
        player2 = P2Board()
        player1.board = player1.generate_board(player1.y_axis, player1.x_axis)
        player2.board = player2.generate_board(player2.y_axis, player1.x_axis)
        print("\n                        ----------BATTLESHIP-----------")
        player1.print_board(player1.board)
        print("\n Player 1 what is your name?")
        self.create_player(player1)
        print("Player 2 what is your name?")
        self.create_player(player2)

        print("\n**NOTE** It's easier to play with CAPS LOCK ON: \n", player1.player, "Place your battleships")

        player1.battleship_locations = self.place_ships(player1)
        print("OK", player1.player, "your ships are all set! Now it's the turn of", player2.player)
        sleep(3)
        self.clear()

        player2.print_board(player2.board)
        print(player2.player, "Place your battleships")
        player2.battleship_locations = self.place_ships(player2)
        print("OK BOTH TEAMS ARE SET")
        sleep(3)
        self.clear()

        print(player1.player, "IS IS YOUR TURN!")
        player1.fired_upon_locations = self.fire_at_ships(player2)

    def validate_fire(self, player, fire):
        i = 0
        if i < len(player.battleship_locations):
            while i < len(player.battleship_locations):
                if fire in player.battleship_locations[i]:
                    return fire
                else:
                    i += 1
                    continue

        xy_choice = input("Input exactly as displayed on Board. Use CAP L## Format_ ")
        return self.validate_xy_choice(player, xy_choice)

    def create_player(self, player):
        name = input("_ ")
        player.player = name

    def fire_at_ships(self, enemy):
        print("\n Choose where you want to fire!")
        print("Example, A01 or F09 or K18")
        fire = input("Please input the coordinates that you want to fire at to see if you hit your enemy?")
        fire = self.validate_fire(enemy, fire)
        print(fire)

    def place_ships(self, player):
        print("\n Choose where you want to place your battleships.")
        print("Example A01 or F09 or Q11 etc.")
        xy_choice = input("Choose the coordinate you want to place your destroyer.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.destroyer)
        player.destroyer += 2
        player.print_board(player.board)
        xy_choice = input("Choose the coordinate you want to place battleship1.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.battleship1)
        player.battleship1 += 4
        player.print_board(player.board)
        xy_choice = input("Choose the coordinate you want to place battleship2.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.battleship2)
        player.battleship2 += 4
        player.print_board(player.board)
        xy_choice = input("Choose the coordinate you want to place your submarine.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.submarine)
        player.submarine -= 3
        player.print_board(player.board)
        xy_choice = input("Choose the coordinate you want to place your aircraft carrier.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.carrier)
        player.carrier += 5
        print(" ")
        player.print_board(player.board)
        return player.board

    def validate_xy_choice(self, xy_choice, player):
        i = 0
        if i < len(player.board):
            while i < len(player.board):
                if xy_choice in player.board[i]:
                    return xy_choice
                else:
                    i += 1
                    continue

        xy_choice = input("Input exactly as displayed on Board. Use CAP L## Format_ ")
        return self.validate_xy_choice(xy_choice, player)


    def place_xy(self, player, xy_choice, ship_type):
        i = 0
        j = 0
        P = "\033[35m"
        W = "\033[0m"
        G = "\033[1;32;40m"
        while i < len(player.board):
            while j < len(player.board[i]):
                if xy_choice == player.board[i][j]:
                    print(player.board[i][j])
                    choice = "NothingYet"
                    print(
                        "As a player, you're solely responsible to put your pieces on the board right.\n So stick within bounds. No letting half your ship hang off the board.\n I didnt build rules to prevent it yet..")
                    print("*Note* the game is easier to play with CAPS LOCK ON.")
                    print(G + "This ship is", ship_type, "coordinates long" + W)
                    print(
                        "Do you want it's length to go up, down, left or right from here? To answer, use u, D, L, or R")
                    while choice != "U" or choice != "D" or choice != "L" or choice != "R":
                        if choice == "u":
                            player.battleship_locations[i][j] = player.board[i][j]
                            player.board[i][j] = G + player.board[i][j] + W
                            ship_type -= 1
                            while ship_type > 0:
                                i -= 1
                                ship_type -= 1
                                player.board[i][j] = G + player.board[i][j] + W
                            break
                        if choice == "D":
                            player.board[i][j] = G + player.board[i][j] + W
                            ship_type -= 1
                            while ship_type > 0:
                                i += 1
                                ship_type -= 1
                                player.board[i][j] = G + player.board[i][j] + W
                            break
                        if choice == "L":
                            player.board[i][j] = G + player.board[i][j] + W
                            ship_type -= 1
                            while ship_type > 0:
                                ship_type -= 1
                                j -= 1
                                player.board[i][j] = G + player.board[i][j] + W
                            break
                        if choice == "R":
                            player.board[i][j] = G + player.board[i][j] + W
                            ship_type -= 1
                            while ship_type > 0:
                                ship_type -= 1
                                j += 1
                                player.board[i][j] = G + player.board[i][j] + W
                            break
                        else:

                            choice = input("U D L or R  ??")

                j += 1
            i += 1
            j -= 20

    def clear(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")