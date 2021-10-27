#Mini Calculatrice
from math import *


#affichage des operateurs
def printOperations(dic_operateurs):
    print("***** Liste des operateurs *****")
    for x , y in dic_operateurs.items():
        print(x, ".", y)


# get number
def getOperateur():
    print("Entrer l'opérateur de votre choix(+,-,*,/,sqrt,**):")
    return input()

# addition
def addition():

    try:
        nb1 = float(input("Entrer un nombre:"))
        nb2 = float(input("Entrer un nombre:"))
        print("resultat:", nb1, "+", nb2, "=", nb1 + nb2)
    except:
        print("Erreur type: veuillez entrer un nombre, merci!")


# soustraction
def soustraction():

    try:
        nb1 = float(input("Entrer un nombre:"))
        nb2 = float(input("Entrer un nombre:"))
        print("resultat:", nb1, "-", nb2, "=", nb1 - nb2)
    except:
        print("Erreur type: veuillez entrer un nombre, merci!")


# multiplication
def multiplication():

    try:
        nb1 = float(input("Entrer un nombre:"))
        nb2 = float(input("Entrer un nombre:"))
        print("resultat:", nb1, "*", nb2, "=", nb1 * nb2)
    except:
        print("Erreur type: veuillez entrer un nombre, merci!")


# division
def division():

    try:
        nb1 = float(input("Entrer un nombre:"))
        nb2 = float(input("Entrer un nombre:"))
        if nb2 != 0:
            print("resultat:", nb1, "/", nb2, "=", nb1 / nb2)
        else:
            print("Erreur: votre 2ieme nombre doit etre différent de 0!")
    except:
            print("Erreur type: veuillez entrer un nombre, merci!")


#racine carré
def racine_carre():
    try:
        nb = float(input("Entrer un nombre:"))
        if nb > 0:
            print("resultat: sqrt(", nb, ") =", sqrt(nb))
        else:
            print("Entrer un nombre positif; La racine carré d'un nombre negatif ne peut etre calculer.")
    except:
        print("Erreur type: veuillez entrer un nombre, merci!")


#exposant
def exposant():
    try:
        nb1 = float(input("Entrer un nombre:"))
        nb2 = float(input("Entrer un nombre:"))
        print("resultat:", nb1, "**", nb2, "=", nb1 ** nb2)
    except:
        print("Erreur type: veuillez entrer un nombre, merci!")


def maCalculatrice(dic_operateurs, operateurs):
    choix = "oui"
    while choix == "oui":
        # affichage liste operations
        printOperations(dic_operateurs)

        #Entrer votre operateur
        operateur = getOperateur()

        if operateur not in operateurs:
            print("Erreur: operateur invalide!")
        else:
            if operateur == "+":
                addition()
            elif operateur == "-":
                soustraction()
            elif operateur == "*":
                multiplication()
            elif operateur == "/":
                division()
            elif operateur == "sqrt":
                racine_carre()
            elif operateur == "**":
                exposant()

        #autre operation
        print("Voulez vous faire une autre operation (oui/non):")
        choix = input()

    #operation terminé
    print("\n Merci! Aurevoir!")









