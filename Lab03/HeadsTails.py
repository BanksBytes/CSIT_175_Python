#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 3 Excercise 3, Coin Flip

import random

# variables and constants
MAX_FLIPS = 20
MAX_VAL = 2
heads = 0
tails = 0
pct_heads = 0.0
pct_tails = 0.0
i = 0
flip = 0

for i in range(1, MAX_FLIPS + 1, 1):
    flip = random.randint(0,1)
    if flip == 1 :
        heads += 1 
        print("Heads")
    if flip == 0 :
        tails += 1
        print("Tails")



# Print out the total # of heads that was flipped
print("Total heads: {0}".format(heads))
# Get the percentage that heads was flipped 
pct_heads = (heads / MAX_FLIPS) * 100.0
# Print out the percentage that was gotten on the previous calculation
print("Pct heads: %{0:.1f}".format(pct_heads))


# Print out the total # of heads that was flipped
print("Total tails: {0}".format(tails))
# Get the percentage that tails was flipped 
pct_tails = (tails / MAX_FLIPS) * 100.0
# Print out the percentage that was gotten on the previous calculation
print("Pct tails: %{0:.1f}".format(pct_tails))