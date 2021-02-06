from director import Director
from breakdown import Breakdown
from guesser import Guesser

class Console:

    # This Class is here to display everything to the console, it will retrive all 
    # the updates that the other funtions make and will display them.

    def __init__(self):
        self.director = Director()
        self.breakdown = Breakdown() 
        self.guesser = Guesser()
        self.word = []

    

    def display_word(self):
        # in order to display the correct amount of blank lines to the screen, the 
        # word will be read from the director class and the length will be calculated
        # using the len() function
        word_length = len(self.director.get_word())

        i = 0

        # the word variable will be filled with the right amount of blanks using
        # this for loop which will also print the word variable to the sceen
        for i in word_length:
            if self.word == None:
                self.word.append("_ ")

            print ( f"{self.word[i]}" )

        print ( "" )

    def display_parachuter(self):
        #This will display the parachuter variable to the screen
        j = 0
        for j in range(8):
            print (self.breakdown.parachuter[j])
            
    def display_guesses(self):
        print (self.guesser.guess)