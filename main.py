from os import system
import signal
import random
from hang_art import stages, logo
from hang_words import word_list

def handler(signum, frame):
    system("cls")
    exit(1)
signal.signal(signal.SIGINT, handler)

display = []
chosen_word = random.choice(word_list)
for _ in chosen_word: display += "_"

def play_game():
    print(logo)
    lives = len(stages) - 1
    guessed_letters = []
    while "_" in display and lives > 0:
        print(f"{' '.join(display)}\n")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'!")
        elif not is_guess_correct(guess, chosen_word):
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")
            lives -= 1
            
        guessed_letters.append(guess)
        print(stages[lives])
        
    handle_result(lives)
    
def is_guess_correct(guess, chosen_word):
    correct_guess = False
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            correct_guess = True
    return correct_guess

def handle_result(lives):
    if not lives: print("You lose.")
    else: print("You won!")
    print(f"The word is: {chosen_word}!")

play_game()

