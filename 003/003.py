N = 600851475143

def check_prime(x):
  count = 0
  for i in range(2, x):
    if x % i == 0:
      count = count + 1
  if count == 0:
    return True
  else:
    return False

def next_prime(x):
  for i in range(x + 1, N):
    if check_prime(i):
      return i

def largest_prime_factor(x):
  prime = 2
  temp = N
  while 1:
    if temp == 1:
      return prime
    elif temp % prime == 0:
      temp = temp / prime
    else:
      prime = next_prime(prime)

print('The largest prime factor of ' + str(N) + ' is ' + str(largest_prime_factor(N)))