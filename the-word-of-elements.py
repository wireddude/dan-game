# Define the Players

Players=['Tom','Korto', 'Jack', 'Nathaniel','David','Jerry The Warrier', 'Noah', 'Jordan']
NumPlayers = len (Players)
Weapons=['Simple Sword', 'First Shotgun', 'Stop Shield', 'Hand and half sword', 'Laser Gun', 'Forcefield']
NumWeapons = len (Weapons)
World=((100,100))

print("Welcome to the World of Elements! Enter if you Dare! This Game was Created by BlazeSlayer1234 and Wireddude73 \n")

print("Here are a list of possible Players to choose from:")
for x in range (0, NumPlayers):
	print ('%s-%s' % (x,Players[x]))



print ("\n")

print("Here is a list of possible weapons")
for i in Weapons:
	print (i)


