from time import time

t0 = time()

N = 1000

for i in range(1, 1000 + 1):
	for j in range(i + 1, 1000 + 1):
		l = N - i - j

		if i * i + j * j == l * l:
			print(i * j * l)
			print(time() - t0)
			exit()
