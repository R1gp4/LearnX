print("Please think of a number between 0 and 100!")

high = 100
low = 0
num_guesses = 0

flag = True
while flag == True:
    guess = (high + low)/2.0
    print('Is your secret number', int(guess), ' ?')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ",end='')
    answer = input()
    answer = str(answer)
        
    if answer == 'h':
        high = (high + low)/ 2.0
        num_guesses += 1
        
    if answer == 'l':
        low = (high + low)/2.0
        num_guesses += 1
    
    if answer == 'c':
        print("Game over. Your secret number was:", int(guess))
        break

    else: #answer != 'c' or 'l' or 'h':
        print("Sorry, I did not understand your input.")
        

