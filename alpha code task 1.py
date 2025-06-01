import random

words = ["uday", "aman", "disha", "rohit"]
word = random.choice(words)
guessed_letters = []
tries = 2
display_word = ["_" for _ in word]

while tries > 0:
    print("Word:", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                display_word[index] = guess
        print("Good guess!")
    else:
        tries -= 1
        print(f"Wrong guess! You have {tries} tries left.")

    if "_" not in display_word:
        print("You win! The word was:", word)
        break
else:
    print("You lose! The word was:",word)