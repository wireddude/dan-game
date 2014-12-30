import sys
import random
import os

# Define the Players

Players=['Tom','Korto', 'Jack', 'Nathaniel','David','Jerry The Warrier', 'Noah', 'Jordan']
NumPlayers = len (Players)

# Define Weapons

Weapons=['Simple Sword', 'First Shotgun', 'Stop Shield', 'Hand and half sword', 'Laser Gun', 'Forcefield']
NumWeapons = len (Weapons)
PlayerWeapon = random.randint(0,NumWeapons)

# Create a 100x100 World

World=((200,200))

# Introduce the user to the game

os.system('clear')

print("Welcome to the World of Elements! Enter if you Dare! This Game was Created by BlazeSlayer1234 and Wireddude73 \n")

print("Here are a list of possible players to choose from:")
for x in range (0, NumPlayers):
	print ('%s-%s' % (x,Players[x]))
print ("\nPlease choose a number for your player:")

PlayerName =  int(sys.stdin.readline())

print ('Hi there %s, you\'ve been assigned a %s as your weapon!' % (Players[PlayerName], Weapons[PlayerWeapon]))



