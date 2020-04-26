# Smallest positive multiple divisible by all prime numbers from 1 to 20

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

prime_20_1 = return_prime(1, 20)[::-1]
print(prime_20_1)

start = 40

cond = 1
found = True

while cond:
  print('Testing-----' + str(start))
  for i in prime_20_1:
    if start % i != 0:
      if i < 14:
        print('Not divide  ' + str(start) + ' by ' + str(i))
      found = False
      break
    found = True

  if found == True:
    break
  start += 1

print(start)
