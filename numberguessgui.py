"""
numberguessgui.py
author - will - 07/12/23
chpt 8 gui demo for number guessing game
"""
#imports 
####MUST HAVE BREEZYPYTHONGUI IN SAME WORKING DIRECTORY#####
from breezypythongui import EasyFrame
from random import randint

#Guessing game class 
class GuessingGame(EasyFrame):
    #class constructor method
    def __init__(self):
        EasyFrame.__init__(self, title="Guessing Game", width=300, height=210, background="cadet blue")
        
        #Class Variables
        self.magicNum = randint(1,100)
        self.count = 0

        #widget creation code block
        self.hintLabel = self.addLabel(text="Guess a Number between 1 & 100", row=0, column=0, background="light cyan", columnspan=2, sticky="NSEW")

        self.addLabel(text="Your Guess: ", row=1, column=0, background="light cyan")
        self.guessField = self.addIntegerField(value=0, row=1, column=1)
        self.nextBtn = self.addButton(text = "Next", row=2, column=0, command=self.nextGuess)
        self.newBtn = self.addButton(text="New Game", row=2, column=1, command= self.newGame)

    def nextGuess(self):
        self.count +=1
        guess = self.guessField.getNumber()

        #gamelogic
        if guess == self.magicNum:
            self.hintLabel["text"] = "OH Swag you got it " + str(self.count) + " attempts"
            self.nextBtn["state"] ="disabled"
        elif guess < self.magicNum:
            self.hintLabel["text"] = "Sorry, your guess was too Low"
        else:
            self.hintLabel["text"] = "Sorry, your guess was too High"
    #reset loop
    def newGame(self):
        self.magicNum = randint(1,100)
        self.count = 0
        self.hintLabel["text"] = "Guess a Number between 1 & 100"
        self.guessField.setNumber(0)
        self.nextBtn["state"] ="normal"

















def main():
    #main run funcition
    GuessingGame().mainloop()

if __name__ == "__main__":
    main()
