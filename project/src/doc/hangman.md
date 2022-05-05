Module hangman
==============

Functions
---------

    
`check_game_state(tries, secret_word)`
:   If the number of tries is less than 6, and all the characters in the secret word are underscores,
    then the game state is won.
    If the number of tries is equal to 6, then the game state is lost.
    Otherwise, the game state is neutral
    
    :param tries: the number of tries the player has left
    :param secret_word: the word the user is trying to guess
    :return: The game state is being returned.

    
`clear()`
:   If the operating system is Windows, clear the screen using the cls command, otherwise clear the
    screen using the clear command.

    
`exit_program()`
:   This function prints the message 'Shutting down...', then waits for 0.5 seconds
    before exiting the program.

    
`game_lost(word, tries, max_tries, hidden_word_joined, missed_characters_joined)`
:   This function prints the final state of the gameboard, the word, the number of attempts remaining,
    the missed characters, and the message "You have lost :(" and the word.
    It then asks the user if they want to play again.
    If they do, the program restarts. If they don't, the program exits.
    
    :param word: the word that the user is trying to guess
    :param tries: the number of tries the user has left
    :param max_tries: The maximum number of tries the user has to guess the word
    :param hidden_word_joined: The hidden word, but joined together with spaces in between each letter
    :param missed_characters_joined: A string of all the characters that the user has guessed incorrectly

    
`game_won(player_name, word, time_between)`
:   This function prints a message to the user that they have won the game, the word they guessed, the
    time it took them to guess the word, and then saves the score to the database
    
    :param player_name: The name of the player
    :param word: the word that the player is trying to guess
    :param time_between: This is the time it took to user to guess the word

    
`main()`
:   This function is the main function of the game. It calls all the other functions and is the main
    game loop.

    
`play_quit_highscores()`
:   It asks the user if they want to play, quit or see highscores. If they want to play, it breaks the
    loop and continues to the next function. If they want to quit, it exits the program. If they want to
    see highscores, it shows the highscores and returns to the main menu when user hits 'enter'.

    
`player_guess(tries, word, secret_word, missed_characters, hidden_word)`
:   The function takes in the number of tries, the word, the secret word, the missed characters, and the
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

    
`print_logo()`
:   It prints the logo.

    
`restart_program()`
:   It prints the text 'Restarting...', then waits for 0.5 seconds then restarts
    the program and closes previous program.

    
`time_calculator(start_time)`
:   This function takes in a start time and returns the time between the start time and the current time
    
    :param start_time: the time when the game was started
    :return: The time between the start time and the end time.

    
`username()`
:   It asks the user to input a username, and if the username is between 3 and 8 characters, it returns
    the username
    :return: The player's name

    
`welcome_message()`
:   This function prints the logo and welcome message

    
`word_choose()`
:   It opens the file, reads the lines, chooses a random line, and returns the line
    :return: A random word from the words.txt file.