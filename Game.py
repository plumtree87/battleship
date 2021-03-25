from Board import Board, P1Board, P2Board

from time import sleep


class Game:
    def __init__(self):
        self.end = False

    def game_start(self):
        player1 = P1Board()
        player2 = P2Board()
        player1.board = player1.generate_board(player1.y_axis, player1.x_axis)
        player2.board = player2.generate_board(player2.y_axis, player1.x_axis)
        player1.fired_upon_locations = player1.generate_board(player1.y_axis, player1.x_axis)
        player2.fired_upon_locations = player1.generate_board(player1.y_axis, player2.x_axis)
        print("\n *ATTENTION* known bug. \n*** You can place your ships off the map, and it will crash the game.\n")
        input("\n Press any key to acknowledge.")
        print("\n", "                 #@*&@^\----------BATTLESHIP----------- ... lol...")
        print("A01 B01 C01 D01 E0#\  \  \  H01 I01 J01 K01 L01 M01 N01 O01 P01 Q01 R01 S01 T01\nA02 B02 C02 D02 E02 \  \  \ H02 I02 J02 K02 L02 M02 N02 O02 P02 Q02 R02 S02 T02\nA03 B03 C03 D03 E03 F\  \  \H03 I03 J03 K03 L03 M03 N03 O03 P03 Q03 R03 S03 T03\nA04 B04 C04 D04 E04 F \  \  \   I04 J04 K04 L04 M04 N04 O04 P04 Q04 R04 S04 T04\nA05 B05 C05 D05 E04 F04\  \__\__ _____________  M05 N05 O05 P05 Q05 R05 S05 T05\nA06 B06 C06 D06 E06 F06 \   H06 I06 J06 K06 L0| M06 N06 O06 P06 Q06 R06 S06 T06\nA07 B07 C07 D07 E07 F07 G\_ H07 I07 J07 K07 L0| M07 N07 O07 P07 Q07 R07 S07 T07\nA08 B08 C08 D08 E08 F08 G0\ H08 I08 J08 K08 L0| M08 N08 O08 P08 Q08 R08 S08 T08\nA09 B______________________ H09 I09 J09 K09 L0|________________ ___ ___ _______\nA10 B\      D10 E10 F10 G10 H10 I10 J10 K10 L10 M10 N10 O10 P10 Q10 R10 S10 T  |\nA11 B1\ C11 D11 E11 F11 G11 H11 I11 J11 K11 L11 M11 N11 O11 P11 Q11 R11 S11  T1/\nA12 B12\    D12 E12 F12 G12 H12 I12 J12 K12 L12 M12 N12 O12 P12 Q12 R12 S12  /2\nA13 B13 \   D13 E13 F13 G13 H13 I13 J13 K13 L13 M13 N12 O13 P13 Q13 R13 S13 /13\nA14 B14 C\  D14 E14 F14 G14 H14 I14 J14 K14 L14 M14 N14 O14 P14 Q14 R14 S14/T14\nA15 B15 C1\ D15 E15 F15 G15 H15 I15 J15 K15 L15 M15 N15 O15 P15 Q14 R15 S1/ T15\nA16 B16 C16\D16 E16 F16 G16 H16 I16 J16 K16 L16 M16 N16 O16 P16 Q16 R16 S/6 T16\nA17 B17 C17 \___E_____17G17___7___7_______17_L1__M17_N17_O17_P17__17_R17/S7 T17\nA18 B18 C18 D18 E18 F18 G18 H18 I18 J18 K18 L18 M18 N18 O18 P18 Q18 R18 S18 T18\nA19 B19 C19 D19 E19 F19 G19 H19 I19 J19 K19 L19 M19 N19 O19 P19 Q19 R19 S19 T19\nA20 B20 C20 D20 E20 F20 G20 H20 I20 J20 K20 L20 M20 N20 O20 P20 Q20 R20 S20 T20\n")
        print("\n Player 1 what is your name?")
        self.create_player(player1)
        print("Player 2 what is your name?")
        self.create_player(player2)
        player1.print_board(player1.board)
        print("\n**NOTE** It's easier to play with CAPS LOCK ON: \n", player1.player, "Place your battleships")

        player1.board = self.place_ships(player1)
        print("\nOK", player1.player, "your ships are all set! Now it's the turn of", player2.player)
        sleep(3)
        self.clear()

        input("press ENTER for next player to begin.\n")
        player2.print_board(player2.board)
        print("\n", player2.player, "Place your battleships")
        player2.board = self.place_ships(player2)
        print("OK BOTH TEAMS ARE SET")
        sleep(3)
        self.clear()

        print(player1.player, "IS IS YOUR TURN!")
        print(" ")
        self.end = self.play_rounds(player1, player2)


    def create_player(self, player):
        name = input("_ ")
        player.player = name

    def place_ships(self, player):
        print("\n Choose where you want to place your battleships.")
        print("Example A01 or F09 or Q11 etc.")
        print("\ndestroyer is ", player.destroyer, "length.")
        xy_choice = input("Choose the coordinate you want to place your destroyer.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.destroyer)
        player.destroyer += 2
        player.print_board(player.board)
        print("\nbattleship is ", player.battleship1, "length.")
        xy_choice = input("Choose the coordinate you want to place battleship1.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.battleship1)
        player.battleship1 += 4
        player.print_board(player.board)
        print("\nbattleship is ", player.battleship2, "length.")
        xy_choice = input("Choose the coordinate you want to place battleship2.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.battleship2)
        player.battleship2 += 4
        player.print_board(player.board)
        print("\nsubmarine is ", player.submarine, "length.")
        xy_choice = input("Choose the coordinate you want to place your submarine.._ ")
        xy_choice = self.validate_xy_choice(xy_choice, player)
        self.place_xy(player, xy_choice, player.submarine)
        player.submarine -= 3
        player.print_board(player.board)
        print("\ncarrier is ", player.carrier, "length.")
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
                    print("*NOTE* PLAY WITH CAPS LOCK ON!")
                    print(G + "This ship is", ship_type, "coordinates long" + W)
                    print(
                        "Do you want it's length to go up, down, left or right from here? To answer, use U, D, L, or R")
                    while choice != "U" or choice != "D" or choice != "L" or choice != "R":
                        if choice == "U":
                            player.battleship_locations.append(player.board[i][j])
                            player.board[i][j] = G + player.board[i][j] + W
                            ship_type -= 1
                            while ship_type > 0:
                                i -= 1
                                ship_type -= 1
                                player.battleship_locations.append(player.board[i][j])
                                player.board[i][j] = G + player.board[i][j] + W
                            break
                        if choice == "D":
                            player.battleship_locations.append(player.board[i][j])
                            player.board[i][j] = G + player.board[i][j] + W
                            ship_type -= 1
                            while ship_type > 0:
                                i += 1
                                ship_type -= 1
                                player.battleship_locations.append(player.board[i][j])
                                player.board[i][j] = G + player.board[i][j] + W
                            break
                        if choice == "L":
                            player.battleship_locations.append(player.board[i][j])
                            player.board[i][j] = G + player.board[i][j] + W
                            ship_type -= 1
                            while ship_type > 0:
                                ship_type -= 1
                                j -= 1
                                player.battleship_locations.append(player.board[i][j])
                                player.board[i][j] = G + player.board[i][j] + W
                            break
                        if choice == "R":
                            player.battleship_locations.append(player.board[i][j])
                            player.board[i][j] = G + player.board[i][j] + W
                            ship_type -= 1
                            while ship_type > 0:
                                ship_type -= 1
                                j += 1
                                player.battleship_locations.append(player.board[i][j])
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

    def fire_at_ships(self, player, enemy):
        print("\n Choose where you want to fire!")
        print("Example, A01 or F09 or K18")
        fire = input("Please input the coordinates that you want to fire at to see if you hit your enemy?\n Don't forget CAPS LOCK ON:__ ")
        hit = self.validate_fire(enemy, fire, player)
        if hit[0] == True:
            enemy.ship_points -= 1
            self.fire_xy(player, hit[1], enemy)
            player.print_board(player.fired_upon_locations)
            print(" HIT!!!")
        else:
            self.miss_fire_xy(player, hit[1], enemy)
            player.print_board(player.fired_upon_locations)
            print("You missed..")

    def validate_fire(self, player, fire, shooter):
        if fire in player.battleship_locations:
            print("FOUND HIM!")
            return True, fire
        i = 0
        j = 0
        while i < len(shooter.fired_upon_locations):
            while j < len(shooter.fired_upon_locations[i]):
                if fire == shooter.fired_upon_locations[i][j]:
                    return False, fire
                j += 1
            i += 1
            j -= 20
        fire_again = input("You probably forgot CAPS, L## .. Try again_  ")
        return self.validate_fire(player, fire_again, shooter)

    def miss_fire_xy(self, player_firing, fire_coordinates, enemy_being_fired_at):
        i = 0
        j = 0
        P = '\033[30m'
        W = "\033[0m"
        while i < len(player_firing.fired_upon_locations) :
            while j < len(player_firing.fired_upon_locations[i]):
                if fire_coordinates == player_firing.fired_upon_locations[i][j]:
                    player_firing.fired_upon_locations[i][j] = P + "000" + W
                    enemy_being_fired_at.board[i][j] = P + "000" + W
                    for ships in enemy_being_fired_at.battleship_locations:
                        if ships == fire_coordinates:
                            enemy_being_fired_at.battleship_locations.remove(ships)
                j += 1
            i += 1
            j -= 20
        print(" ")
        print(player_firing.player, "'s            TOP BOARD            places you've fired")

    def fire_xy(self, player_firing, fire_coordinates, enemy_being_fired_at):
        i = 0
        j = 0
        P = "\033[31m"
        W = "\033[0m"
        while i < len(player_firing.fired_upon_locations) :
            while j < len(player_firing.fired_upon_locations[i]):
                if fire_coordinates == player_firing.fired_upon_locations[i][j]:
                    player_firing.fired_upon_locations[i][j] = P + "XXX" + W
                    enemy_being_fired_at.board[i][j] = P + "XXX" + W
                    for ships in enemy_being_fired_at.battleship_locations:
                        if ships == fire_coordinates:
                            enemy_being_fired_at.battleship_locations.remove(ships)
                j += 1
            i += 1
            j -= 20
        print(" ")
        print(player_firing.player, "'s            TOP BOARD            places you've fired")

    def play_rounds(self, player1, player2):
        while player1.ship_points > 0 or player2.ship_points > 0:
            print(player1.player, "'s                        TOP BOARD           where", player1.player, "has fired.")
            player1.print_board(player1.fired_upon_locations)
            print("\n", player1.player, "IT IS YOUR TURN")
            self.fire_at_ships(player1, player2)
            self.check_player_board(player1)
            if player2.ship_points < 1:
                print(player1.player, 'WINS!"')
                return True
            input("Press enter for next player to see his board.\n")
            print(player2.player, "'s                   TOP BOARD                 where", player2.player, "has fired.")
            player2.print_board(player2.fired_upon_locations)
            print("\n", player2.player, "IT IS YOUR TURN")
            self.fire_at_ships(player2, player1)
            self.check_player_board(player2)
            if player1.ship_points < 1:
                print(player2.player, "WINS!")
                return True
            input('Press enter for next player to see his board.\n')
        print(player1.name, player1.ship_points, "vs", player2.name, player2.ship_points)

    def check_player_board(self, player):
        check_board = "NOT_RIGHT_ANSWER_YET"
        while check_board != "Y" or check_board != "N" or check_board != "y" or check_board != "n":
            if check_board == "y" or check_board == "Y":
                print(player.player, "'s               BOTTOM BOARD        (your ships and their damage taken)    ")
                player.print_board(player.board)
                input("Press any key to clear your board and give next player his turn.")
                break
            if check_board == "n" or check_board == "N":
                break
            else:
                check_board = input("Would you like to check your bottom board? Y or N ")
        self.clear()

    def re_play(self):
        while self.end == True:
            answer = "gibberish"
            while answer != "N" or answer != "Y":
                if answer == "Y":
                    self.end = False
                    self.game_start()
                if answer == "N":
                    self.end = False
                    break

                else:
                    answer = input("Do you want to play again? Y or N   ")
