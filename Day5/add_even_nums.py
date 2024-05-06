target = int(input()) # Enter a number between 0 and 1000

if target < 1000:
  sum = 0
  for num in range(0, target + 1, 2):
    sum += num 
  print(sum)