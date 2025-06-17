import random
import numpy as np

class TileGenerator:
    def __init__(self, prob_two):
        self.prob_two = prob_two

    def get_random_tile_value(self):
        """Return 2 with probability prob_two, else 4."""
        return 2 if random.random() < self.prob_two else 4

    def get_random_empty_position(self, board):
        """Return a random (row, col) tuple from empty positions on the board."""
        empty_positions = list(zip(*np.where(board == 0)))
        if not empty_positions:
            return None
        return random.choice(empty_positions)