# Python come with lots of built in modules. 
# A list of them can be found here: https://docs.python.org/3/py-modindex.html

# Example: Generate a random value using the random module

import random
random.random() # - generates a random number

for i in range(3): #in a loop from 0-3
    print(random.random())

# Example: get a randon number between 10 & 20
rand_num = random.randint(10,20) # - this generates a within a range of 10 & 20
print(rand_num)

# Example: given a list of people, randomly select a team lead

members=['briahana', 'chynna','krystal','Nubia']
lead = random.choice(members) # - this randomly selects an item from a list
print(lead)

# Problem: write a program that simulates the act of rolling a pair of dice
# Dice is a new type that has the roll method

class Dice:
    def roll(self):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        return die1, die2

dice = Dice()
print(dice.roll())