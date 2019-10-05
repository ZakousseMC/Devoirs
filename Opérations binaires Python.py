from math import *

#Défintion des différentes fonctions.

def binaire_decimal(chaine_binaire):
	"""Converti un nombre binaire en nombre en base 10"""
	nb_decimal = 0
	for element in chaine_binaire :
		if element == '0' :
			nb_decimal = 2 * nb_decimal
		else :
			nb_decimal = 2 * nb_decimal + 1
	return nb_decimal #Affiche le nombre en décimal, BASE 10.

def decimal_binaire(produit):
	"""Converti un nombre décimal en nombre de base 2. BINAIRE"""
	while produit != 0:
		if produit % 2 == 0:
			print("0",end="")
			produit = produit // 2
		else:
			print("1",end="")
			produit = produit // 2
	print("")
	print("Attention ! Le nombre donné en base 2 est inversé, lisez le de gauche à droite. ")

def produit_binaire(entier_binaire1, entier_binaire2):
	"""Effectue le produit de deux nombres donnés en binaire."""
	entier_decimal1 = 0
	entier_decimal2 = 0
	entier_decimal1 = binaire_decimal(entier_binaire1)
	entier_decimal2 = binaire_decimal(entier_binaire2)
	produit = entier_decimal1 * entier_decimal2
	print("Le résultat de la multiplication en décimal est : ",produit)
	r = input("Voulez-vous convertir la valeur en base 2 ? Tapez 'Oui' si vous le souhaitez, écrivez autre chose si vous ne voulez pas : ")
	if r == "Oui":
		print("Le resultat de la multiplication en binaire est : ")
		return decimal_binaire(produit)
	else :
		print("Ok !")

#Initialisation des variables.

#La variable "chaine_binaire" est facultative, celle-ci lance la première fonction lorsqu'elle est activée.
#chaine_binaire = input("Entrez la chaîne de votre nombre en binaire : ")
entier_binaire1 = input("Entrez la chaîne de votre premier facteur en binaire : ")
entier_binaire2 = input("Entrez la chaîne de votre deuxième facteur en binaire : ")

#Début - End.
produit_binaire(entier_binaire1, entier_binaire2)