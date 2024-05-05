print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

score = 0
true_score = 0 # For matching characters of T R U E
love_score = 0 # For matching characters of L O V E

for char in name1:
  if char.lower() == "t" or char.lower() == "r" or char.lower() == "u":
    true_score += 1
  elif char.lower() == "l" or char.lower() == "o" or char.lower() == "v":
    love_score += 1
  elif char.lower() == "e":
    true_score += 1
    love_score += 1

for char in name2:
  if char.lower() == "t" or char.lower() == "r" or char.lower() == "u":
    true_score += 1
  elif char.lower() == "l" or char.lower() == "o" or char.lower() == "v":
    love_score += 1
  elif char.lower() == "e":
    true_score += 1
    love_score += 1

score = int(str(true_score) + str(love_score))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")