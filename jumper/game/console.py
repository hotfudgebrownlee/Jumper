class Console:

    # This Class is here to display everything to the console, it will retrive all 
    # the updates that the other funtions make and will display them.

    def __init__(self):
        self.word = []

    def create_blanks(self,guess_word):
        # in order to display the correct amount of blank lines to the screen, the 
        # word will be read from the director class and the length will be calculated
        # using the len() function
        word_length = len(guess_word)
        # the word variable will be filled with the right amount of blanks using
        # this for loop which will also print the word variable to the sceen
        for i in range(word_length):
            self.word.append("_ ")
    
    def display_word(self):
        for letter in self.word:
            print(letter,end='')
        print('')

    def display_parachuter(self, parachuter):
        #This will display the parachuter variable to the screen
        j = 0
        for j in parachuter:
            print (j)
            
    def display_guesses(self,correct,guess,guess_word):
        if correct:
            for i in range(len(guess_word)):
                if guess_word[i] == guess:
                    self.word[i] = f'{guess} '