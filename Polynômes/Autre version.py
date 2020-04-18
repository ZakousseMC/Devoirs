from math import *

#Début du programme.
print("Ce programme permet d'effectuer la résolution de certains trînomes, ainsi que d'afficher Delta.")
#Initalisation des variables.
a = int(input("Entrez le coefficient a : "))
b = int(input("Entrez le coefficient b : "))
c = int(input("Entrez le coefficient c : "))

delta = (b**2) - (4 * a * c)
print ("Delta égal à ", delta) #Test de vérification

x = 0 #x1
y= 0 #x2

#Début du test de conditions.
if delta < 0:
	print("Il n y a pas de solution dans l'ensemble R.")
elif delta == 0:
	print("Il y a qu'une seule solution.")
	x = -b / 2 * a
	print("La solution est égale à", x)
elif delta > 0:
	print("Il y a deux solutions.")
	x = ((-b - sqrt(delta)) / (2 * a))
	y = ((-b + sqrt(delta)) / (2 * a))
	print("x1 est égal à", x)
	print("x2 est égal à", y)
