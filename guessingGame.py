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
        if (counter < numGuesses - 1):
            print("Try Again")
            counter += 1
            if int(guess < rndNmbr):
                print("Lower")
            if int(guess < rndNmbr):
                print("Higher")
        else:
            print("You Lost!")
            break

guessingGame()
