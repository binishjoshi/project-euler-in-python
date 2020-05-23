from time import time

t0 = time()

def is_prime(x):
  if x == 2:
    return 1
  elif x % 2 == 0:
    return 0
  i = 3
  r = int(x ** 0.5) + 1
  while i < r:
    if x % i == 0:
      return 0
    i += 1
  return 1

i, p = 1, 3
while i < 10001:
  if is_prime(p):
    i += 1
  p += 2

print(p - 2)
t1 = time()
print(t1 - t0)
