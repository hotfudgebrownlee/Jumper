from director import Director
from breakdown import Breakdown
class Guesser:
    def __init__(self):
        self.track_guess = 0
        self.director = Director()
        self.breakdown = Breakdown()
        self.guess = ''
    def get_input(self):
        guess = input('Guess a letter [a-z]: ')
        if guess in self.director.word():
            self.guess = guess
            self.track_guess += 1
        else:
            self.breakdown.cut_chute()
            self.track_guess += 1
            self.get_input
    def correct_guess(self):
        pass