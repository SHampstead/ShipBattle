from Classes_SB import *
from sys import exit

print("Hello and welcome to Ship Battle.")
players = input("Are there two palyers? ")
if "y" in players.lower():
    print("Great! lets begin!")
else:
    print("Please get another player!")
    exit()

player1_name = input("Player 1, what is your name? ")
player2_name = input("Player 2, what is your name? ")


