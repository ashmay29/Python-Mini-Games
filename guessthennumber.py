import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose the difficulty Easy or Hard: Type 'easy' or 'hard': ")
if difficulty.lower() == 'easy':
    no_of_guesses = 10
else:
    no_of_guesses = 5

print(f"You have {no_of_guesses} attempts to guess the correct number.")
secret_number = random.randint(1, 100)

while no_of_guesses > 0:
    guess = int(input("Make a guess: "))
    if guess > secret_number:
        print("Too High.")
    elif guess < secret_number:
        print("Too Low.")
    else:
        print(f"Congratulations! You guessed the answer {secret_number}!!")
        break
    no_of_guesses -= 1
    if no_of_guesses > 0:
        print(f"You have {no_of_guesses} attempts remaining.")
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

