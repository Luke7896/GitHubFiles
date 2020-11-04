"""
Program: Hangman GUI


"""


import random

from breezypythongui import EasyFrame

class hangman(EasyFrame):


    def __init__(self):

        EasyFrame.__init__(self)
        self.setBackground("light grey")
        self.addLabel(text = "HANGMAN", row = 0, column = 1, sticky = "N")
        self.addButton(text = "Instructions", row = 0, column = 2,\
                       command = self.instruction)
        self.addButton(text = "New", row = 0, column = 0)
        self.display = self.addTextField(text = "", row = 1, column = 1,\
                                         state = "readonly", sticky = "N")

        self.addLabel(text = "Enter a single letter", row = 3, column = 1,\
                      sticky = "N")
        self.addTextField(text = "", row = 4, column = 1, sticky = "N", width = 2)

        self.game = {1:"You win!", 2:"You lose!", 3:"The word was",\
            4:"You have used these letters: ", \
            5:"You have {}/6 incorrect guesses remaining!",\
            6:"Press enter to start the game",7:"Invalid entry",\
            8:"You've already guessed ",9:"Incorrect!",10:"Correct!",\
            11:"Guess a single letter: ",12:"Word: ",13:"HANGMAN",\
            14:"""The game will choose a random secret word.\n
You will attempt to guess the secret word by entering one letter at a time.\n
You will be allowed 6 incorrect guesses."""}


 
    def instruction(self):
        self.messageBox(title = "Instructions", message = self.game[14])

    
        

    
        

    




def main():
    hangman().mainloop()

if __name__ == "__main__":
    main()
