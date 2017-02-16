import random


class TTT():

    GRID_SPOTS = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def __init__(self):
        self.move_list = self.set_up_moves()
        self.x_moves = []
        self.o_moves = []

    def check_win(self, moves):
        return any((set(win).issubset(set(moves)) for win in self.win_conditions))

    def set_up_moves(self):
        return random.sample(self.GRID_SPOTS, k=len(self.GRID_SPOTS))

    def choose_spot(self, player):
        player.append(self.move_list.pop())

    @property
    def win_conditions(self):
        return frozenset(((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)))
