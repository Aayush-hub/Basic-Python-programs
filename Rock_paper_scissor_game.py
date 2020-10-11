from random import choice
import sys


class RPSGame:
    def __init__(self):
        self.win, self.lose, self.tie = 0, 0, 0
        self.options = ['Rock', 'Paper', 'Scissor']
        print("\n\n"+"Welcome to Rock, Paper, Scissor GAME".center(46, "-"))

    def show_result(self):
        print("\nWIN = {0}  LOSE = {1}  TIE = {2}".format(
            self.win, self.lose, self.tie))
        print("\nEnter Rock, Paper, Scissor or (q)uit\n")

    def take_input(self):
        self.inp = input()   # User input
        if self.inp in self.options:
            print(' VS')
        elif (self.inp == "q"):
            sys.exit()
        else:
            print("ENTER VALID INPUT\n")
            self.take_input()

    def pc_move(self):
        self.pc = choice(self.options)   # Taking pc input
        print(f'{self.pc}')

    def game_won(self):
        print("\nYou WIN.")
        self.win += 1

    def game_lost(self):
        print("\nYou LOSE.")
        self.lose += 1

    def check_conditions(self):
        if self.inp == self.pc:
            print("\nIt's a TIE.")
            self.tie += 1
        elif self.inp == 'Rock':
            if self.pc == 'Paper':
                self.game_lost()
            else:
                self.game_won()
        elif self.inp == 'Paper':
            if self.pc == 'Scissor':
                self.game_lost()
            else:
                self.game_won()
        elif self.inp == 'Scissor':
            if self.pc == 'Rock':
                self.game_lost()
            else:
                self.game_won()
        print("\n"+"-"*46)

    def show_final_win(self):
        print("\nWIN = {0}  LOSE = {1}  TIE = {2}".format(
            self.win, self.lose, self.tie))
        if self.win > self.lose:
            print("\nWinner of the Game : YOU\n")
        elif self.win > self.lose:
            print("\nWinner of the Game : COMPUTER\n")
        else:
            print("\nResult of the Game : IT'S A TIE\n")

    def play(self):
        for _ in range(5):
            self.show_result()
            self.take_input()
            self.pc_move()
            self.check_conditions()
        self.show_final_win()


if __name__ == "__main__":
    game = RPSGame()
    game.play()
