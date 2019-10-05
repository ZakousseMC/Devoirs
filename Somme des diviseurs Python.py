from math import *

x = int(input("Saisissez un nombre et je vais écrire les diviseurs : "))
z = 0


for i in range(1, x+1):
	if x % i == 0:
		print(i)
		z = z + i
print(z)