import constant as constant
from board import Board2048
from tile_generator import TileGenerator

class Game2048:
    def __init__(self, grid_size=None, prob_two=None):
        self.grid_size = grid_size if grid_size else constant.GRID_SIZE
        self.prob_two = prob_two if prob_two else constant.PROBABILITY_OF_TWO
        self.board = Board2048(self.grid_size)
        self.tile_generator = TileGenerator(self.prob_two)
        self.game_over = False
        self.won = False
        self.start_game()

    def start_game(self):
        self.board.reset_board()
        first_pos = self.tile_generator.get_random_empty_position(self.board.get_board())
        self.board.add_tile(first_pos, 2)
        self.game_over = False
        self.won = False  # Reset won flag

    def check_state(self):
        board_arr = self.board.get_board()
        if (board_arr == constant.WIN_VALUE).any():
            print(constant.WIN_MESSAGE)
            self.won = True
            self.game_over = False  # Don't set game_over on win
            return True
        if self.board.count_zeroes() == 0 and self.board.no_moves_left():
            print(constant.LOSE_MESSAGE)
            self.game_over = True
            self.won = False
            return True
        return False
    
    def check_won(self):
        return self.won

    def add_block(self):
        if self.board.count_zeroes() == 0:
            return
        number = self.tile_generator.get_random_tile_value()
        position = self.tile_generator.get_random_empty_position(self.board.get_board())
        if position:
            self.board.add_tile(position, number)

    def move_left(self):
        moved = self.board.move_left()
        if moved:
            self.add_block()
        return moved

    def move_right(self):
        moved = self.board.move_right()
        if moved:
            self.add_block()
        return moved

    def move_up(self):
        moved = self.board.move_up()
        if moved:
            self.add_block()
        return moved

    def move_down(self):
        moved = self.board.move_down()
        if moved:
            self.add_block()
        return moved

    def get_board(self):
        return self.board.get_board()

    def is_game_over(self):
        return self.game_over