from math import *

#Définition de la fonction "retournement", qui retourne les valeurs à l'envers.

def retournement(tD):
	tI = ""
	for l in tD:
		tI = str(l + tI)
	print(tI)
	if tI == tD:
		print("True")
	else:
		print("False")

#Initialisation de la variable de base. tD = Texte Droit.
tD = input("Entrez le texte que vous souhaitez inverser : ")

#Début - End.
retournement(tD)

"""
------------------------------------------------------------------------------------
-|- Il existe aussi une autre manière de le faire. Avec le générateur reversed :

from math import *

#Initalisation des variables.

tD = input("Que voulez-vous mettre à l'envers ? ")
tI = ""

#Générateur reversed. 

for l in reversed(tD):
    tI += l

#Impression du texte à l'envers.
print (t2)"""

