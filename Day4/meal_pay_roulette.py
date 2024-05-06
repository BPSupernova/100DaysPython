names_string = input("Input members of the table, separated by commas ")
names = names_string.split(", ")
# names_string contains the input values provided. 

import random
rand_int = random.randint(0, len(names) - 1)
print(f"{names[rand_int]} is going to buy the meal today!")