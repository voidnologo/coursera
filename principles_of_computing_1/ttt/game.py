import collections
import random
import time


class InvalidMoveException(Exception):
    pass


Player = collections.namedtuple('Player', ['name', 'moves'])
MontePlayer = collections.namedtuple('MontePlayer', ['name', 'moves', 'new_moves'])


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

    TRIALS = 10
    SCORE_CURRENT = 1.0
    SCORE_OTHER = 1.0

    def __init__(self, board, x_moves, o_moves):
        self.x = MontePlayer('X', x_moves, [])
        self.o = MontePlayer('O', o_moves, [])
        self.current_player = self.x
        self.initial_board = board[:]
        self.move_list = self.set_up_moves()
        self.scores = collections.defaultdict(int)

    def set_up_moves(self):
        return random.sample(self.initial_board, k=len(self.initial_board))

    def choose_spot(self, player):
        player.new_moves.append(self.move_list.pop())

    def play(self):
        for cnt, _ in enumerate(range(self.TRIALS)):
            print('Trial:', cnt, '\n')
            while self.move_list:
                print()
                self.choose_spot(self.current_player)
                self.print_board()
                if self.check_win(self.current_player.moves + self.current_player.new_moves):
                    self.score_game()
                    break
                self.toggle_player()
                time.sleep(1)
            self.reset()
        print('BEST MOVE:', self.best_move())
        return self.best_move()

    def reset(self):
        del self.x.new_moves[:]
        del self.o.new_moves[:]
        self.move_list = self.set_up_moves()

    def score_game(self):
        if self.current_player is self.x:
            self.score_moves(self.x.new_moves, self.SCORE_CURRENT)
            self.score_moves(self.o.new_moves, -self.SCORE_OTHER)
        else:
            self.score_moves(self.o.new_moves, self.SCORE_OTHER)
            self.score_moves(self.x.new_moves, -self.SCORE_CURRENT)
        print('\nSCORES:', self.scores)

    def score_moves(self, moves, value):
        for spot in moves:
            self.scores[spot] += value

    def best_move(self):
        high_score = max(self.scores.values())
        return next((k for k, v in self.scores.items() if v == high_score))

    def print_board(self):
        def value(spot):
            if spot in self.x.moves + self.x.new_moves: return self.x.name
            if spot in self.o.moves + self.o.new_moves: return self.o.name
            return spot
        for row in zip(*[iter(self.GRID_SPOTS)] * 3):
            print(' '.join([str(value(i)) for i in row]))


if __name__ == '__main__':
    # game = TTT()
    # game.play()
    game = MonteCarloTTT([1, 2, 4, 7], [3, 5], [8, 9])
    game.play()
