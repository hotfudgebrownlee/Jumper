# from game.director import Director
class Guesser:
    def __init__(self):
        self.track_guess = []
        # self.director = Director()
        self.guess_correct = True
        self.word = "apples"
        
    
    def get_input(self):
        guess = input('Guess a letter [a-z]: ')
        if guess in "abcdefghijklmnopqrstuvwxyz":
            if len(guess) != 1:
                if guess in self.track_guess:
                    print(f"You've already guessed {guess}. Try again!")
                    self.get_input()
                else:
                    if guess in self.word:
                        self.guess_correct = True
                        self.track_guess.append(guess)
                    else:
                        self.guess_correct = False
                        self.track_guess.append(guess)
        else:
            print("Not a valid guess.")
            self.get_input()

x = Guesser()
x.get_input()
print (x.guess_correct)