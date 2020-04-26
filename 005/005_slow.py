# Smallest positive multiple divisible by all prime numbers from 1 to 20

# Returns Prime Numbers from provided intervals
def return_prime(start, end):
  prime = list()
  for i in range(start, end + 1):
    count = 0
    for j in range(2, i):
      if i % j == 0:
        count += 1
    if count == 0:
      prime.append(i)
  return prime

# Tests if start is divisible by all numbers from 1 to 20
def test_all(start):
  # Range from 2 because is every number is divisible by 1 and doesn't need check
  for i in range(2, 21):
    if start % i != 0:
      return False
  return True

prime_20_1 = return_prime(1, 20)[::-1]

start = 40
found = False
count = 0

while not found:

  if count % 1261073 == 0:
    print('Testing-----' + str(start))

  count += 1

  for i in prime_20_1:
    if start % i != 0:
      # If start variable is not divisible by one of the primes, break loop, and check for another
      found = False
      break
    
    # if start variable is divisible by all primes, check if it is divisible for all numbers
    if test_all(start):
      found = True
  
  start += 1


print(start - 1)
