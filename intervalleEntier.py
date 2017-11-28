import os
def entrées():
    a = float(input("a : "))
    b = float(input("b : "))
    somme = 0
    return a,b,somme



#Cette fonction aditionne les multibles de 5 compris dans un intervalle 
#entrées : a,b et somme sont des nombre réels
#sortie : la fonction retourne le réel somme
def metier(a,b,somme):
    while (a<b):
        if (a%5==0):
            somme = somme + a
        a=a+1
    return somme




def affiche(somme):
    print(somme)


a,b,somme=entrées()
somme=metier(a,b,somme)
affiche(somme)

os.system("pause")
