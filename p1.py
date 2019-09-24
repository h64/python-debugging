from random import randint

guessed = False
target = randint(1, 10)

while not guessed:
    print("I'm thinking of a number between 1 and 10")
    guess = int(input("Please guess what it is:\n"))
    if(guess < target):
        print('Too low!')
    if(guess > target):
        print('Too high!')
    if(guess == target):
        print("That's it! You win!")
        guessed = True