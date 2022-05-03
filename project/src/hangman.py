import random
import os
import sys
import time
from ASCII import gameboard
from scores import *

tries = 0
max_tries = 6
missed_characters = []
end_time = 0
time_between = 0
start_time = 0
player_name = ''
seconds = 0
game_active = False

# It opens the file words.txt and reads all the lines in the file. It then chooses a random word from
# the list of words.
with open('words/words.txt') as f:
    lines = f.readlines()
    word = random.choice(lines).strip()

# Converting the string word into a list of characters.
secret_word = list(word)

# Creating a list of underscores that is the same length as the secret word.
hidden_word = []
for item in secret_word:
    hidden_word.append('_')

#Function to just print the logo of the game
def print_logo():
    """
    It prints the logo.
    """
    print("""
[]    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
[]    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
[][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
[]    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
[]    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]
\n""")

#Function to print the time elapsed
def timer(time_between):
    """
    The function timer takes in a parameter time_between and sets the global variable seconds to the
    value of time_between
    
    :param time_between: The time between start_time and end_time
    """
    global seconds
    seconds = time_between
    print(f'Your time was: {int(seconds)} seconds')

#Function to count the time elapsed between start and end of the game
def time_calculator():
    """
    This function calculates the time between the start and end of the program
    """
    global time_between
    end_time = time.time()
    time_between = end_time - start_time

#Function to restart the program if user wants to play again
def restart_program():
    """
    It restarts the program by calling the python executable and passing it the current script's name
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Function to clear the console after every turn to make it look cleaner
def clear():
    """
    If the operating system is Windows, clear the screen using the cls command, otherwise clear the
    screen using the clear command
    """
    os.system('cls' if os.name == 'nt' else 'clear')

#Function to check if game has been won or lost yet
def check_game_state(tries):
    """
    If the player has used less than 6 tries, check if all the characters in the secret word are guessed. If
    they are, the player has won. If the player has used all 6 tries, the player has lost
    
    :param tries: the number of tries the player has used
    """
    if tries < 6:
        if all(char == '_' for char in secret_word):
            time_calculator()
            game_over('won')
    elif tries == 6:
        game_over('lost')

#Function to take in player guess imput and check if it hits or misses
def player_guess(tries):
    """
    The function takes in the number of tries as an argument and returns the number of tries after the
    player has guessed
    
    :param tries: the number of tries the player has used
    :return: The number of tries
    """
    while game_active:
        guess = input('your guess: ')

        if not guess.isalpha():
            print(f'{guess} is not a letter')

        elif guess.lower() in missed_characters or guess in hidden_word:
            print(f'{guess} has been used already')
        
        elif len(guess) > 1 and len(guess) < len(word) or len(guess) > len(word):
            print('Please guess with one letter or whole word')
        
        elif guess.lower() == word:
            time_calculator()
            game_over('won')

        elif guess.lower() in secret_word:
            for i in range(len(secret_word)):
                char = secret_word[i]
                if char == guess.lower():
                    hidden_word[i] = secret_word[i]
                    secret_word[i] = '_'
            return tries

        else:
            missed_characters.append(guess)
            tries += 1
            return tries

#Function to print the end game screen and ask user to play again
def game_over(state):
    """
    If the game is won, print a congratulations and time, save the score, and ask the player if they want to play again. 
    If the game is lost, print a gameboard, and ask the player if they want to play again.
    
    :param state: 'won' or 'lost'
    """
    if state == 'won':
        print()
        print('You have won :)')
        print(f'The word was: {word}')
        timer(time_between)
        print()
        save_score(word, player_name, seconds)
        while True:
            play_again = input("Play again? 'y' for yes 'n' for no: ")

            if play_again.casefold() == 'y':
                restart_program()
            elif play_again.casefold() == 'n': 
                sys.exit()
            else:
                print('Invalid input. Please try again')

    elif state == 'lost':
        #Printing final state of gameboard for clarification
        clear()
        print("""
    []    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
    []    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
    [][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
    []    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
    []    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

            ___________
            |         |
            |         |
            |         @
            |        /|\\
            |         |
            |        / \\
            |
   _________|__________________
  /         |                 /|
 /                           / |
/___________________________/  /
|                           | /
|___________________________|/
    """)
        print(f'word: {hidden_word_joined}')
        print(f'{max_tries - tries} attempts remaining')
        print(f'misses: {missed_characters_joined}')
        print()
        print('You have lost :(')
        print(f'The word was: {word}')
        print()
        while True:
            play_again = input("Play again? 'y' for yes 'n' for no: ")

            if play_again.casefold() == 'y':
                restart_program()
            elif play_again.casefold() == 'n':
                sys.exit()
            else:
                print('Invalid input. Please try again \n')

#Prints logo and welcome message
clear()
print()
print_logo()
print('WELCOME TO HANGMAN!')

# Asking the user if they want to play, quit or see highscores. If the user inputs 'p', the program
# will break out of the loop and continue. If the user inputs 'q', the program will exit. If the user
# inputs 'h', the program will show the highscores. If the user inputs anything else, the program will
# print the logo and ask the user to try again.
print('Do you want to play, quit or see highscores? \n')
while True:
    what_to_do = input("'p' to play, 'q' to quit and 'h' to see highscores: ")
    clear()

    if what_to_do.casefold() == 'p':
        break
    elif what_to_do.casefold() == 'q':
        sys.exit()
    elif what_to_do.casefold() == 'h':
        show_scores()
    else:
        print()
        print_logo()
        print('Invalid input. Please try again')

#Prints the logo
print_logo()

# This is a while loop that asks the user for a username. The username has to be between 3 and 8
# characters. If the username is not between 3 and 8 characters, the user will be asked to try again.
while True:

    player_name = input('Enter username (min 3, max 8 characters): ')

    if len(str(player_name)) <= 8 and len(str(player_name)) >= 3:
        break
    else:
        print('Invalid name')

# It starts the game and timer
game_active = True
start_time = time.time()

# This is the main game loop. It prints the gameboard, the hidden word, the number of tries remaining, the
# missed characters and calls the player_guess function.
while game_active:
    missed_characters_joined = ','.join(missed_characters)
    hidden_word_joined = ' '.join(hidden_word)
    clear()
    print(gameboard(tries))
    print(f'word: {hidden_word_joined}')
    print(f'{max_tries - tries} attempts remaining')
    print(f'misses: {missed_characters_joined}')
    tries = player_guess(tries)
    check_game_state(tries)