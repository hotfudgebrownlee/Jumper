class Guesser:
    def __init__(self):
        self.track_guess = []
        self.guess_correct = True
        self.guess = ''
        
    def get_input(self, word):
        guess = input('Guess a letter [a-z]: ').lower()
        if guess in "abcdefghijklmnopqrstuvwxyz":
            if len(guess) != 1:
                print(self.track_guess)
                if guess in self.track_guess:
                    print(f"You've already guessed {guess}. Try again!")
                    self.get_input(word)
                else:
                    if guess in word:
                        "yep"
                        self.guess_correct = True
                    else:
                        "nope"
                        self.guess_correct = False
                    self.track_guess.append(guess)
                    self.guess = guess
        else:
            print("Not a valid guess.")
            self.get_input(word)