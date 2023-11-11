import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "coding", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        current_display = display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Correct!")
                guessed_letters.append(guess)
            else:
                print("Incorrect!")
                attempts -= 1
        else:
            print("Please enter a valid single letter.")

        if "_" not in display_word(secret_word, guessed_letters):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            break

    if attempts == 0:
        print(f"\nSorry, you ran out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
