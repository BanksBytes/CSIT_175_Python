#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 3 Excercise 3, Coin Flip

import random

# variables and constants
MAX_FLIPS = 20
MAX_VAL = 2
heads = 0.0
tails = 0.0
pct_heads = 0.0
pct_tails = 0.0
i = 0
flip = 0

for i in range(1, MAX_FLIPS + 1, 1):
    flip = random.randint(0,1)
    if flip == int 1:
        heads += 1 and print ("Heads!")
    else:
        tails += 1 and print("Tails!")


print("Total heads: {0}".format(heads))

pct_heads = (heads / MAX_FLIPS) * 100.0

print("Pct heads: %{0:.1f}".format(pct_heads))