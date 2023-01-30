#This is a guess the number game.
import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 20)
print(f"Well, {name} I am thinking of a number between 1 and 20.")
# Comment-out the "DEGUG:" line below before submitting the production code!
print('DEBUG: Secret number is ' + str(secretNumber))

for guessesTaken in range (1, 7):
    "range (1, 7) means 6 tries to guess the number"
    print('Take a guess at the number between 1 and 20')
    # "input reverts a string so we need to convert it to int"
    guessedNumber = int(input())
    if guessedNumber < secretNumber:
        print('Your guess is too low')
    elif guessedNumber > secretNumber:
        print('Your guess is too high')
    else:
    # This condition is for the correct guess
        break

if guessedNumber == secretNumber:
    print(f"Good job, {name}! You guessed my number in {str(guessesTaken)} guess(es)!")
else:
    print("Nope " + name + " the number I was thinking of was " + str(secretNumber) + "!")