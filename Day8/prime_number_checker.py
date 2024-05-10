def prime_checker(number):
  prime = True
  if number <= 1:
    print("It's not a prime number.")
    prime = False
    
  else:
    for num in range(2, number - 1):
      if number % num == 0:
        print("It's not a prime number.")
        prime = False
        break

  if prime == True:
    print("It's a prime number.")

n = int(input()) # Check this number
prime_checker(number=n)