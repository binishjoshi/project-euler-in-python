from time import time
from eulerlib import prime_numbers # Uses Seive of Eratosthenes

t0 = time()

print(sum(prime_numbers.primes(1999999)))
print(time() - t0)
