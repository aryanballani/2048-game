import numpy as np

class Board2048:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.board = np.zeros((self.grid_size, self.grid_size), dtype=int)

    def reset_board(self):
        self.board = np.zeros((self.grid_size, self.grid_size), dtype=int)

    def get_board(self):
        return self.board.copy()

    def set_board(self, board):
        self.board = np.array(board, dtype=int)

    def move_left(self):
        moved = False
        for i in range(self.grid_size):
            original = self.board[i].copy()
            self.board[i] = self._merge_row(self.board[i])
            if not np.array_equal(original, self.board[i]):
                moved = True
        return moved

    def move_right(self):
        self.board = np.fliplr(self.board)
        moved = self.move_left()
        self.board = np.fliplr(self.board)
        return moved

    def move_up(self):
        self.board = self.board.T
        moved = self.move_left()
        self.board = self.board.T
        return moved

    def move_down(self):
        self.board = np.fliplr(self.board.T)
        moved = self.move_left()
        self.board = np.fliplr(self.board).T
        return moved

    def _merge_row(self, row):
        non_zero = row[row != 0]
        merged = []
        i = 0
        while i < len(non_zero):
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                merged.append(non_zero[i] * 2)
                i += 2
            else:
                merged.append(non_zero[i])
                i += 1
        merged += [0] * (self.grid_size - len(merged))
        return np.array(merged, dtype=int)

    def count_zeroes(self):
        return np.count_nonzero(self.board == 0)

    def no_moves_left(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.board[i, j] == 0:
                    return False
                if j + 1 < self.grid_size and self.board[i, j] == self.board[i, j + 1]:
                    return False
                if i + 1 < self.grid_size and self.board[i, j] == self.board[i + 1, j]:
                    return False
        return True

    def add_tile(self, position, value):
        r, c = position
        self.board[r, c] = value