import unittest

from game import TTT


class TTTTests(unittest.TestCase):

    def setUp(self):
        self.sut = TTT()

    def test_basic_win_condition(self):
        moves = [2, 5, 3, 7, 9]
        win = self.sut.check_win(moves)
        self.assertTrue(win)

    def test_win_returns_false_if_no_win(self):
        moves = [2, 1, 4, 8, 9]
        win = self.sut.check_win(moves)
        self.assertFalse(win)

    def test_set_up_turns(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(sorted(self.sut.move_list), expected)


if __name__ == '__main__':
    unittest.main()
