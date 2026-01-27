import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
print("Welcome to Hangman!")

chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for index in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'.")
        continue
    display =""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("*************** !!! YOU LOSE !!! ***************")
    if "_" not in display:
        game_over = True
        print("*************** !!! YOU WIN !!! ***************")
    print(f"************* {lives} / 6 LIVES REMAINING ************")
    print(stages[lives])
