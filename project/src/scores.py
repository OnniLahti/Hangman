import os

#Saves the users username and score to txt file and arranges the text file and deletes others than top 3
def save_score(word, player_name, seconds):
    """
    The function takes in a word, player name, and the time it took to quess the word. It then opens
    the file for the word and appends the player name and time to the end of the file. It then reads the
    file and creates a list of tuples with the player name and time. It then sorts the list by the time
    and creates a new list with the top 3 scores. It then writes over the old file with the new list.
    
    :param word: The word that the player is trying to guess
    :param player_name: The username of the player
    :param seconds: The time it took the player to quess the word
    """
    with open(f'highscores/{word}.txt', 'a+') as f:
        f.write(f'\n{player_name}, {int(seconds)}')
        
    with open(f'highscores/{word}.txt') as f:
        scores = [tuple(line.split()) for line in f]

    #Sorting the scores highest to lowest / if there is no scores, pass
    try:
        scores.sort(key = lambda scores: int(scores[1]))
    except IndexError:
        pass

    #Declaring new list of top 3 scores that will overwrite the old list
    new_scores = list()

    #Iterating through the original list and appending the top 3 items in that list to the new list
    # if there is not 3 items in the list then stop and pass where the list ends
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
    """
    This function opens the highscore files for each word, and prints the scores in a readable format.
    """
    try:
        with open('highscores/bear.txt', 'x+') as f:
            scores_bear = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Bear"')
            print()
            for i in scores_bear:
                print(f"         {' '.join(map(str,i))} seconds")
    except FileExistsError:
        with open('highscores/bear.txt') as f:
            scores_bear = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Bear"')
            print()
            for i in scores_bear:
                print(f"         {' '.join(map(str,i))} seconds")

    try:
        with open('highscores/fox.txt', 'x+') as f:
            scores_fox = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Fox"')
            print()
            for i in scores_fox:
                print(f"        {' '.join(map(str,i))} seconds")
    except FileExistsError:
        with open('highscores/fox.txt') as f:
            scores_fox = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Fox"')
            print()
            for i in scores_fox:
                print(f"         {' '.join(map(str,i))} seconds")
    try:
        with open('highscores/groundhog.txt', 'x+') as f:
            scores_groundhog = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Groundhog"')
            print()
            for i in scores_groundhog:
                print(f"         {' '.join(map(str,i))} seconds")
    except FileExistsError:
        with open('highscores/groundhog.txt') as f:
            scores_groundhog = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Groundhog"')
            print()
            for i in scores_groundhog:
                print(f"         {' '.join(map(str,i))} seconds")

    try:
        with open('highscores/puffin.txt', 'x+') as f:
            scores_puffin = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Puffin"')
            print()
            for i in scores_puffin:
                print(f"        {' '.join(map(str,i))} seconds")
    except FileExistsError:
        with open('highscores/puffin.txt') as f:
            scores_puffin = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Puffin"')
            print()
            for i in scores_puffin:
                print(f"         {' '.join(map(str,i))} seconds")

    try:
        with open('highscores/raccoon.txt', 'x+') as f:
            scores_raccoon = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Raccoon"')
            print()
            for i in scores_raccoon:
                print(f"         {' '.join(map(str,i))} seconds")
            print('  ----------------------------------------')
    except FileExistsError:
        with open('highscores/raccoon.txt') as f:
            scores_raccoon = [tuple(line.split()) for line in f]
            print('  ----------------------------------------')
            print('  Word: "Raccoon"')
            print()
            for i in scores_raccoon:
                print(f"       {' '.join(map(str,i))} seconds")
            print('  ----------------------------------------')