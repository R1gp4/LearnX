"""Hangman

Hi Roman. I reviewed your code and I can follow some of your logic. There
are some good ideas here but I can see you are struggling to get things
working.

I thought the best thing I can do right now is give you a hand with
some of the game logic.

Perhaps you can play around with this and extend it bit by bit with new
ideas.

You need to find a way to keep track of what the user is inputting. One way
of doing this is to choose a python container object such as a 'list',
'set', 'tuple' or 'dict'.

Each container object has special properties that may help you implement
your hangman algorithm.

Good luck, and I will try to be more responsive as you iterate towards your
solution.

Example interaction from the python3 interpreter::

    >>> from hangman import hangman
    >>> hangman('apples')
    Welcome to the game, Hangman!
    I am thinking of a word that is 6 letters long.
    -------------
    You have 8 guesses left.
    Please guess a letter: a
    YAY
    You have 7 guesses left.
    Please guess a letter: p
    YAY
    You have 6 guesses left.
    Please guess a letter: p
    YAY
    You have 5 guesses left.
    Please guess a letter: l
    YAY
    You have 4 guesses left.
    Please guess a letter: d
    You have 3 guesses left.
    Please guess a letter: w
    You have 2 guesses left.
    Please guess a letter: v
    You have 1 guesses left.
    Please guess a letter: w
    Game Over
    >>>

"""


def hangman(secret_word):
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

    print("Welcome to the game, Hangman!")
    print(
        "I am thinking of a word that is {} letters long."
        .format(len(secret_word))
    )
    print("-------------")

    guessed = False
    turns_left = 8

    while not guessed and turns_left > 0:
        print("You have {} guesses left.".format(turns_left))
        guess = input("Please guess a letter: ")
        if guess in secret_word:
            print("YAY")
        turns_left = turns_left - 1

    print("Game Over")

hangman('agent')











'''

    print "welcome to the game, Hangman!"
    f=0
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long."
    lettersGuessed = ''
    i=0
    while i<8:
        print "-------------"
        print "You have "+str(8-i) +" guesses left."
        print "Available letters: "+str(getAvailableLetters(lettersGuessed))
        guess=raw_input("Please guess a letter: ")
        guess=guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed+=guess
            if guess in secretWord:
                 print "Good guess: "+str(getGuessedWord(secretWord, lettersGuessed))   
                 if secretWord == getGuessedWord(secretWord, lettersGuessed):
                    print "-------------"
                    print "congratulations, you won!"
                    f=1
                    break
            else :
                i=i+1
                print "Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed))
    if f==0 and i==8:
        print "-------------\nSorry, you ran out of guesses. The word was "+str(secretWord)+". "                        



'''
