import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guess the Number Game!")
    print("I've selected a random number between 1 and 100. Can you guess it?")

    attempts = 0

    while True:
        # Ask the user to input their guess
        user_guess = int(input("Your guess: "))
        
        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_the_number()
