print("Tip calculator has booted up! * Smiley face w/ sunglasses *")
total = float(input("How much was the total bill? "))
tip_percent = float(input("What percent tip would you like to give? (Type in a number) "))
split = float(input("Now how many people are splitting the bill? (Type in a whole number) "))
price = round((total + (total * (tip_percent / 100))) / split, 2)
print(f"Each person should pay {price}")