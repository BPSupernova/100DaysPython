print("Thank you for choosing Ben Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

price = 0
invalid = False

if size == "S":
  price = 15
elif size == "M":
  price = 20
elif size == "L":
  price = 25
else:
  invalid = True
  
if add_pepperoni == "Y":
  if size == "M" or size == "L":
    price += 3
  elif size == "S":
    price += 2

if extra_cheese == "Y":
  price += 1

if invalid == False:
  print(f"Your final bill is: ${price}.")
else:
  print("Your order was invalid. Please enter a legitimate pizza size.")