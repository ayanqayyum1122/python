import sys
import random

print("")
playerchoice = input("Enter...\n1 for ROCK , \n2 for PAPER , or \n3 for SCISSORS:\n\n")
print(" the type when you multiply")
print(type(playerchoice))

player = int(playerchoice)
print(" the type when you changed the Type" )
print(player+player)
print(type(player))


if player < 1 |  player > 3:
    sys.exit("you must enter 1, 2 or 3.")

COMPUTERCHOICE = random.choice("123456")

computer = int(COMPUTERCHOICE)

print("")
print("YOU choose   :"+ playerchoice)
print(" python choose  :" + COMPUTERCHOICE)
print("")

if player == 1:
  print("you win")








