import os

#Saves the users username and score to txt file and arranges the text file and deletes others than top 3
def save_score(word, player_name, seconds):
    
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

    if os.path.exists('highscores/bear.txt'):
        with open('highscores/bear.txt') as f:
            scores_bear = [tuple(line.split()) for line in f]
            print('----------------------------------------')
            print('Word: "Bear"')
            print()
            for i in scores_bear:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------------------')

    if os.path.exists('highscores/fox.txt'):
        with open('highscores/fox.txt') as f:
            scores_fox = [tuple(line.split()) for line in f]
            print('----------------------------------------')
            print('Word: "Fox"')
            print()
            for i in scores_fox:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------------------')

    if os.path.exists('highscores/groundhog.txt'):
        with open('highscores/groundhog.txt') as f:
            scores_groundhog = [tuple(line.split()) for line in f]
            print('----------------------------------------')
            print('Word: "Groundhog"')
            print()
            for i in scores_groundhog:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------------------')

    if os.path.exists('highscores/puffin.txt'):
        with open('highscores/puffin.txt') as f:
            scores_puffin = [tuple(line.split()) for line in f]
            print('----------------------------------------')
            print('Word: "Puffin"')
            print()
            for i in scores_puffin:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------------------')

    if os.path.exists('highscores/raccoon.txt'):
        with open('highscores/raccoon.txt') as f:
            scores_raccoon = [tuple(line.split()) for line in f]
            print('----------------------------------------')
            print('Word: "Raccoon"')
            print()
            for i in scores_raccoon:
                print(f"        {' '.join(map(str,i))} seconds")
            print('----------------------------------------')