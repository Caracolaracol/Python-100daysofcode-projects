import random




def guessinggame():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    difficulty = input("Choose a dificulty. Type 'easy' or 'hard':")
        
    if difficulty == 'easy':
        attemps = 10
    elif difficulty == 'hard':
        attemps = 5
    keep_playing = True
    while keep_playing:
        guess = int(input("Make a guess:"))
        if guess == number_to_guess:
            print("That's the number, you win!")
            keep_playing = False
        elif guess > number_to_guess:
            attemps = attemps - 1
            print("Too High, guess again")
        elif guess < number_to_guess:
            attemps = attemps - 1
            print("Too low, guess again")
        if attemps == 0:
            print("You don't have more attemps, you lose")
            keep_playing = False


guessinggame()