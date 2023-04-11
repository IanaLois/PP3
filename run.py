# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import word_list

def get_new_word():
    """
    Retrieve new randomized word from imported word list
    """
    word = random.choice(word_list)
    return word.upper()

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

print("Welcome! Are you ready to play?\n")
print("Press 'R' to see game rules")
print("Press 'P' to play game\n")

print("Choose game difficulty\n")
print("Press 'E' for Easy")
print("Press 'M' for Moderate")
print("Press 'C' for Challenging")

def main():
    """
    Run all essential functions
    """