import random
# random.randrange(stop) or random.randrange(start,stop,step)
# returns a randomly selected element from range(start, stop, step


def guess(x):  # x is our parameter, function returns a random number between 1 and x
    # basically you have 5 Guesses left
    guess_count = 5
    print(f"you have {guess_count} guesses Left!! Goodluck~ ")
    random_number=random.randint(1,x)
    guess=0 #initialize the guessed number to zero ~

    while guess != random_number:  # keeps going untill you are right
        guess = int(input(f"Guess a number between 1 and {x} : "))
        guess_count -= 1
        if guess < random_number:
            print("Number you guessed is too low. ")
            print(f"Number of guesses remaining: {guess_count}")
        elif guess > random_number:
            print("Number you guessed is too high")
        else:
            print("Congrats you guessed the right number !")
            print(int(guess))
            break
        if guess_count == 0:
            print("You Have Zero Guesses remaining! Sorry")
            break  # breaks the while loop
