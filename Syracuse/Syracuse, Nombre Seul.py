from math import *

#DEF PAIRIMPAIR
def PairImpair(n):

    if n % 2 == 0:
        return("pair")
    else:
        return("impair")

n=int(input("Entrez le nombre que vous vouliez tester, il doit être entier : "))
print("Le nombre ",n," est ",PairImpair(n))

while n != 1:
    if n % 2 == 0:
        n = n // 2
        print(n)
        if n == 4:
            print("Lorsque n = 4, il est impossible de continuer, fin du programme.")
            sys.exit(".") #Fin du programme.
    else:
        n = 3*n+1
        print (n)
        if n == 4:
            print("Lorsque n = 4, il est impossible de continuer, fin du programme.")
            sys.exit(".") #Fin du programme.

#CONTOURNER OVERFLOW SYS ADD 2 SLASH/IMPORT SYS
#Python peut gérer des nombres entiers arbitrairement grands lors du calcul.
#Tout nombre entier trop grand pour tenir sur 64 bits (ou quelle que soit la limite matérielle sous-jacente) est géré par logiciel.
#Pour cette raison, Python 3 n'a pas de constante sys.maxint.
