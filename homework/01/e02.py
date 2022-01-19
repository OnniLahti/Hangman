#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Luodaan kilpikonna

import turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

# Tulosta ruudulle seuraavat tekstit
print("Mihin suuntaan haluat siirtää kilpikonnaa?")
print("Kirjoita oikea tai vasen")

# Ota käyttäjän syöte vastaan
suunta = input()

# Jos käyttäjän syöte oli "oikea", liiku oikealle. 
if suunta == "oikea":
    kilpikonna.forward(50)

# Jos käyttäjän syöte oli "vasen", liiku vasemmalle.
if suunta == "vasen":
    kilpikonna.left(180)
    kilpikonna.forward(50)

if suunta == "ylÖs":
    kilpikonna.left(90)
    kilpikonna.forward(50)

if suunta == "alas":
    kilpikonna.right(90)
    kilpikonna.forward(50)