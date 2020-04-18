from math import *

def solutions(a, b, c):
	""""
	Donne les solutions d'un polynômes.
	Renvoie un message s'il n'y a aucune solution dans l'ensemble R.
	"""
	d = (b**2) - (4 * a * c) #Calcul du discriminant nommé d.

	if d < 0: #Test de condition pour voir si le discriminant est inférieur à zéro.
		return "Il n'y a pas de solution dans l'ensemble R." #Si le discriminant est inférieur à zéro, il n'y a pas de solution dans l'ensemble R.
	elif d == 0: #Test de condition pour voir si le discriminant est égal à zéro.
		x = (-b) / (2*a) #Si le discriminant est égal à zéro, il n'y à qu'une seule solution dans R, qui est égale à alpha. (-b / 2a).
		return x #Renvoyer la solution contenue dans la variable x.
	else: #Si le discriminant n'est ni inférieur, ni égal à zéro, c'est qu'il est forcément supérieur. Il y a donc deux solutions.
		x_1 = ((-b - sqrt(d)) / (2 * a)) #Calcul de la première solution. 
		x_2 = ((-b + sqrt(d)) / (2 * a)) #Calcul de la deuxième solution.
		return x_1, x_2 #Renvoyer les deux solutions contenues dans les variables x_1 et x_2.
