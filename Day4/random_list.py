import random
import my_module # My own defined module

# Mersenne Twister is the math algorithm that Python uses to generate psuedo-random numbers
# Random integer generation
rand_int = random.randint(1, 10)

# Random float generation
rand_float = random.random() * 5

# Using a user-defined module
print(my_module.pi)

# Python List
states_of_america = ["Delaware", "Pennsylvania"]
print(len(states_of_america))

# Add an item to the end of the list through append()
# Add items to the end of the list through extend()
