from math import * #Importer le module math.

X = [x for x in range(1, 11)] #Création de la liste X pour x variant de 1 à 11 (exclu).
P = [p/55 for p in range(1, 11)] #Création de la liste P pour p variant de 1 à 11(exclu) et prenant la valeur p/55.

def esperance(X,P): #Définition de la fonction "esperance".
	"""
	Retourne l'espérance d'une loi de
	probabilité grâce à ses valeurs.

	>>> esperance(X,P)
	7.0
	"""
	E = 0 #Initialisation de la variable.

	for k in range(10): #Début de la boucle.
		E += X[k]*P[k] #Calcul de l'espérance.


	return E #Retourne la valeur de E, soit l'espérance. (Et une petite phrase). 

def parametre_dispersion(X,P):
	"""
	Retourne la variance et l'écart-type.

	>>> parametre_disposition(X,P)
	(6.0, 2.449489742783178)
	"""
	E = esperance(X,P) #Calcul de l'espérance.
	V = 0 #Initalisation de la variance. (Variable V).

	for i in range(10): #Début de la boucle. 
		V += P[i]*((X[i] - E)**2) #Calcul de la variance.

	ET = sqrt(V) #Calcul de l'écart type.

	return V, ET #Retourne la variable V ainsi que la variable ET.