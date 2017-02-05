import unittest

def shift(line):
    return [x for x in line if x]


def pad(line, length):
    padding = [0] * (length - len(line))
    return line + padding


def merge(line):
    idx1 = 0
    idx2 = 1
    while idx1 < len(line):
        if idx2 < len(line) and line[idx1] == line[idx2]:
            yield line[idx1] + line[idx2]
            idx1 = idx2 + 1
            idx2 = idx2 + 2
        else:
            yield line[idx1]
            idx1 = idx2
            idx2 += 1


def calculate_line(line):
    shifted = shift(line)
    merged = list(merge(shifted))
    padded = pad(merged, len(line))
    return padded


class GameTests(unittest.TestCase):

    def test_basic_merge(self):
        line = [2, 2]
        result = list(merge(line))
        self.assertEqual(result, [4])

    def test_basic_dont_merge(self):
        line = [2, 4]
        result = list(merge(line))
        self.assertEqual(result, [2, 4])

    def test_dont_merge_cells_more_than_once(self):
        line = [2, 2, 4]
        result = list(merge(line))
        self.assertEqual(result, [4, 4])

    def test_dont_merge_cells_more_than_once_arbitrary_length(self):
        line = [2, 2, 4, 8, 8, 4, 4, 8]
        result = list(merge(line))
        self.assertEqual(result, [4, 4, 16, 8, 8])

    def test_shifts_filled_cells_to_the_left_and_drop_blanks(self):
        line = [0, 2]
        result = shift(line)
        self.assertEqual(result, [2])

    def test_shifts_cells_for_arbitrary_length_of_input(self):
        line = [0, 0, 1, 3, 0, 5, 0, 7]
        result = shift(line)
        self.assertEqual(result, [1, 3, 5, 7])

    def test_returns_empty_list_if_no_values(self):
        line = [0, 0, 0]
        result = shift(line)
        self.assertEqual(result, [])

    def test_pad_returns_list_with_correct_number_of_elements(self):
        line = [1, 2]
        length = 4
        result = pad(line, length)
        self.assertEqual(result, [1, 2, 0, 0])

    def test_pad_does_not_add_elements_if_line_already_long_enough(self):
        line = [1, 2, 3, 4]
        length = 4
        result = pad(line, length)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_integration_empty_case(self):
        line = [0, 0, 0, 0, 0]
        result = calculate_line(line)
        self.assertEqual(result, [0, 0, 0, 0, 0])

    def test_integration_base_case(self):
        line = [2]
        result = calculate_line(line)
        self.assertEqual(result, [2])

    def test_integration_case_1(self):
        line = [2, 2]
        result = calculate_line(line)
        self.assertEqual(result, [4, 0])

    def test_integration_case_2(self):
        line = [2, 2, 4]
        result = calculate_line(line)
        self.assertEqual(result, [4, 4, 0])

    def test_integration_case_3(self):
        line = [2, 0, 2, 4]
        result = calculate_line(line)
        self.assertEqual(result, [4, 4, 0, 0])

    def test_integration_case_4(self):
        line = [2, 2, 0, 2, 4]
        result = calculate_line(line)
        self.assertEqual(result, [4, 2, 4, 0, 0])


if __name__ == '__main__':
    unittest.main()
