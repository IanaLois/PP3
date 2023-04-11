# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import word_list

print("""
  _    _                                               
 | |  | |                                              
 | |__| |  __ _  _ __    __ _  _ __ ___    __ _  _ __  
 |  __  | / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \ 
 | |  | || (_| || | | || (_| || | | | | || (_| || | | |
 |_|  |_| \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_|
                         __/ |                         
                        |___/                          
""")

def get_new_word():
    """
    Retrieve new randomized word from imported word list
    """
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    gameover = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print(display_hangman(lives))
    print(word_completion)
    print("\n")
    while not gameover and tries > 0:
        guess = input("Enter any letter: ").upper()
        if guess.isalpha():
            if guess in guessed_letters or guess in guessed_words:
                print(f"{guess} was already used!")
            elif guess == word:
                gameover = True
                word_completion = word
            elif len(guess) == 1 and guess in word:
                print(f"Well done, {guess} is in the word!")
                guessed_letters.append(guess)
                word_completion = "".join([guess if letter == guess else word_completion[i] for i, letter in enumerate(word)])
                if "_" not in word_completion:
                    gameover = True
            else:
                print(f"{guess} is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
        else:
            print("Sorry, that\'s not a valid guess.")
        print(display_hangman(lives))
        print(word_completion)
        print("\n")
    if gameover:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you have no more lives left. The word was {word}. Better luck next time!")

print("Welcome! Are you ready to play?\n")
print("Enter 'R' to see game rules")
print("Enter 'P' to play game\n")

print("Choose game difficulty\n")
print("Enter 'E' for Easy")
print("Enter 'M' for Moderate")
print("Enter 'C' for Challenging")

def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]

def main():
    """
    Run all essential functions
    """
    word = get_new_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_new_word()
        play(word)

main()