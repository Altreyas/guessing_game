'''
Joseph Burns
5-20
1/22/20
Description - Random Number Guessing Game - This program will have a user try and
guess to see what number the computer is thinking about.
'''

# We need to input random in order to get the computer's number.
import random

'''
So in main, the program will keep track of a guessing counter in order to
tell the user how many times they guessed. The computer will
generate a random number through the computerRandom function
and the player will guess it. It will pass
the two numbers in to the higherOrLower function to find if the user's
number is higher, lower, or congruent with the computer's number.
'''

def main():
    while True:
        guessCounter = 0
        computerNumber = computerRandom()
        userNumber = int(input("I'm thinking of a number between 1-100, what is it? "))
        while userNumber != computerNumber:
            guessCounter += 1
            higherOrLower(userNumber,computerNumber)
            if userNumber != computerNumber:
                userNumber = int(input("New guess: "))
        higherOrLower(userNumber,computerNumber)
        print("It took you",guessCounter,"guess(s) to get my number.")
        
def computerRandom():
    cRandomNumber = random.randint(1,100)
    return cRandomNumber

def higherOrLower(user,computer):
    if user > computer:
        print("Too high, try again")
    elif user < computer:
        print("Too low,try again")
    else:
        print("Congratulations! You guessed the number")

# Let's play the game!
main()
