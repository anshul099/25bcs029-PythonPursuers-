import random

numCorrect = random.randint(1, 10) 
print(numCorrect)
print('The Computer has chosen a random number between 1 and 10!')
print('You have 3 tries!! Guess the number~')
numUser = int(input('Enter your guess: '))

for guess in range (1, 4) :
    if numUser == numCorrect :
        print('You guessed Correct!!')
        break
    else :
        print('Wrong guess,', guess , 'try used.')
        if guess == 3 :
            print('You failed....')
        else :
            numUser = int(input('Try again: '))
        