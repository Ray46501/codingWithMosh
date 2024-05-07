import random

level = int(input("LEVEL: "))
secrect_num = random.randint(0,level)
current_guesses = 0


while True:
    guess = int(input("Guess: "))
    current_guesses += 1
    if guess == secrect_num:
        print(f"You Win with {current_guesses} guesses!")
        break
    elif guess > secrect_num:
        print("Lower")
    elif guess < secrect_num:
        print("Higher")    