class Breakdown:
    """The purpose of this class is to keep track of the user
    score. It passes a parachuter display to the console class
    and a can_play value to the director class. It receives
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
    def __init__(self,can_play):
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
        self.can_play = True
    
    def cut_chute(self, guess_correct):
        """This method cuts a line off the top of the chute if the guess 
        was incorrect. If the chute is cut to the parachuter's head, the
        head is replaced with an X and the game ends because the parachuter
        is dead.

        Args:
            self(Breakdown): Instance of Breakown.
            guess_correct(boolean): passed in from the guesser class.

        Returns:
            can_play(boolean): communicate whether player can keep playing.
        """
        if not guess_correct:
            self.parachuter.pop(0)
        if (len(self.parachuter)>5):
            self.can_play = True
        else:
            self.parachuter[0] = "   X   "
            self.can_play = False
            self.parachuter.append("Game over!")
        return self.can_play


"""TESTS
import random
options = [True, False]
# test to make sure the class can be initialized.
x = Breakdown()
# test to make sure parachute prints correctly.
for line in x.parachuter:
    print(line)
# loop until the game ends.
while x.can_play:
    # test to make sure a random guess maintains or breaks
    # the chute depending on if it's true or false.
    bool_op = (random.choice(options))
    x.cut_chute(bool_op)
    print(bool_op)
    for line in x.parachuter:
        print(line)
"""