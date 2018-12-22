#
# Ce programme permet de trouver le plus grand temps de vol avec la suite de Syracuse
#

from math import *

def pairoupas(n):       # fonction qui dit si un nombre est pair ou pas
    
    if n % 2 == 0:
        return("pair")
    else:
        return("impair")


def fairevoler(n):      # fonction qui fait "voler" le nombre n et retourne son vol sous forme de liste
    
    vol=[]  # on initialise à vide la liste vol qui va contenir le vol de n (la liste des valeurs successives prises par n)
    while n > 1 :       # cette boucle fait "voler" le nombre n
        if pairoupas(n)=="pair":
             n = n//2
        else :
            n = (3*n)+1
        vol.append(n)   # ajoute à la liste vol la nouvelle valeur de n
    return(vol)

N=int(input("Entrer un nombre entier : "))  # on saisit un nombre entier au clavier

k_max = 0    # cette variable qu'on initialise à 0 contiendra le nombre qui a le plus grand temps de vol
t_max = 0    # cette variable qu'on initialise à 0 contiendra le plus grand temps de vol

for x in range(3,N+1) : # on fait "voler" tous les nombres de 3 à N

    k=x     # attention on ne peut pas modifier la variable x de la boucle for, donc on travaille avec k
    voldek=fairevoler(k)    # on fait voler k et voldek contient son vol 
    longueurduvol = len(voldek)    # la longueur de vol est la taille de la liste voldek
    #print("vol de ",x," : ",voldek," Temps de vol : ",longueurduvol)    # affiche les nombres, leur vol et leur temps de vol
    if longueurduvol > t_max:  # si la longueur du vol qu'on vient de faire est plus grande que le max, alors ça devient le max
        t_max=longueurduvol  # en Python on peut aussi affecter les 2 variables d'un coup : t_max,k_max=longueurduvol,x
        k_max=x
        print("vol de ",x," : ",voldek)     # affiche le nouveau record
      
print("Parmi tous les nombres plus petits que ",N," celui qui a le vol le plus long est : ",k_max)
print("Son temps de vol est : ",t_max)
