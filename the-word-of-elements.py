## The World of Elements v1.0
## Authors: BlazeSlayer1234, WiredDude73
## nogui branch

import sys
import random
import os
import time
import pickle


# check if game data file exists before asking user all their info, right now we don't do anything with the value.
SaveFilePresent =  os.path.isfile("save.dat")

Players = [
 {'Name':'Korto','Strength': 75, 'Speed': 56, 'Magic': 27, 'Dexterity': 89 },
 {'Name':'Tom','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29 } ,
 {'Name':'Jack','Strength': 15, 'Speed': 96, 'Magic': 57, 'Dexterity': 57 },
 {'Name':'Nathaniel','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29 },
 {'Name':'David','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29 },
 {'Name':'Jerry','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29 },
 {'Name':'Noah','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29 },
 {'Name':'Jordan','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29 } ]


# Get the Time, Define the Players
Time = time.asctime()
# Players=[Tom, Korto, Jack, Nathaniel, David, Jerry, Noah, Jordan]
NumPlayers = len (Players) -1
Monsters=['Creeper','Enderman', 'Killer Squid', 'Fire Dragon','Killer Kitty','Jerry The Monster', 'Larry the Killer Bug', 'Baby Monster Dragon', 'Zombie']


# Define Weapons

Weapons=['Simple Sword', 'First Shotgun', 'Stop Shield', 'Hand and half sword', 'Laser Gun', 'Forcefield']
random.shuffle(Weapons)
PlayerWeapon=Weapons[0]

# Create a 100x100 World

World=((350,350))

# Introduce the user to the game

os.system('clear')

print("Welcome to the World of Elements! Enter if you Dare! This Game was Created by BlazeSlayer1234 and Wireddude73 \n")
print("Here are a list of possible players to choose from:")
for x in range (0, NumPlayers):
	print ('%s-%s' % (x,Players[x]['Name']))
print ("\nPlease choose a number for your player:")
PlayerNameChoice =  int(sys.stdin.readline())
PlayerName = Players[PlayerNameChoice]

print ('Hi there %s, you\'ve been assigned a %s as your weapon!' % (PlayerName, PlayerWeapon))

## stop here to save game status
game_data = {'time': Time, 'player-position' : 'N23 E25', 'pockets' : PlayerWeapon, 'player-name' : PlayerName , 'gold' : 158.50 }
save_file = open ('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()


