# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    letters=[secretWord[0]]

    for i in range(0,len(secretWord)):

        if secretWord[i] not in letters:
            letters+=secretWord[i]

    for i in range(0,len(letters)):

        if letters[i] not in lettersGuessed:
            return False
    return True

    #assert return boolean, 'output is not boolean'




def getGuessedWord(secretWord, lettersGuessed):
    
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    # FILL IN YOUR CODE HERE...
    # subsitute x with lettersGuessed?
    lettersGuessed = ''
    
    letters=[secretWord[0]]
    
    for i in range(0, len(secretWord)):
        
        if secretWord[i] in lettersGuessed:
            lettersGuessed += secretWord[i]
        
        else:
            lettersGuessed += '_ '
            
    return(lettersGuessed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    lettersGuessed = ''
    a = 'abcdefghijklmnopqrstuvwxyz'
    
    #going through the alphabet; when the character is not in the list lettersguessed, 
    # add this character to the empty string b. Otherwise do nothing, continue to the next character.

    for i in a:
        if i not in lettersGuessed:
            lettersGuessed += i
    
    return(lettersGuessed)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    


    lettersGuessed  = ''
    turns_left = 8
    guessed = False

    print("Welcome to the game, Hangman!")
    print(
        "I am thinking of a word that is {} letters long."
        .format(len(secretWord))
    )
    print("-------------")
   
    while not guessed and turns_left > 0:

        print("You have {} guesses left." .format(turns_left))
        print("Available letters: " +str(getAvailableLetters(lettersGuessed)))
        guess = input("Please guess a letter: " )

        if guess in secretWord:
            print("Good guess:" +str(getGuessedWord(secretWord, lettersGuessed)))

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " +str(lettersGuessed))
            turns_left -= 1

        if guess not in secretWord and guess not in lettersGuessed:  
            print("Oops! That letter is not in my word: " +str(getGuessedWord(secretWord, lettersGuessed)))
            turns_left -= 1

        if isWordGuessed(secretWord, lettersGuessed):
            break

    if turns_left == 0:
        print("Sorry, you ran out of guesses. The word was" +str(secretWord))

    print("-------------")
    print("Congratulations, you won!")







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
