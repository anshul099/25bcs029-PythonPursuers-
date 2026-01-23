import random

while True:
    numCorrect = random.randint(1, 10)
    # Computer randomly selects a number between 1 and 10

    # --------Test-----------
    # print(numCorrect)
    # -----------------------

    print("The Computer has chosen a random number between 1 and 10!")
    print("You have 3 tries!! Guess the number~")

    guess = 1
    while 1 <= guess <= 3:
        # Error Handling
        try:
            numUser = int(input("Enter your guess: "))
            if numUser < 1 or numUser > 10:
                raise ValueError
        except ValueError:
            print("!INVALID INPUT! Please enter an integer between 1 and 10")
            continue

        if numUser == numCorrect:
            print("You guessed Correct!!")
            break
            # If user guesses correctly, loop stops
        else:
            print("Wrong guess,", guess, "try used.")
            guess += 1
            if guess > 3:
                print("You failed.... The correct number was", numCorrect)
                # When the user uses all 3 tries, the correct number is revealed
            else:
                print("Try Again..")

    # To restart the game
    while True:

        playAgain = input("Do you want to play again? (y/n): ").lower()

        if playAgain == "y":
            break
        elif playAgain == "n":
            print("Thank you for playing!")
            exit()
        else:
            print("Invalid input! Enter either y or n.")
