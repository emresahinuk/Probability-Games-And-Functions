#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math
# Taking Inputs
lower = 1
 
# Taking Inputs
upper = 20
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
       5,
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < 5:
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= 5:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")


# In[ ]:




