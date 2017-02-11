import unittest

from cli_2048 import Game


class Cli2048PlayTests(unittest.TestCase):

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
