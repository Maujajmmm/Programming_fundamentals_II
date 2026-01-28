secret_number = 129837
guess = 1
maximum = 0
minimum = 0
guesses = 0
e = 2.71828
while True:
    guesses += 1
    print(guess)
    guess = round(guess)
    if guess == secret_number:
        print(f"num is {secret_number}")
        print(f"took {guesses} guesses")
        break
    elif guess > secret_number:
        maximum = guess
        if minimum:
            guess = minimum + (maximum - minimum)*0.68
        else:
            guess = maximum/e
    elif guess < secret_number:
        minimum = guess
        if maximum:
            guess = maximum + (maximum - minimum)*0.68
        else:
            guess = minimum*e
