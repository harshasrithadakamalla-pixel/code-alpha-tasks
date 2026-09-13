import random

# List of 5 predefined words
words = ["apple", "computer", "python", "college", "hangman"]

# Select a random word
word = random.choice(words)

guessed_word = ["_"] * len(word)
guessed_letters = []
wrong_guesses = 0

print("=================================")
print("          HANGMAN GAME")
print("=================================")

while wrong_guesses < 6 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", 6 - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check whether input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! 🎉")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)