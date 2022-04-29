import random
import os


with open('highscores/shark.txt') as f:
    try:
        scores = [tuple(line.split()) for line in f]
    except IndexError:
        scores = (tuple(line.split()) in f)

print(scores)

scores = str(scores)
scores.strip('[]')

print(scores)