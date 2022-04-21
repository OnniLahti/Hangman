import random
import os
import sys

with open('words/words.txt') as f:
    lines = f.readlines()
    word = random.choice(lines)

secret_word = list(word)
secret_word = secret_word[:-1]
hidden_word = []
for item in secret_word:
    hidden_word.append('_')
tries = 0
max_tries = 6
missed_characters = []


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
   _________|___________________
  /         |                 /|
 /                           / |
/_ _________________________/  /
|                           | /
|--------------------------- /
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
   _________|___________________
  /         |                 /|
 /                           / |
/_ _________________________/  /
|                           | /
|--------------------------- /
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
   _________|___________________
  /         |                 /|
 /                           / |
/_ _________________________/  /
|                           | /
|--------------------------- /
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
   _________|___________________
  /         |                 /|
 /                           / |
/_ _________________________/  /
|                           | /
|--------------------------- /
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
   _________|___________________
  /         |                 /|
 /                           / |
/_ _________________________/  /
|                           | /
|--------------------------- /
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
   _________|___________________
  /         |                 /|
 /                           / |
/_ _________________________/  /
|                           | /
|--------------------------- /
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
   _________|___________________
  /         |                 /|
 /                           / |
/_ _________________________/  /
|                           | /
|--------------------------- /
    """

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_win(tries):
    if tries < 6:
        if all(char == '_' for char in secret_word):
            game_over('won')

    elif tries == 6:
        game_over('lost')

def player_guess(tries):
    guess = input('your guess: ')
    if guess in secret_word:
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

def game_over(state):
    if state == 'won':
        print()
        print('You have won :)')
        print(f'The word was: {word}')
        print()
        while True:
            play_again= input("Play again? 'y' for yes 'n' for no: ")

            if play_again == 'y':
                restart_program()
            elif play_again == 'n':
                sys.exit()
            else:
                print('Invalid input. Please try again')

    elif state == 'lost':
        print()
        print('You have lost :(')
        print(f'The word was: {word}')
        print()
        while True:
            play_again= input("Play again? 'y' for yes 'n' for no: ")

            if play_again == 'y':
                restart_program()
            elif play_again == 'n':
                sys.exit()
            else:
                print('Invalid input. Please try again')


while True:
    missed_characters_joined = ','.join(missed_characters)
    hidden_word_joined = ' '.join(hidden_word)
    clear()
    print(gameboard(tries))
    print(f'word: {hidden_word_joined}')
    print(f'{max_tries - tries} attempts remaining')
    print(f'misses: {missed_characters_joined}')
    tries = player_guess(tries)
    check_win(tries)



