import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6  # Add lives for incorrect guesses

    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left and have used these letters: ', ' '.join(used_letters))
        print('Current word: ', ' '.join([letter if letter in used_letters else '-' for letter in word]))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print(f'You died, sorry. The word was {word}')
    else:
        print(f'Yay! You guessed the word {word}!')

if __name__ == "__main__":
    hangman()
