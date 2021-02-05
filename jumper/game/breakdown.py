from pprint import pprint
class Breakdown:
    """The purpose of this class is to keep track of the user
    score. It passes a parachuter display to the console class
    and a keep_playing value to the director class. It receives
    a boolean value on if the guess was correct from the guesser
    classs.

    Attributes:
        guess_correct (boolean): a value of whether the guess was
            correct.
        parachuter (list of strings): A list of strings that, when
            displayed, show a parachuter. List is changed by incorrect
            guesses.

    Methods: 
        cut_chute(self, parachuter): cuts off a line of the parachuter
            if guess is false. returns cut parachuter.
        
    Returns:
        keep_playing (boolean): indicates if parachute is gone or not.
    """
    def __init__(self):
        """Class constructor. Declares/Initializes instance attributes.

        self(Breakdown): Instance of Breakdown.
        """
        self.parachuter = ["  ___  ",
                           " /___\ ",
                           " \   / ",
                           "  \ /  ",
                           "   0   ",
                           "  /|\  ",
                           "  / \  ",
                           "       ",
                           "^^^^^^^"]
        self.guess_correct = True
        self.keep_playing = True
    
    def cut_chute(self, parachuter):
        if self.keep_playing:
            if not self.guess_correct:
                parachuter.pop(0)
                return parachuter
            return parachuter
        else:
            parachuter[0] = "   X   "
            return parachuter

    def can_guess(self):
        self.keep_playing = (len(self.parachuter) > 5)


"""TESTS
# test to make sure the class can be initialized.
x = Breakdown()
# test to make sure parachute prints correctly.
for line in x.parachuter:
    print(line)
# test to make sure a false guess cuts the chute.
x.guess_correct = False
x.cut_chute(x.parachuter)
for line in x.parachuter:
    print(line)
# test to make sure a true guess maintains the chute.
x.guess_correct = True
x.cut_chute(x.parachuter)
for line in x.parachuter:
    print(line)
"""