from math import * 

#Initialisation limites. Entrez 10 000 pour faire comme dans la consigne.
n = int(input("Entrez un nombre n et je vous dirais tous les nombres parfaits compris entre 1 et n : "))

#Début de la boucle.
for i in range(1, n):
	s = 0 #Initialisation somme.
	for j in range(1, i):
		if i % j == 0:
			s = s + j #Calcul de la somme des diviseurs.
	if s == i:
		print(s) #Affichage du nombre parfait.

#Warning : Programme assez consommateur, à éviter pour des n trop grands.