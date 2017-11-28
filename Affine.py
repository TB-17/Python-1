import os
def entrées():
    a = float(input("a : "))
    b = float(input("b : "))
    return a,b



#Cette fonction affine calcul la fonction affine f(x)=ab
#entrées : a et b deux nombre réels
#sortie : la fonction retourne le resultat de a*b
def metier(a,b):
    fx = a*b
    return fx




def affiche(charac):
    print(charac)


a,b=entrées()
fx=metier(a,b)
affiche(fx)

os.system("pause")

