
class Board:
    def __init__(self):
        self.y_axis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        self.x_axis = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        self.battleship_locations = []
        self.board = []
        self.fired_upon_locations = []
        self.ship_points = 1
        self.player = ""
        self.destroyer = 2
        self.submarine = 3
        self.battleship1 = 4
        self.battleship2 = 4
        self.carrier = 5


class P1Board(Board):
    def __init__(self):
        super().__init__()

    def generate_board(self, y_axis, x_axis):
        return [[(count + x) for count in y_axis] for x in x_axis]

    def print_board(self, generated_board):
        for xy in generated_board:
            print(*xy)


class P2Board(Board):
    def __init__(self):
        super().__init__()

    def build_board(self, size=20):
        return [["~" for count in range(size)] for count in range(size)]

    def generate_board(self, y_axis, x_axis):
        return [[(count + x) for count in y_axis] for x in x_axis]

    def print_board(self, generated_board):
        for xy in generated_board:
            print(*xy)

