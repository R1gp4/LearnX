print("Please think of a number between 0 and 100!")

high = 100
low = 0
num_guesses = 0
guessed = False

while not guessed:
    guess = (high + low)//2
    print("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if answer == 'c':
        guessed == True
        break
    
    elif answer == 'h':
        high = guess
        num_guesses += 1
        
    elif answer == 'l':
        low = guess
        num_guesses += 1
       

    else: #answer != 'c' or 'l' or 'h':
        print("Sorry, I did not understand your input.")
        
print("Game over. Your secret number was: " + str(guess))