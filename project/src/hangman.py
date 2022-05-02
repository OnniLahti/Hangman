import random
import os
import sys
import time

with open('words/words.txt') as f:
    lines = f.readlines()
    word = random.choice(lines).strip()

secret_word = list(word)

hidden_word = []
for item in secret_word:
    hidden_word.append('_')

tries = 0
max_tries = 6
missed_characters = []
end_time = 0
time_between = 0
start_time = 0
player_name = ''
seconds = 0
game_active = False

#Function to just print the logo of the game
def print_logo():
    print("""
[]    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
[]    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
[][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
[]    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
[]    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]
\n""")

#Function to print the time elapsed
def timer(time_between):
    global seconds
    seconds = time_between
    print(f'Your time was: {int(seconds)} seconds')

#Function to count the time elapsed between start and end of the game
def time_calculator():
    global end_time
    global time_between
    global start_time
    end_time = time.time()
    time_between = end_time - start_time

#Function that stores the different states of gamein strings made from ASCII characters
def gameboard(tries):
    match tries:

        case 0:
            return """
[]    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
[]    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
[][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
[]    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
[]    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

            ___________
            |         |
            |         |
            |
            |
            |
            |
            |
   _________|__________________
  /         |                 /|
 /                           / |
/___________________________/  /
|                           | /
|___________________________|/
"""

        case 1:
            return """
[]    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
[]    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
[][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
[]    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
[]    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

            ___________
            |         |
            |         |
            |         @
            |
            |
            |
            |
   _________|__________________
  /         |                 /|
 /                           / |
/___________________________/  /
|                           | /
|___________________________|/
"""

        case 2:
            return """
[]    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
[]    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
[][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
[]    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
[]    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

            ___________
            |         |
            |         |
            |         @
            |         |
            |         |
            |
            |
   _________|__________________
  /         |                 /|
 /                           / |
/___________________________/  /
|                           | /
|___________________________|/
"""

        case 3:
            return """
[]    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
[]    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
[][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
[]    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
[]    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

            ___________
            |         |
            |         |
            |         @
            |        /|
            |         |
            |
            |
   _________|__________________
  /         |                 /|
 /                           / |
/___________________________/  /
|                           | /
|___________________________|/
"""

        case 4:
            return """
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
            |
            |
   _________|__________________
  /         |                 /|
 /                           / |
/___________________________/  /
|                           | /
|___________________________|/
"""

        case 5:
            return """
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
            |        /
            |
   _________|__________________
  /         |                 /|
 /                           / |
/___________________________/  /
|                           | /
|___________________________|/
    """

        case 6: """
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
"""

#Function to restart the program if user wants to play again
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Function to clear the console after every turn to make it look cleaner
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Function to check if game has been won or lost yet
def check_game_state(tries):
    if tries < 6:
        if all(char == '_' for char in secret_word):
            time_calculator()
            game_over('won')
    elif tries == 6:
        game_over('lost')

#Function to take in player guess imput and check if it hits or misses
def player_guess(tries):
    while game_active:
        guess = input('your guess: ')

        if not guess.isalpha():
            print(f'{guess} is not a letter')

        elif guess in missed_characters or guess in hidden_word:
            print(f'{guess} has been used already')
        
        elif len(guess) > 1 and len(guess) < len(word) or len(guess) > len(word):
            print('Please guess with one letter or whole word')
        
        elif guess == word:
            game_over('won')

        elif guess in secret_word:
            for i in range(len(secret_word)):
                char = secret_word[i]
                if char == guess:
                    hidden_word[i] = secret_word[i]
                    secret_word[i] = '_'
            return tries

        else:
            missed_characters.append(guess)
            tries += 1
            return tries

#Function to print the end game screen and ask user to play again
def game_over(state):
    if state == 'won':
        print()
        print('You have won :)')
        print(f'The word was: {word}')
        timer(time_between)
        print()
        save_score()
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

#Saves the users username and score to txt file and arranges the text file and deletes others than top 3
def save_score():
    
    with open(f'highscores/{word}.txt', 'a+') as f:
        f.write(f'\n{player_name}, {int(seconds)}')
        
    with open(f'highscores/{word}.txt') as f:
        scores = [tuple(line.split()) for line in f]

    #Sorting the scores highest to lowest
    try:
        scores.sort(key = lambda scores: int(scores[1]))
    except IndexError:
        pass

    #Declaring new list of top 3 scores that will overwrite the old list
    new_scores = list()

    #Iterating through the original list and appending the top 3 items in that list to the new list
    try:
        for i in range(3):
            new_scores.append(scores[i])
    except IndexError:
        pass

    #Writing over the old list with the new list
    with open(f'highscores/{word}.txt', 'w') as f:
        try:
            f.write("\n".join("%s %s" % score for score in new_scores))
        except TypeError:
            f.write(str(' '.join(new_scores[1])))



#Prints the top 3 scores of all words
def show_scores():
    if os.path.exists('highscores/cat.txt'):
        with open('highscores/cat.txt') as f:
            scores_cat = [tuple(line.split()) for line in f]
            print('----------------------------')
            print('Word: Cat')
            for i in scores_cat:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------')
            f.close()
    else:
        print('----------------------------------------')
        print(f'No scores saved for word: "Cat" yet')
        print('----------------------------------------')

    if os.path.exists('highscores/fox.txt'):
        with open('highscores/fox.txt') as f:
            scores_fox = [tuple(line.split()) for line in f]
            print('Word: Fox')
            for i in scores_fox:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------')
            f.close()
    else:
        print('----------------------------------------')
        print(f'No scores saved for word: "Fox" yet')
        print('----------------------------------------')

    if os.path.exists('highscores/bear.txt'):
        with open('highscores/bear.txt') as f:
            scores_bear = [tuple(line.split()) for line in f]
            print('Word: Bear')
            for i in scores_bear:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------')
            f.close()
    else:
        print('----------------------------------------')
        print(f'No scores saved for word: "Bear" yet')
        print('----------------------------------------')

    if os.path.exists('highscores/shark.txt'):
        with open('highscores/shark.txt') as f:
            scores_shark = [tuple(line.split()) for line in f]
            print('Word: Shark')
            for i in scores_shark:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------')
            f.close()
    else:
        print('----------------------------------------')
        print(f'No scores saved for word: "Shark" yet')
        print('----------------------------------------')

    if os.path.exists('highscores/raccoon.txt'):
        with open('highscores/raccoon.txt') as f:
            scores_raccoon = [tuple(line.split()) for line in f]
            print('Word: Raccoon')
            for i in scores_raccoon:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------')
            f.close()
    else:
        print('----------------------------------------')
        print(f'No scores saved for word: "Raccoon" yet')
        print('----------------------------------------')

#Printing logo and welcome message
clear()
print()
print_logo()
print('WELCOME TO HANGMAN!')

#Ask user to play, see highscores or quit
print('Do you want to play, see highscores or quit? \n')
while True:
    what_to_do = input("'p' to play, 'h' to see highscores and q to quit: ")
    clear()

    if what_to_do.casefold() == 'p':
        break
    elif what_to_do.casefold() == 'h':
        show_scores()
    elif what_to_do.casefold() == 'q':
        sys.exit()
    else:
        print()
        print_logo()
        print('Invalid input. Please try again')

#Printing the logo
print_logo()

#Asking for username loop
while True:

    player_name = input('Enter username (min 3, max 8 characters): ')

    if len(str(player_name)) <= 8 and len(str(player_name)) >= 3:
        break
    else:
        print('Invalid name')

#starts the game and timer
game_active = True
start_time = time.time()

#The game loop itself
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