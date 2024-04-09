import random
import sys
def main():
    while True:
        level = input('Level: ')
        if level.isnumeric() and int(level) > 0:
            level = random.randint(1 , int(level))
            break
    while True:
        guess = input('Guess: ')
        if guess.isnumeric() :
            guess = int(guess)
            if guess > level :
                print('Too Large! ')
            elif guess < level :
                print('too Small! ')
            else :
                print('Just right! ')
                sys.exit()
                
main()

        