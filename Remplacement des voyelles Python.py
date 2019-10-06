from math import *

#Initialisaton des variables.

mot = input("Entrez un mot, je remplacerais les voyelles par i : ") #Entrée
mot2 ="" #Sortie (mot sans voyelles)

#Détection et remplacement des voyelles.

for l in mot: 
	if l == "a" or l == "e" or l == "o" or l == "u"or l == "y": #Test de condition.
		l = "i" #Remplacement
	mot2 += l #Formation du mot.
#Impression du mot.
print(mot2)