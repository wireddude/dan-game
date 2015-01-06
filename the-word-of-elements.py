# The Game of Elements v1.0
# Authors: BlazeSlayer1234, WiredDude73
# nogui branch

# see http://inventwithpython.com/pygcurse/tutorial/ for more info


import sys
import random
import os
import time
import pickle
import pygcurse

win = pygcurse.PygcurseWindow(80, 50, 'The World Of Elements')
print = win.pygprint
input = win.input
win.setscreencolors('green', 'black', clear=True)


# Define the Players, Monsters, Weapons (later, move all this to a config file)
hitpoints = 10
increment = 9

# time check
Time = time.asctime()
# check if game data file exists before asking user all their info, right now we don't do anything with the value.
SaveFilePresent =  os.path.isfile("save.dat")

  
Players = [
     {'Name':'Kuruto','Strength': 75, 'Speed': 56, 'Magic': 27, 'Dexterity': 89, 'Gold Coins': 100, 'Hit Points': hitpoints },
     {'Name':'Tom','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29, 'Gold Coins': 100, 'Hit Points': hitpoints } ,
     {'Name':'Jack','Strength': 15, 'Speed': 96, 'Magic': 57, 'Dexterity': 57, 'Gold Coins': 100 , 'Hit Points': hitpoints},
     {'Name':'Nathaniel','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 9, 'Gold Coins': 100, 'Hit Points': hitpoints },
     {'Name':'Kibou','Strength': 290, 'Speed':290, 'Magic':30,'Dexterity': 10, 'Gold Coins': 50 , 'Hit Points': hitpoints } ,
     {'Name':'David the Wimp','Strength': 3, 'Speed': 21, 'Magic': 60, 'Dexterity': 39, 'Gold Coins': 100, 'Hit Points': hitpoints },
     {'Name':'Jerry','Strength': 2, 'Speed': 91, 'Magic': 70, 'Dexterity': 49, 'Gold Coins': 100, 'Hit Points': hitpoints },
     {'Name':'Noah','Strength': 100, 'Speed': 34, 'Magic': 80, 'Dexterity': 69, 'Gold Coins': 100, 'Hit Points': hitpoints },
     {'Name':'Jordan','Strength': 67, 'Speed': 43, 'Magic': 100, 'Dexterity': 99, 'Gold Coins': 100 , 'Hit Points': hitpoints } ]
    
Monsters = [
     {'Name':'Creeper','Strength': 51, 'Speed': 56, 'Magic': 27, 'Dexterity': 89, 'Hit Points': hitpoints },
     {'Name':'Enderman','Strength': 94, 'Speed': 86, 'Magic': 77, 'Dexterity': 29, 'Hit Points': hitpoints } ,
     {'Name':'Killer Squid','Strength': 15, 'Speed': 96, 'Magic': 57, 'Dexterity': 57, 'Hit Points': hitpoints },
     {'Name':'Fire Dragon','Strength': 91, 'Speed': 86, 'Magic': 77, 'Dexterity': 9, 'Hit Points': hitpoints },
     {'Name':'Killer Kitty','Strength': 19, 'Speed': 21, 'Magic': 60, 'Dexterity': 39, 'Hit Points': hitpoints },
     {'Name':'Jerry the Monster','Strength': 20, 'Speed': 91, 'Magic': 70, 'Dexterity': 49, 'Hit Points': hitpoints },
     {'Name':'Larry the Killer Bug','Strength': 10, 'Speed': 34, 'Magic': 80, 'Dexterity': 69, 'Hit Points': hitpoints },
     {'Name':'Baby Monster Dragon','Strength': 6, 'Speed': 43, 'Magic': 100, 'Dexterity': 99, 'Hit Points': hitpoints },
     {'Name':'Zombie','Strength': 6, 'Speed': 46, 'Magic': 100, 'Dexterity': 99, 'Hit Points': hitpoints } ]

Weapons = [
     {'Name': 'Simple Sword', 'Power': 38, 'Enchanted': 'FALSE'},
     {'Name': 'Enchanted Sword', 'Power': 78, 'Enchanted': 'TRUE'},
     {'Name': 'First Shotgun', 'Power': 55, 'Enchanted': 'FALSE'},
     {'Name': 'Stop Shield', 'Power': 23, 'Enchanted': 'FALSE'},
     {'Name': 'Dagger', 'Power': 23, 'Enchanted': 'FALSE'},
     {'Name': 'Hand and a Half Sword', 'Power': 8, 'Enchanted': 'FALSE'},
     {'Name': 'Laser Gun', 'Power': 89, 'Enchanted': 'FALSE'} ,
     {'Name': 'Forcefield', 'Power': 56, 'Enchanted': 'FALSE'} ,
     {'Name': 'Axe', 'Power': 66, 'Enchanted': 'FALSE'} ]

NumPlayers = len (Players) -1
NumMonsters = len (Monsters) -1
NumWeapons = len (Weapons) -1
random.shuffle(Weapons)
PlayerWeapon=Weapons[0]['Name']



## Build a 9x9 zero index World Matrix as a list of lists first, then make it more random after you learn more
## has M for money, H for hostile,D for dimension (to the next world or touch and P for people (to next level, or you can just win). 
## you start at the *

matrix = [['H',' ','H',' ','H'], 
          [' ','*','H','P',' '], 
          ['P','H','H','H','P'], 
          ['H',' ','H',' ','M'], 
          [' ','H','H','P','D']]

## Print Matrix Out

def printmatrix() :
  print(' |-------------------|')
  print(' | ' + matrix[0][0] + ' | ' + matrix[0][1] + ' | ' + matrix[0][2] + ' | ' + matrix[0][3] + ' | ' + matrix[0][4] + " | ")
  print(' |-------------------|')
  print(' | ' + matrix[1][0] + ' | ' + matrix[1][1] + ' | ' + matrix[1][2] + ' | ' + matrix[1][3] + ' | ' + matrix[1][4] + " | ")
  print(' |-------------------|')
  print(' | ' + matrix[2][0] + ' | ' + matrix[2][1] + ' | ' + matrix[2][2] + ' | ' + matrix[2][3] + ' | ' + matrix[2][4] + " | ")
  print(' |-------------------|')
  print(' | ' + matrix[3][0] + ' | ' + matrix[3][1] + ' | ' + matrix[3][2] + ' | ' + matrix[3][3] + ' | ' + matrix[3][4] + " | ")
  print(' |-------------------|')
  print(' | ' + matrix[4][0] + ' | ' + matrix[4][1] + ' | ' + matrix[4][2] + ' | ' + matrix[4][3] + ' | ' + matrix[4][4] + " | ")
  print(' |-------------------|')

def getplayerpos() :
  return (1,1)

def welcome() :
    os.system('clear')
    print("/  \    /  \ ____ |  |   ____  ____   _____   ____      "    )
    print("\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \      "   )
    print(" \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/       "  )
    print("	\__/\  /  \___  >____/\___  >____/|__|_|  /\___  >      "  )
    print("			 \/       \/          \/            \/     \/   "   )   
    print("___________                                                 ")
    print("\__    ___/___                                              ")
    print("	|    | /  _ \                                             ")
    print("	|    |(  <_> )                                            ")
    print("	|____| \____/                                             ")
    print("																")														
    print("	________                                                  ")
    print("/  _____/_____    _____   ____                             ")
    print("/   \  ___\__  \  /     \_/ __ \                            ")
    print("\    \_\  \/ __ \|  Y Y  \  ___/                            ")
    print(" \______  (____  /__|_|  /\___  >                           ")
    print("				\/     \/      \/     \/                      "  )    
    print("________   _____                                            ")
    print("\_____  \_/ ____\                                           ")
    print(" /   |   \   __\                                            ")
    print("/    |    \  |                                              ")
    print("\_______  /__|                                              ")
    print("				\/                                            "  )    
    print("___________.__                                __         ._.")
    print("\_   _____/|  |   ____   _____   ____   _____/  |_  _____| |")
    print(" |    __)_ |  | _/ __ \ /     \_/ __ \ /    \   __\/  ___/ |")
    print(" |        \|  |_\  ___/|  Y Y  \  ___/|   |  \  |  \___ \ \|")
    print("/_______  /|____/\___  >__|_|  /\___  >___|  /__| /____  >__")
    print("		\/           \/      \/     \/     \/          \/ \/")
    print ("-----------------------------------------------------------")
    print("Welcome to the Game of Elements! Enter if you Dare! This Game was Created by BlazeSlayer1234 and Wireddude73 \n")
    
    
 

def roll_die() :
    return (random.randrange(1, 20))



def dobattle() :
    random.shuffle(Monsters)
    tMonster = Monsters[0]['Name']
    tMonster_Strength = int(Monsters[0]['Strength'])
    print ("-----------------------------------------------------")
    print ("You encounter a ", tMonster)
    print ("with a strenth of: ", tMonster_Strength)
    print ("Press f to fight, r to run, q to quit")
    action = input()
    if action == 'r':
        print ("Running . . . ")
        return ("You Ran!")
    elif action == 'f':
        die = roll_die()  
        print ("Die Roll Generates: ", die)        
        if die == 20:    
            print ("You Rolled a 20! You Win and Kill the ", tMonster)
            return ("You Win!")
        elif die == 1:
            print("You rolled a 1")
            return ("You Lose!")            
        ## at this point they didn't role a 1 or a 20 so we're just going my their strength comparison
        elif tMonster_Strength >= pStrength :
            print ("You Lose!")
            return ("You Lose!")
        else:
            print ("You Win!")
            return ("You Win!")
    elif action == 'q':
        print ("Quitting Game") ## later ask if they want to save, then also instrument a load previous progress
        return ("Quit")

# welcome() ## display welcome message

## Choose Player

print("Here are a list of possible players to choose from:")
for x in range (0, NumPlayers):
    print ('%s-%s' % (x,Players[x]['Name']))
print ("\nPlease choose a number for your player:")
PlayerNameChoice =  int(input())
PlayerName = Players[PlayerNameChoice]['Name']
print ('Hi there %s, you\'ve been assigned a %s as your weapon!' % (PlayerName, PlayerWeapon))

pStrength = Players[PlayerNameChoice]['Strength']
pSpeed = Players[PlayerNameChoice]['Speed']
pDexterity = Players[PlayerNameChoice]['Dexterity']
pMagic = Players[PlayerNameChoice]['Magic']
pGold_Coins = Players[PlayerNameChoice]['Gold Coins']
pWeaponPower = Weapons[0]['Power']
pWeaponEnchanted = Weapons[0]['Enchanted']
pStrength = pStrength + pWeaponPower
print ("Strength: ", pStrength)
#print ("Speed: ", pSpeed)
#print ("Dexterity: ", pDexterity)
#print ("Magic: ", pMagic)
#print ("Gold Coins: ", pGold_Coins)
#print ("Weapon Power: ", pWeaponPower)
#print ("Weapon Enchanted: ", pWeaponEnchanted)


## As long as you have some strength, do all this in the while loop (unless you quit the game)

while (pStrength > 0) :              ## as long as you have some strength, do all this in the while loop (unless you quit the game)
    
    
 ## Start your first move on the matrix
## find out where you are '*' matrix[0][1] for our purposes
## ask player what direction they want to go
## w = up, s = down, a = left, d = right
    playerpos = getplayerpos()
    printmatrix()
    print('what direction do you want to go w=up, s=down, a=left, d=right')
    direction = input()
    print (direction)
    x=playerpos[0]
    y=playerpos[1]
    if direction == 'w': # move player UP
      print ("w") # make current playerpos blank ' ' and change location of '*' playerpos from playerpos[0][1] to playerpos [0][0] 
      getLetter = matrix[x-1][y]  # gets the letter at the new position they're about to walk to
      matrix[x][y] = ' ' # makes the current position a space
      matrix[x-1][y] = '*' # draws the marker of where you are in the new position
      print ("You meet a", getLetter)
      printmatrix()
    elif direction == 's': # mobe player DOWN
      getLetter = matrix[x+1][y]  # gets the letter at the new position they're about to walk to
      matrix[x][y] = ' ' # makes the current position a space
      matrix[x+1][y] = '*' # draws the marker of where you are in the new position 
      print ("You meet a", getLetter)
      printmatrix()
    elif direction == 'a': # move player LEFT
      print ("a") 
      getLetter = matrix[x][y-1]  # gets the letter at the new position they're about to walk to
      matrix[x][y] = ' ' # makes the current position a space
      matrix[x][y-1] = '*' # draws the marker of where you are in the new position 
      print ("You meet a", getLetter)
      printmatrix()
    elif direction == 'd': # move player RIGHT
      print ("d")
      getLetter = matrix[x][y+1]  # gets the letter at the new position they're about to walk to
      matrix[x][y] = ' ' # makes the current position a space
      matrix[x][y+1] = '*' # draws the marker of where you are in the new position 
      print ("You meet a", getLetter)
      printmatrix()
 
      
## move player to appropriate square
## If H (hostile)  take durn, do battle
## If M for money add random number between 5-10 gold coins
## If D for dimension a new world generates, they level up
## If P people you move to a random P
## If ' ' then nothing, take another turn   
    

    
    Attack_Result = dobattle() 
    if Attack_Result == "You Win!":  ## if you win the fight, do all this
        pStrength+= increment
        print ("Your Strength has been incremented to ", pStrength)
    elif Attack_Result == "You Lose!":
        pStrength-= increment ## here, you lost the fight, but don't want to quit, you want to keep playing,
        print ("You lost the battle and your strength reduced to: ", pStrength)
        print ("Better luck next time!")
    elif Attack_Result == "You Ran!":     #### Below you ran, so your strength is decremented by 1, but we're still in the active while loop.
        pStrength-= 1 ## here, you lost the fight, but don't want to quit, you want to keep playing.
        print ("Strength reduced by running: ", pStrength)
    elif Attack_Result == "Quit":
        break    

print ("Out of Strength, Game Over!")

## stop here to save game status
game_data = { 'time': Time, 'player-position' : 'N23 E25', 'pockets' : PlayerWeapon, 'player-name' : PlayerName, 'gold coins': pGold_Coins}
## print (game_data)
save_file = open ('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

pygcurse.waitforkeypress()


