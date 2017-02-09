import unittest

from cli_2048 import Game


class GameTests(unittest.TestCase):

    def setUp(self):
        self.grid = [
            [2, 2, 0, 0],
            [0, 0, 4, 0],
            [8, 8, 0, 16]
        ]
        self.game = Game(board=self.grid)

    def test_game_initializes_with_blank_board_of_right_size_if_one_not_provided(self):
        game = Game(width=2, height=3)
        expected = [
            [0, 0],
            [0, 0],
            [0, 0],
        ]
        self.assertEqual(expected, game.board)

    def test_initializes_with_passed_in_board_and_sets_width_and_height(self):
        self.assertEqual(self.game.board, self.grid)
        self.assertEqual(self.game.width, 4)
        self.assertEqual(self.game.height, 3)

    def test_shift_left(self):
        expected = [
            [4, 0, 0, 0],
            [4, 0, 0, 0],
            [16, 16, 0, 0]
        ]
        self.game.take_turn('left')
        self.assertEqual(expected, self.game.board)

    def test_shift_right(self):
        expected = [
            [0, 0, 0, 4],
            [0, 0, 0, 4],
            [0, 0, 16, 16]
        ]
        self.game.take_turn('right')
        self.assertEqual(expected, self.game.board)

    def test_shift_up(self):
        expected = [
            [2, 2, 4, 16],
            [8, 8, 0, 0],
            [0, 0, 0, 0]
        ]
        self.game.take_turn('up')
        self.assertEqual(expected, self.game.board)

    def test_shift_down(self):
        expected = [
            [0, 0, 0, 0],
            [2, 2, 0, 0],
            [8, 8, 4, 16]
        ]
        self.game.take_turn('down')
        self.assertEqual(expected, self.game.board)
