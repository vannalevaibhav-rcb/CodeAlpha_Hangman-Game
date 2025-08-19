import random

def hangman():
    print(" Welcome to Hangman Game ")
    print("Guess the hidden word, one letter at a time.")
    print("You have 6 incorrect attempts. Good luck!\n")

    # Predefined list of words (5 words)
    words = ["python", "school", "apple", "computer", "friend"]

    # Randomly select a word
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    # Create display version of the word
    hidden_word = ["_"] * len(secret_word)

    # Game loop
    while attempts_left > 0 and "_" in hidden_word:
        print("Word: ", " ".join(hidden_word))
        print(f"Attempts left: {attempts_left}")
        print("Guessed letters: ", " ".join(guessed_letters) if guessed_letters else "None")

        # Player input
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print("✅ Good guess!\n")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    hidden_word[i] = guess
        else:
            print("❌ Wrong guess!\n")
            attempts_left -= 1

    # Game result
    if "_" not in hidden_word:
        print(" Congratulations! You guessed the word:", secret_word)
    else:
        print(" Game Over! The word was:", secret_word)


# Run the game
if _name_ == "_main_":
    hangman()

