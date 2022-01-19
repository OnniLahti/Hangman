# Luodaan kilpikonna
import turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

sade = 10
while sade < 100:
    kilpikonna.circle(sade)
    sade = sade + 5 #ympyröiden määrä tuplaantui automaattisesti, kun vain muutti sädettä kasvamaan sen 5 pikseliä kerralla.