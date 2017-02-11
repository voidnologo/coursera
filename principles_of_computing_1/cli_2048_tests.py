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

    def test_find_empty_spots_to_add_new_tiles_in(self):
        grid = [
            [0, 2],
            [2, 2],
            [2, 0],
        ]
        game = Game(board=grid)
        expected = [(0, 0), (2, 1)]
        result = game.find_empty()
        self.assertEqual(expected, result)

    def test_add_new_value_to_empty_spot(self):
        grid = [
            [0, 2],
            [2, 2],
        ]
        game = Game(board=grid)
        empty = game.find_empty()
        game.add_new_tile(empty)
        self.assertIn(game.board[0][0], (2, 4))


class Cli2048GridTests(unittest.TestCase):

    def setUp(self):
        self.grid = [
            [0, 2, 4, 0],
            [2, 2, 4, 4],
            [2, 0, 2, 2],
        ]
        self.game = Game(board=self.grid)

    def test_display_board_displays_game_object_correctly(self):
        expected =  '┌─────┬─────┬─────┬─────┐\n'
        expected += '│  0  │  2  │  4  │  0  │\n'
        expected += '├─────┼─────┼─────┼─────┤\n'
        expected += '│  2  │  2  │  4  │  4  │\n'
        expected += '├─────┼─────┼─────┼─────┤\n'
        expected += '│  2  │  0  │  2  │  2  │\n'
        expected += '└─────┴─────┴─────┴─────┘\n'
        self.assertEqual(expected, self.game.display_board())

    def test_display_board_displays_game_with_different_dimensions(self):
        grid = [
            [0, 2],
            [2, 2],
            [2, 0],
        ]
        game = Game(board=grid)
        expected =  '\u250c\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2500\u2510\n'
        expected += '\u2502  0  \u2502  2  \u2502\n'
        expected += '\u251c\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2524\n'
        expected += '\u2502  2  \u2502  2  \u2502\n'
        expected += '\u251c\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2524\n'
        expected += '\u2502  2  \u2502  0  \u2502\n'
        expected += '\u2514\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2518\n'
        self.assertEqual(expected, game.display_board())

    def test_str_returns_game_board(self):
        self.assertEqual(str(self.grid), str(self.game))
