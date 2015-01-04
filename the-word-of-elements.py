# The Game of Elements v1.0
# Authors: BlazeSlayer1234, WiredDude73
# nogui branch

# see http://inventwithpython.com/pygcurse/tutorial/ for more info
# win = pygcurse.PygcurseWindow(80, 50, 'The World Of Elements')
# print = win.pygprint
# input = win.input
# win.setscreencolors('green', 'black', clear=True)


import sys
import random
import os
import time
import pickle
import pygcurse

def welcome() :
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





def roll_die() :
    return (random.randrange(1, 20))

# time check

Time = time.asctime()

# check if game data file exists before asking user all their info, right now we don't do anything with the value.
SaveFilePresent =  os.path.isfile("save.dat")

# Define the Players, Monsters, Weapons (later, move all this to a config file)

hitpoints = 100
increment = 5

Players = [
 {'Name':'Korto','Strength': 75, 'Speed': 56, 'Magic': 27, 'Dexterity': 89, 'Gold Coins': 100, 'Hit Points': hitpoints },
 {'Name':'Tom','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29, 'Gold Coins': 100, 'Hit Points': hitpoints } ,
 {'Name':'Jack','Strength': 15, 'Speed': 96, 'Magic': 57, 'Dexterity': 57, 'Gold Coins': 100 , 'Hit Points': hitpoints},
 {'Name':'Nathaniel','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 9, 'Gold Coins': 100, 'Hit Points': hitpoints },
 {'Name':'David the Wimp','Strength': 3, 'Speed': 21, 'Magic': 60, 'Dexterity': 39, 'Gold Coins': 100, 'Hit Points': hitpoints },
 {'Name':'Jerry','Strength': 2, 'Speed': 91, 'Magic': 70, 'Dexterity': 49, 'Gold Coins': 100, 'Hit Points': hitpoints },
 {'Name':'Noah','Strength': 100, 'Speed': 34, 'Magic': 80, 'Dexterity': 69, 'Gold Coins': 100, 'Hit Points': hitpoints },
 {'Name':'Jordan','Strength': 67, 'Speed': 43, 'Magic': 100, 'Dexterity': 99, 'Gold Coins': 100 , 'Hit Points': hitpoints} ]

Monsters = [
 {'Name':'Creeper','Strength': 75, 'Speed': 56, 'Magic': 27, 'Dexterity': 89, 'Hit Points': hitpoints },
 {'Name':'Enderman','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 29, 'Hit Points': hitpoints } ,
 {'Name':'Killer Squid','Strength': 15, 'Speed': 96, 'Magic': 57, 'Dexterity': 57, 'Hit Points': hitpoints },
 {'Name':'Fire Dragon','Strength': 35, 'Speed': 86, 'Magic': 77, 'Dexterity': 9, 'Hit Points': hitpoints },
 {'Name':'Killer Kitty','Strength': 3, 'Speed': 21, 'Magic': 60, 'Dexterity': 39, 'Hit Points': hitpoints },
 {'Name':'Jerry the Monster','Strength': 2, 'Speed': 91, 'Magic': 70, 'Dexterity': 49, 'Hit Points': hitpoints },
 {'Name':'Larry the Killer Bug','Strength': 100, 'Speed': 34, 'Magic': 80, 'Dexterity': 69, 'Hit Points': hitpoints },
 {'Name':'Baby Monster Dragon','Strength': 67, 'Speed': 43, 'Magic': 100, 'Dexterity': 99, 'Hit Points': hitpoints } ,
 {'Name':'Zombie','Strength': 67, 'Speed': 43, 'Magic': 100, 'Dexterity': 99, 'Hit Points': hitpoints } ]

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

# Define Weapons
# hitpoints
# character class
# level XP
# experience points


random.shuffle(Weapons)
PlayerWeapon=Weapons[0]['Name']


World=((350,350))

# Introduce the user to the game

os.system('clear')

welcome()
print("Welcome to the Game of Elements! Enter if you Dare! This Game was Created by BlazeSlayer1234 and Wireddude73 \n")
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

print ("Strength: ", pStrength)
#print ("Speed: ", pSpeed)
#print ("Dexterity: ", pDexterity)
#print ("Magic: ", pMagic)
#print ("Gold Coins: ", pGold_Coins)
#print ("Weapon Power: ", pWeaponPower)
#print ("Weapon Enchanted: ", pWeaponEnchanted)


def taketurn() :
    random.shuffle(Monsters)
    tMonster = Monsters[0]['Name']
    tMonster_Strength = int(Monsters[0]['Strength'])
    print ("You encounter a ", tMonster)
    print ("with a strenth of: ", tMonster_Strength)
    print ("Press f to fight or r to run")
    action = input()
    if action == 'r':
        print ("Running to next village")
        return ("You Lose!")
    else:
        die = roll_die()  ## assumes you pressed f since you didn't run.
        print ("Die Roll Generates: ", die)        
        if die == 20:    
            print ("You Win and Kill the ", tMonster)
            return ("You Win!")
        elif die == 1:
            return ("You Lose!")
        elif tMonster_Strength >= pStrength :
            return ("You Lose!")
        else:
            return ("You Win!")

## First Battle

while (pStrength > 0) :              ## as long as you have some strength, do all this in the while loop (unless you quit the game)
    Attack_Result = taketurn() 
    if Attack_Result == "You Win!":  ## if you win the fight, do all this
        pStrength+= increment
        print (Attack_Result)
        print ("Your Strength has been incremented to ", pStrength)
        print ("Play Again? (y/n)")
        action = input()
        if action == 'y':
            Attack_Result = taketurn()
        elif action == 'n': 
            print ("Quitting Game") ## later ask if they want to save, then also instrument a load previous progress
            break
    pStrength-= increment ## here, you lost the fight, but don't want to quit, you want to keep playing,
    print ("You lost the battle and your strength reduced to: ", pStrength)
    print ("Better luck next time!")

print ("Out of Strength, Game Over!")

## stop here to save game status
game_data = { 'time': Time, 'player-position' : 'N23 E25', 'pockets' : PlayerWeapon, 'player-name' : PlayerName, 'gold coins': pGold_Coins}
## print (game_data)
save_file = open ('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

#pygcurse.waitforkeypress()


