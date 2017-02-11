from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


class Game():

    @property
    def directions(self):
        return {
            'left':  {'start': Point(0, 0), 'movement': (0, 1), 'cols': 'width', 'rows': 'height'},
            'right': {'start': Point(0, self.width - 1), 'movement': (0, -1), 'cols': 'width', 'rows': 'height'},
            'down': {'start': Point(self.height - 1, 0), 'movement': (-1, 0), 'cols': 'height', 'rows': 'width'},
            'up': {'start': Point(0, 0), 'movement': (1, 0), 'cols': 'height', 'rows': 'width'},
        }

    def __init__(self, width=None, height=None, board=None):
        self.width = width
        self.height = height
        self.board = self.set_board(board)

    def __str__(self):
        return str(self.board)

    def display_board(self):
        top_left = '\u250c'
        top_right = '\u2510'
        top_middle = '\u252c'
        middle_left = '\u251c'
        middle_right = '\u2524'
        middle_middle = '\u253c'
        bottom_left = '\u2514'
        bottom_right = '\u2518'
        bottom_middle = '\u2534'
        vertical = '\u2502'
        horizontal = '\u2500'
        h_cell = horizontal * 5
        top_row = top_left + ((h_cell + top_middle) * (self.width - 1)) + h_cell + top_right + '\n'
        middle_row = middle_left + ((h_cell + middle_middle) * (self.width - 1)) + h_cell + middle_right + '\n'
        bottom_row = bottom_left + ((h_cell + bottom_middle) * (self.width - 1)) + h_cell + bottom_right + '\n'
        display = top_row
        for idx, row in enumerate(self.board):
            display += vertical + vertical.join(['{:^5}'.format(x) for x in row]) + vertical + '\n'
            if idx != len(self.board) - 1:
                display += middle_row
        display += bottom_row
        return display

    def play(self):
        while True:
            print(self.display_board())
            move = input('>>')
            self.take_turn(move)

    def set_board(self, board):
        if not board:
            return [[0 for col in range(self.width)] for row in range(self.height)]
        self.width = len(board[0])
        self.height = len(board)
        return board

    def take_turn(self, direction):
        start = self.directions[direction]['start']
        movement = self.directions[direction]['movement']
        cols = self.directions[direction]['cols']
        steps = getattr(self, self.directions[direction]['cols'])
        for offset in range(getattr(self, self.directions[direction]['rows'])):
            start_cell = Point(start.x + offset, start.y) if cols == 'width' else Point(start.x, start.y + offset)
            line = self.calculate_line(list(self.get_line(start_cell, movement, steps)))
            self.set_line(start_cell, movement, steps, line)

    def get_line(self, start_cell, direction, steps):
        for step in range(steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            yield self.board[row][col]

    def set_line(self, start_cell, direction, steps, line):
        for step in range(steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            self.board[row][col] = line[step]

    def calculate_line(self, line):
        shifted = self.shift(line)
        merged = list(self.merge(shifted))
        padded = self.pad(merged, len(line))
        return padded

    def shift(self, line):
        return [x for x in line if x]

    def pad(self, line, length):
        padding = [0] * (length - len(line))
        return line + padding

    def merge(self, line):
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


if __name__ == '__main__':
    grid = [
        [0, 2, 4, 0],
        [2, 2, 4, 4],
        [2, 0, 2, 2],
    ]
    game = Game(board=grid)
    game.play()
