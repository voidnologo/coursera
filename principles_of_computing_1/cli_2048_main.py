import cmd

from cli_2048 import Game


class GameLoop(cmd.Cmd):

    welcome = "Command Line 2048 "
    prompt = '>>> '

    def preloop(self):
        print(self.welcome)
        self.initialize_game()

    def initialize_game(self):
        default = (4, 4)
        size = input('What size of game board do you want? \nFormat: x, y  Example: 2, 3\n(press Enter for default of 4x4) >>')
        x, y = [int(q.strip()) for q in size.split(',')] if size else default
        self.game = Game(width=x, height=y)
        amount = int(x * y / 3) or 1
        for _ in range(amount):
            empty = self.game.find_empty()
            self.game.add_new_tile(empty)
        self.display_board()

    def display_board(self):
        print(self.game.display_board())

    def do_h(self, args):
        'Shift tiles left'
        self.game.take_turn('left')

    def do_left(self, args):
        self.do_h(args)

    def do_l(self, args):
        'Shift tiles right'
        self.game.take_turn('right')

    def do_right(self, args):
        self.do_l(args)

    def do_j(self, args):
        'Shift tiles up'
        self.game.take_turn('up')

    def do_up(self, args):
        self.do_j(args)

    def do_k(self, args):
        'Shift tiles down'
        self.game.take_turn('down')

    def do_down(self, args):
        self.do_k(args)

    def do_q(self, args):
        return True

    def do_quit(self, args):
        return True

    def postcmd(self, stop, line):
        if line in ('q', 'quit'):
            return True
        empty = self.game.find_empty()
        if not empty:
            return self.lose_game()
        self.game.add_new_tile(empty)
        self.display_board()
        return stop

    def lose_game(self):
        print('You have failed!!! ')
        return True


if __name__ == '__main__':
    GameLoop().cmdloop()
