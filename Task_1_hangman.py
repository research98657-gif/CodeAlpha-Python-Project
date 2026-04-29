import random

# Step 1: word list
words = ["apple", "mango", "grapes", "peach", "banana"]

# Step 2: random word choose
word = random.choice(words)

# Step 3: empty display
guessed_word = ["_"] * len(word)

# Step 4: attempts
attempts = 6

print("Welcome to Hangman Game!")

# Step 5: game loop
while attempts > 0:
    print("\nWord:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    # check if guess correct
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    # check win
    if "_" not in guessed_word:
        print("\n You Win! The word was:", word)
        break

# check lose
if "_" in guessed_word:
    print("\n You Lost! The word was:", word)