from math import * 

a = int(input("Entrez un nombre : "))
b = int(input("Entrez un autre nombre : "))
c = int(input("Entrez un autre autre nombre : "))

if a > b & a > c:
	print(a)
if b > a & b > c:
	print(b)
if c > a & c > b:
	print(c)
