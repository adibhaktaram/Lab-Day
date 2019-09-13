import random
def guessingGame():
    rndNmbr = random.randint(0,20)
    numGuesses = 10
    counter = 0
    while(counter < numGuesses):
        guess = input("Guess a number:")
        if (int(guess == rndNmbr)):
            print("You Win!")
            break
        else:
            if (int(guess < rndNmbr - 1)):
                print("Try Again")
            else:
                print("You Lost!")
                counter += 1



guessingGame()
