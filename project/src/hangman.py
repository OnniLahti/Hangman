import random
import os
import sys
import time
from scores import *
from gamestate import gameboard

# Function to just print the logo of the game
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

# Function to count the time elapsed between start and end of the game
def time_calculator(start_time):
    """
    This function takes in a start time and returns the time between the start time and the current time
    
    :param start_time: the time when the game was started
    :return: The time between the start time and the end time.
    """
    end_time = time.time()
    time_between = end_time - start_time
    return time_between

# Function to restart the program if user wants to play again
def restart_program():
    """
    It restarts the program by calling the python executable and passing it the current script's name
    """
    os.system("python hangman.py")
    print()
    print("  Restarting...")
    time.sleep(1)
    exit()

# Function to clear the console after every turn to make it look cleaner
def clear():
    """
    If the operating system is Windows, clear the screen using the cls command, otherwise clear the
    screen using the clear command
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to check if game has been won or lost yet
def check_game_state(tries, secret_word):
    """
    If the number of tries is less than 6, and all the characters in the secret word are underscores,
    then the game state is won.
    If the number of tries is equal to 6, then the game state is lost.
    Otherwise, the game state is neutral
    
    :param tries: the number of tries the player has left
    :param secret_word: the word the user is trying to guess
    :return: The game state is being returned.
    """
    if tries < 6:
        if all(char == '_' for char in secret_word):
            game_state = 'won'
            return game_state
    elif tries == 6:
        game_state = 'lost'
        return game_state
    else:
        game_state = 'neutral'
        return game_state

# Function to take in player guess imput and check if it hits or misses
def player_guess(tries, word, secret_word, missed_characters, hidden_word):
    """
    The function takes in the number of tries, the word, the secret word, the missed characters, and the
    hidden word. 
    It then asks the user to guess a letter or the whole word. 
    If the guess is invalid it asks again. 
    If the guess is the whole word, it replaces the secret word with underscores. 
    If the guess is a letter that is in the secret word, 
    it replaces the secret word with underscores and replaces the hidden word with the letter. 
    If the guess is a letter that is not in the secret word, it adds the letter to the missed characters 
    and adds one to the number of tries.
    
    :param tries: the number of tries the player has left
    :param word: the word that the player is trying to guess
    :param secret_word: the word that the player is trying to guess
    :param missed_characters: a list of characters that the player has guessed but are not in the secret word
    :param hidden_word: the word that is displayed to the player
    :return: The number of tries
    """
    while True:
        guess = input('  your guess: ')

        if not guess.isalpha():
            print(f'  {guess} is not a letter')

        elif guess.lower() in missed_characters or guess in hidden_word:
            print(f'  {guess} has been used already')
        
        elif len(guess) > 1 and len(guess) < len(word) or len(guess) > len(word):
            print('  Please guess with one letter or whole word')
        
        elif guess.lower() == word:

            for i in range(len(secret_word)):
                secret_word[i] = '_'
            return tries

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

# Function to tell user they have won
def game_won(player_name, word, time_between):
    """
    This function prints a message to the user that they have won the game, the word they guessed, the
    time it took them to guess the word, and then saves the score to the database
    
    :param player_name: The name of the player
    :param word: the word that the player is trying to guess
    :param time_between: This is the time it took to user to guess the word
    """
    print()
    print('  You have won :)')
    print(f'  The word was: {word}')
    print(f'  Your time was: {int(time_between)} seconds')
    print()
    save_score(word, player_name, time_between)
    while True:
        play_again = input("  Play again? 'y' for yes 'n' for no: ")

        if play_again.casefold() == 'y':
            restart_program()
        elif play_again.casefold() == 'n': 
            sys.exit()
        else:
            print('  Invalid input. Please try again')

# Function to tell user they have lost
def game_lost(word, tries, max_tries, hidden_word_joined, missed_characters_joined):
    """
    This function prints the final state of the gameboard, the word, the number of attempts remaining,
    the missed characters, and the message "You have lost :(" and the word.
    It then asks the user if they want to play again.
    If they do, the program restarts. If they don't, the program exits.
    
    :param word: the word that the user is trying to guess
    :param tries: the number of tries the user has left
    :param max_tries: The maximum number of tries the user has to guess the word
    :param hidden_word_joined: The hidden word, but joined together with spaces in between each letter
    :param missed_characters_joined: A string of all the characters that the user has guessed incorrectly
    """
    #Printing final state of gameboard for clarification
    clear()
    print(gameboard(6))
    print(f'  word: {hidden_word_joined}')
    print(f'  {max_tries - tries} attempts remaining')
    print(f'  misses: {missed_characters_joined}')
    print()
    print('  You have lost :(')
    print(f'  The word was: {word}')
    print()
    while True:
        play_again = input("  Play again? 'y' for yes 'n' for no: ")

        if play_again.casefold() == 'y':
            restart_program()
        elif play_again.casefold() == 'n':
            sys.exit()
        else:
            print('  Invalid input. Please try again \n')

# Function to ask user for username
def username():
    """
    It asks the user to input a username, and if the username is between 3 and 8 characters, it returns
    the username
    :return: The player's name
    """
    print_logo()
    while True:
        player_name = input('  Enter username (min 3, max 8 characters): ')

        if len(str(player_name)) <= 8 and len(str(player_name)) >= 3:
            break
        else:
            print('  Invalid name')
    return player_name

# Function to choose random word to be guessed
def word_choose():
    """
    It opens the file, reads the lines, chooses a random line, and returns the line
    :return: A random word from the words.txt file.
    """
    with open('words/words.txt') as f:
        lines = f.readlines()
        word = random.choice(lines).strip()
    return word

# Function to print welcome message and logo
def welcome_message():
    """
    This function prints the logo and welcome message
    """
    clear()
    print_logo()
    print('  WELCOME TO HANGMAN!')

# Function to ask if user wants to play/quit/see highscores
def play_quit_highscores():
    """
    It asks the user if they want to play, quit or see highscores. If they want to play, it breaks the
    loop and continues to the next function. If they want to quit, it exits the program. If they want to
    see highscores, it shows the highscores and returns to the main menu when user hits 'enter'.
    """
    print('  Do you want to play, quit or see highscores? \n')
    while True:
        what_to_do = input("  'p' to play, 'q' to quit and 'h' to see highscores: ")
        clear()
        if what_to_do.casefold() == 'p':
            break
        elif what_to_do.casefold() == 'q':
            sys.exit()
        elif what_to_do.casefold() == 'h':
            show_scores()
            print()
            input("  Press Enter to return...")
            main()
        else:
            print_logo()
            print('  Invalid input. Please try again')

# Main game loop
def main():
    """
    This function is the main function of the game. It calls all the other functions and is the main
    game loop.
    """

    welcome_message()
    play_quit_highscores()

    #Defining variables
    tries = 0
    max_tries = 6
    missed_characters = []
    hidden_word = []
    word = word_choose()
    player_name = username()

    # Starting the timer
    start_time = time.time()

    # Converting the string word into a list of characters.
    secret_word = list(word)

# Appending an underscore to the list hidden_word for every character in the secret_word.
    for item in secret_word:
        hidden_word.append('_')

# This is the main game loop. It prints the gameboard, the word, the number of attempts remaining,
# the missed characters, and then calls the player_guess function. It then checks if the game has been
# won or lost, and if it has, it calls the game_won or game_lost function. If the game has not been won or
# lost, it continues the loop.
    while True:
        missed_characters_joined = ','.join(missed_characters)
        hidden_word_joined = ' '.join(hidden_word)
        clear()
        print(gameboard(tries))
        print(f'  word: {hidden_word_joined}')
        print(f'  {max_tries - tries} attempts remaining')
        print(f'  misses: {missed_characters_joined}')
        tries = player_guess(tries, word, secret_word, missed_characters, hidden_word)
        game_state = check_game_state(tries, secret_word)
        if game_state == 'neutral':
            pass
        elif game_state == 'won':
            time_between = time_calculator(start_time)
            game_won(player_name, word, time_between)
        elif game_state == 'lost':
            game_lost(word, tries, max_tries, hidden_word_joined, missed_characters_joined)

# A way to make sure that the code in the if statement is only executed if the script is run directly,
# and not imported.
if __name__ == "__main__":
    main()