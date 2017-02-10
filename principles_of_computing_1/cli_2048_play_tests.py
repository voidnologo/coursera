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

    def test_str_displays_game_object_correctly(self):
        expected =  '+-----+-----+-----+-----+\n'
        expected += '|  0  |  2  |  4  |  0  |\n'
        expected += '+-----+-----+-----+-----+\n'
        expected += '|  2  |  2  |  4  |  4  |\n'
        expected += '+-----+-----+-----+-----+\n'
        expected += '|  2  |  0  |  2  |  2  |\n'
        expected += '+-----+-----+-----+-----+\n'
        self.assertEqual(expected, str(self.game))

    def test_str_displays_game_with_two_by_three(self):
        grid = [
            [0, 2],
            [2, 2],
            [2, 0],
        ]
        game = Game(board=grid)
        expected =  '+-----+-----+\n'
        expected += '|  0  |  2  |\n'
        expected += '+-----+-----+\n'
        expected += '|  2  |  2  |\n'
        expected += '+-----+-----+\n'
        expected += '|  2  |  0  |\n'
        expected += '+-----+-----+\n'
        self.assertEqual(expected, str(game))
