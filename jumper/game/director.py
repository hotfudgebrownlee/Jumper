from game.guesser import Guesser
from game.breakdown import Breakdown
from game.console import Console
import random

class Director:
    """This class runs the program until the word is completely guessed,
    or until the parachuter is dead.

    Attributes:
        wordlist(list of strings): a random list of words.
        guesser(Guesser): an instance of guesser.
        breakdown(Breakdown): an instance of breakdown.
        console(Console): an instance of console.
        word(string): a word from the list.
        keep_playing(boolean): indicates if player can keep playing.
        check(list): used to check if word has been guessed.
    """
    def __init__(self):
        """Class constructor. Declares and Initializes instance attributes.

        self(Director): instance of Director.
        """
        self.guesser = Guesser()
        self.console = Console()
        self.breakdown = Breakdown()
        self.wordlist = ['apple', 'bazaar', 'crayon', 'query', 'ears']
        self.word = ''
        self.keep_playing = True
        self.check = []

    def get_word(self):
        # chooses a word from the list.
        word = random.choice(self.wordlist)
        return word

    def start_game(self):
        self.word = self.get_word()
        self.console.create_blanks(self.word)
        self.console.display_word()
        self.console.display_parachuter(self.breakdown.parachuter)
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            

    def get_inputs(self):
        self.guesser.get_input(self.word)

    def do_updates(self):
        self.breakdown.cut_chute(self.guesser.guess_correct)
        if(len(self.breakdown.parachuter)>5):
            self.keep_playing = True
        else:
            print("Game over!")
            self.keep_playing = False
        self.console.display_guesses(self.guesser.guess_correct,
                                    self.guesser.guess,
                                    self.word)
        self.check_word()
        

    def check_word(self):
        self.check.clear()
        for letter in self.word:
            self.check.append(f'{letter} ')
        if self.console.word == self.check:
            print("You win!")
            self.keep_playing = False

    def do_outputs(self):
        self.console.display_word()
        print()
        self.console.display_parachuter(self.breakdown.parachuter)