import random

level = int(input("LEVEL: "))
secret_num = round(random.random()*level)
current_guesses = 0


while True:
    guess = int(input("Guess: "))
    current_guesses += 1
    
    score = round(((level*level)/(current_guesses*current_guesses))/(level/10))
    
    if guess == secret_num:
        print(f"The Secret Number was {secret_num} You Win with {current_guesses} guesses and a score of {score}!")
        break

    elif guess > secret_num:
        print("Lower")
        
    elif guess < secret_num:
        print("Higher")   
