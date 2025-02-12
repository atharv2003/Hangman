import random
import hangman_words
import hangman_art

print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)


lives = 6
placeholder = ["_"] * len(chosen_word)
guessed_letters = set()

while "_" in placeholder and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed '{guess}'. Try a different letter.")
        continue
    guessed_letters.add(guess)
    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                placeholder[index] = guess
    else:
        lives -= 1
        print(f"Wrong guess! '{guess}' is not in word\n"
              f"You have {lives} lives left.")
    print(hangman_art.stages[lives])
    print(" ".join(placeholder))


if "_" not in placeholder:
    print("Congratulations! 😎 You guessed the word!")
else:
    print(f"You lost! 😣 The word was '{chosen_word}'.")
