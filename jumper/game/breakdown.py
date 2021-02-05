from pprint import pprint
class Breakdown:
    """The purpose of this class is to keep track of the user
    score. It passes a parachuter display to the console class
    and a keep_playing value to the director class. It receives
    a boolean value on if the guess was correct from the guesser
    classs.

    Attributes:
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
        self.keep_playing = True
    
    def cut_chute(self, guess_correct):
        if not guess_correct:
            self.parachuter.pop(0)
        if (len(self.parachuter)>5):
            self.keep_playing = True
        else:
            self.parachuter[0] = "   X   "
            self.keep_playing = False
            self.parachuter.append("Game over!")
        return self.keep_playing


"""TESTS
import random
options = [True, False]
# test to make sure the class can be initialized.
x = Breakdown()
# test to make sure parachute prints correctly.
for line in x.parachuter:
    print(line)
# loop until the game ends.
while x.keep_playing:
    # test to make sure a random guess maintains or breaks
    # the chute depending on if it's true or false.
    bool_op = (random.choice(options))
    x.cut_chute(bool_op)
    print(bool_op)
    for line in x.parachuter:
        print(line)
"""