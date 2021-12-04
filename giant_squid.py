class Game:
    """Defines a Bingo game"""

    def __init__(self) -> None:
        self.boards = []
        self.draws = []

    def set_board(self, board: list) -> None:
        """Receives a list of strings and creates a Board

        Args:
            board_str (list): [List of strings representing a board]
        """
        new_board = Board(board)
        self.boards.append(new_board)

    def set_draws(self, draws: str) -> None:
        """Sets the draws list

        Args:
            draws (str): [String list of drwas]
        """
        self.draws = list(map(int, draws.split(",")))

    def find_best_board(self):
        """Runs the Bing rounds and checks for a winner after each one"""
        for draw in self.draws:
            self.call_a_draw(draw)
            if self.check_for_winner(draw):
                break

    def call_a_draw(self, draw: int) -> None:
        """Checks if the drawn number exists on the boards

        Args:
            draw ([int]): [Drawn number]
        """
        for board in self.boards:
            board.check_number_in_board(draw)

    def check_for_winner(self, draw: int) -> bool:
        """After the draw is called. Checks if any bingo board won the game

        Args:
            draw (int): [Drawn number]

        Returns:
            bool: [Indicates if a board won]
        """
        for board in self.boards:
            if board.winner:
                print(board.get_winning_points(draw))
                return True
        return False


class Board:
    def __init__(self, board) -> None:
        self.board = board
        self.marks = [[0] * 5] * 5
        self.winner = False

    def check_number_in_board(self, number: int) -> None:
        """Checks if a number exists in the board. If it exists, it is set to -1 so that
        it isn't counted in the final sum

        Args:
            number ([int]): [Drawn number]
        """
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                if number == self.board[row][col]:
                    self.board[row][col] = -1
                    if self.check_winning_row(row):
                        self.winner = True
                    elif self.check_winning_col():
                        self.winner = True

    def get_winning_points(self, draw: int) -> int:
        """Counts the total number of points in the winning board

        Args:
            draw (int): [Drawn number]

        Returns:
            int: [Number of points]
        """
        sum_ = 0
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                if self.board[row][col] > -1:
                    sum_ += self.board[row][col]

        winning_points = sum_ * draw

        return winning_points

    def check_winning_row(self, row) -> bool:
        """Check if a row has won

        Args:
            row ([int]): [Row number]

        Returns:
            bool: [Indicates if it is a winning row]
        """
        if len(set(self.board[row])) == 1:
            return True

        return False

    def check_winning_col(self) -> bool:
        """Checks if a column has won

        Returns:
            bool: [Indicates if there is a winning column]
        """
        for i in range(len(self.board)):
            if (
                self.board[0][i]
                + self.board[1][i]
                + self.board[2][i]
                + self.board[3][i]
                + self.board[4][i]
                == -5
            ):
                return True

        return False


if __name__ == "__main__":
    game = Game()

    with open("/Users/gerardo.garzon/CodeGym/AdventOfCode/input4.txt", "r") as f:
        lines = f.readlines()

    current_board = []
    for i in range(0, len(lines)):
        clean_line = lines[i].strip()
        if i == 0:
            game.set_draws(lines[0])
        elif clean_line != "":
            current_board.append(list(map(int, lines[i].split())))

        if len(current_board) == 5:
            game.set_board(current_board)
            current_board = []

    game.find_best_board()
