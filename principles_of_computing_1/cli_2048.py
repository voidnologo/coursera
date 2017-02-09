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
