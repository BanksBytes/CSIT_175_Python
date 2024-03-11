#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 6 Excercise 2, Dice Game

import random

# variables and constants
HOW_MANY_DICE = 5
MAX_DICE_VALUE = 6

roll_types = ["Junk", "Pair", "3 of a kind", "4 of a kind", "5 of a kind"]

# declare a list for dice rolls and tallying dice rolls
# there are 5 dice when we roll, so we need to store each one
pdice = [0, 0, 0, 0, 0] # player's dice
cdice = [0, 0, 0, 0, 0] # computer's dice

# tally lists will be 6 in size since the dice values run from 1 - 6
# count how many 1s, 2s, 3s, 4s...
ptally = [0, 0, 0, 0, 0, 0] # player: how many of each value rolled
ctally = [0, 0, 0, 0, 0, 0] # computer :

# Start the game !
# roll the dice for player and computer
i = 0 # start the (dice) counter 
while i < HOW_MANY_DICE:
    pdice[i] = random.randint(1, MAX_DICE_VALUE)
    cdice[i] = random.randint(1, MAX_DICE_VALUE)
    i += 1

i = 0 # reset the counter
print("Player dice: ", end = "")
while i < HOW_MANY_DICE:
    print(pdice[i], end="")
    i += 1

i = 0 # reset the counter
print("\nComputer dice: ", end=" ")
while i < HOW_MANY_DICE:
    print(cdice[i], end=" ")
    i += 1


#Check the results !
# Load the tally list so we can determine pair, 3 of a kind...
# Notice how we use the dice value (1 - 6) minus 1 as an array subscript
# (0 - 5). (Clever!)
# Good application from the chapter how we can use an array (well, "list"
# in python)to replacve a selcetion structure
    
i = 0
while i < HOW_MANY_DICE:
    # if the value of this one is "1", then tally it in the first open spot (0),
    # if it's 6, add it to the index 5.
    ptally[pdice[i] - 1] += 1
    ctally[cdice[i] - 1] += 1
    i += 1

# find the largest count
# find out how many 2s, 3s, 4s... to determine pair, 2 of a kind...
pmax = ptally[0]
cmax = ctally[0]

i = 1
while i < MAX_DICE_VALUE: # this should be i < len(ptally) !
    if pmax < ptally[i]:
        pmax = ptally[i]
    if cmax < ctally[i]:
        cmax = ctally[i]
    # end if:
    i += 1
# end while: loop
    
# output - display pair, 3 of a kind...
# Once again, we use an array (list) to replace a selection structure
print("\n\nPlayer rolled: " + roll_types[pmax - 1])
print("Computer rolled: " + roll_types[cmax - 1])
print()

# who won?
if pmax > cmax:
    print("Player wins!")
elif cmax > pmax:
    print("Computer Wins")
else:
    print("Tie!")