a, b, s = 1, 2, 0
while a < 4000000:
  if a % 2 == 0:
    s = s + a 
  c = a + b
  a = b
  b = c
print('Sum is ' + str(s))