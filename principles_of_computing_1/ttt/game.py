import collections
import random


class InvalidMoveException(Exception):
    pass


Player = collections.namedtuple('Player', ['name', 'moves'])


class TTT():

    GRID_SPOTS = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def __init__(self):
        self.x = Player('X', [])
        self.o = Player('O', [])
        self.current_player = self.x
        self.open_spots = list(self.GRID_SPOTS[:])

    def play(self):
        end = False
        while not end:
            print()
            # print('X:', self.x.moves)
            # print('O:', self.o.moves)
            # print('Remaining spots:', self.open_spots)
            self.print_board()
            if self.open_spots:
                move = int(input("{}'s turn >> ".format(self.current_player.name)))
                try:
                    self.take_move(move)
                except InvalidMoveException:
                    print('Invalid move.')
                    continue
                if self.check_win(self.current_player.moves):
                    print(self.current_player.name, ' wins!')
                    end = True
            else:
                print('No open Moves')
                end = True
            self.toggle_player()

    def print_board(self):
        def value(spot):
            if spot in self.x.moves: return self.x.name
            if spot in self.o.moves: return self.o.name
            return spot
        for row in zip(*[iter(self.GRID_SPOTS)] * 3):
            print(' '.join([str(value(i)) for i in row]))

    def toggle_player(self):
        self.current_player = self.o if self.current_player == self.x else self.x

    def take_move(self, move=None):
        try:
            self.open_spots.remove(move)
            self.current_player.moves.append(move)
        except ValueError:
            raise InvalidMoveException

    def check_win(self, moves):
        return any((set(win).issubset(set(moves)) for win in self.win_conditions))

    @property
    def win_conditions(self):
        return frozenset(((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)))


class MonteCarloTTT(TTT):

    TRIALS = 100
    SCORE_CURRENT = 1.0
    SCORE_OTHER = 1.0

    def __init__(self, board):
        self.initial_board = board
        self.move_list = self.set_up_moves(self.inital_board)

    def set_up_moves(self):
        return random.sample(self.GRID_SPOTS, k=len(self.GRID_SPOTS))

    def choose_spot(self, player):
        player.moves.append(self.move_list.pop())


if __name__ == '__main__':
    game = TTT()
    game.play()
