import random
import logging

# Setup logging
logging.basicConfig(filename='hangman_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Word list
WORDS = ["python", "developer", "hangman", "adventure", "algorithm", "interface", "function"]

def choose_word():
    return random.choice(WORDS).lower()

def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

def play_game():
    word = choose_word()
    guessed = set()
    attempts = 6

    logging.info(f"New game started. Word to guess: {word}")

    print("\n🎯 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed)}")
        print(f"Guessed letters: {', '.join(sorted(guessed)) if guessed else 'None'}")
        print(f"Attempts remaining: {attempts}")

        guess = input("Enter a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("✅ Good guess!")
            if all(letter in guessed for letter in word):
                print(f"\n🎉 Congratulations! You guessed the word: {word}")
                logging.info(f"Player won. Word: {word}")
                break
        else:
            print("❌ Wrong guess.")
            attempts -= 1

    else:
        print(f"\n💀 Out of attempts! The word was: {word}")
        logging.info(f"Player lost. Word: {word}")

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if replay != 'yes':
            print("Thanks for playing Hangman! 🎮")
            break

if __name__ == "__main__":
    main()
