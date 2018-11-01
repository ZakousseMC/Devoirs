from math import *

print("Bienvenue dans le programme de calcul de périmètre et d'aire d'un triangle fait par Zaky.")
print("Merci d'entrer les cordonnés.")
xA=int(input("Entrez l'abscisse du point A: "))
yA=int(input("Entrez l'ordonnée du point A: "))
xB=int(input("Entrez l'abscisse du point B: "))
yB=int(input("Entrez l'ordonnée du point B: "))
xC=int(input("Entrez l'abscisse du point C: "))
yC=int(input("Entrez l'ordonnée du point C: "))
AB = sqrt((xB - xA)**2 + (yB - yA)**2)  #-Calcul des longueurs.
AC = sqrt((xC - xA)**2 + (yC - yA)**2)
BC = sqrt((xB - xC)**2 + (yB - yC)**2)  #-Fin.
ABarrondi = round(AB, 2) #Longueurs arrondies.
ACarrondi = round(AC, 2)
BCarrondi = round(BC, 2)
Pabc = AB + AC + BC #Périmètre.
Pabcarrondi = round(Pabc, 2) #Périmètre arrondi.
S = 0.5 * Pabc
Aabc = sqrt(S * (S - AB)*(S - AC)*(S - BC)) #Aire.
Aabcarrondi = round(Aabc, 2) #Aire arrondie.
TC = 0
if AB == AC or AC == BC or AB == BC : #ISO
    print("Il s'agit d'un triangle isocele")
    f = 1
elif BC**2 == AB**2 + AC**2 or AB**2 == BC**2 + AC**2 or AC**2 == AB**2 == BC**2 : #REC
    print("Il s'agit d'un triangle rectangle")
    f = 1
elif AB == AC and AB == BC and AC == BC : #EQUI
    print("Il s'agit d'un triangle equilateral")
    f = 1
elif f == 0 :
    print("Il s'agit d'un triangle quelconque")
print("AB = ", ABarrondi,"AC = ", ACarrondi, "BC = ", BCarrondi, "Les mesures sont arrondies au centième") #MONTRE LES MESURES.
print("Le périmètre du triangle ABC arrondi au centième est de : ", Pabcarrondi) #MONTRE LE PERIMETRE.
print("L'aire du triangle ABC arrondi au centième est de :", Aabcarrondi) #MONTRE L'AIRE.



