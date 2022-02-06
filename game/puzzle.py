from ast import For
import random

class Puzzle():
    '''
        Class Puzzle
        this class represents a hidden incognite and handles the comparation 
        funtions since only the puzzle knows its hidden word
    '''
    def __init__(self):
        '''
        Constuctor of class Puzzle
        arguments: self reference
        class attributes: 
            __dictionary (private): list of possible words
            __secretWord (private):  random word taken from the dictionary list 
        '''
        self.__dictionary = ["mountain", "apple", "germany", "hope" ]
        self.__secretWord = random.choice(self.__dictionary)
        self.leng = len(self.__secretWord)

    def checkWord(self,word):
        '''
        verify if the given word is the hidden word of the puzzle
        arguments: 
            
            - self reference
        
            - word (string): guessing word. The functions check the given word with
            the secret word of the puzzle, Return true if they are the same, either case
            return false. 
        '''
        if(self.__secretWord == word):
            return True
        else:
            return False

    def checkLetter(self,pos, letter):
        '''
        verify if the given letter is the letter of the hidden word in the given position
        arguments: 
            - self reference 
            - letter (string): The functions check if the given letter is the letter
            the secret word have in the given position, Return true if they are the same, either case
            return false. 
        '''
        if( self.__secretWord[pos] == letter ):
            return True
        else:
            return False

    def printPuzzle(self, turno):
        l = len(self.__secretWord)
        i = 0
        while(i < turno):
            print(self.__secretWord[i], end=" ")
            i = i+1
        while(i < self.leng):
            print("_", end=" ")
            i = i+1

