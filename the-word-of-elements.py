## The World of Elements v1.0
## Authors: BlazeSlayer1234, WiredDude73


import sys
import random
import os
import pygame
import time
import pickle
from pygame.locals import *

# check if game data file exists before asking user all their info, right now we don't do anything with the value.
SaveFilePresent =  os.path.isfile("save.dat")

# Get the Time, Define the Players
Time = time.asctime()
Players=['Tom','Korto', 'Jack', 'Nathaniel','David the Wimpy Kid','Jerry The Warrier', 'Noah', 'Jordan', 'David the Great']
NumPlayers = len (Players)

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
	print ('%s-%s' % (x,Players[x]))
print ("\nPlease choose a number for your player:")
PlayerNameChoice =  int(sys.stdin.readline())
PlayerName = Players[PlayerNameChoice]

print ('Hi there %s, you\'ve been assigned a %s as your weapon!' % (PlayerName, PlayerWeapon))

## stop here to save game status
game_data = {'time': Time, 'player-position' : 'N23 E25', 'pockets' : PlayerWeapon, 'player-name' : PlayerName , 'gold' : 158.50 }
save_file = open ('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()


## initialize graphics stuff

pygame.init()
DISPLAYSURF=pygame.display.set_mode((400,400))
FPS=30
fpsClock = pygame.time.Clock()
catImg = pygame.image.load('cat.png')
catx=40
caty=40
direction='right'
RED = (200,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)


fontObj = pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj= fontObj.render('Beware of the Kitty!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)


# tried to draw a pixel here but causes a seg fault 11 on OSX. 
# pixObj = pygame.PixelArray(DISPLAYSURF) 






pygame.display.set_caption('The World Of Elements')

## the main while loop for the game

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	pygame.draw.rect(DISPLAYSURF, GREEN, (20,20,350,350))
	
	if direction == 'right':
		catx +=5
		if catx == 250:
			direction='down'
	elif direction == 'down':
		caty +=5
		if caty == 250:
			direction='left'
	elif direction == 'left':
		catx-=5
		if catx == 40:
			direction = 'up'
	elif direction  == 'up':
		caty-=5
		if caty == 40:
			direction='right'

	DISPLAYSURF.blit(catImg, (catx, caty))
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)


#	pixObj[480][380] = BLACK
	
