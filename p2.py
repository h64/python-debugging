from random import randint

guessed = False
target = randint(1, 10)

while not guessed:
    print("I'm thinking of a number between 1 and 10")
    guess = input("Please guess what it is:\n")
    try:
        guess = int(guess)
        if(guess < target):
            print('Too low!')
        if(guess > target):
            print('Too high!')
        if(guess == target):
            print("That's it! You win!")
            guessed = True
    except ValueError:
        print('That is not a number, Bart!')
