import os
def entrées():
    a = float(input("a : "))
    b = float(input("b : "))
    masse1 = float(input("masse 1 : "))
    masse2 = float(input("masse 2 : "))
    return a,b,masse1,masse2



#Cette fonction calcul la force de gravitation selon la distance et la masse des deux objets
#entrées : a,b,masse1 et masse2 sont des nombre réels
#sortie : la fonction retourne le réel somme
def metier(a,masse1,masse2):
    gravitation = float((6.67*10**(-11))*((masse1*masse2)/(a**2)))
    return gravitation




def affiche(gravitation,a):
    print("F(",a,")=",gravitation," N")


a,b,masse1,masse2=entrées()
while(a<b):
    gravitation = metier(a,masse1,masse2)
    affiche(gravitation,a)
    a=a*2

os.system("pause")

