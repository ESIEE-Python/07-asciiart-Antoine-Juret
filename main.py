""" ce fichier sert a encoder une chaine de charactère"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(10000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
     passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    caractère=[s[0]]
    occurences=[1]

    if len(s) == 0:
        return []

    for k in range(1,len(s)):
        if s[k]==s[k-1]:
            occurences[-1] +=1
        else:

            occurences.append(1)
            caractère.append(s[k])

    Resultat = []
    for i in range(len(caractère)):
        Resultat.append((caractère[i],occurences[i]))

    return Resultat




def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    if len(s) == 0:
        return []
    caractère=s[0]
    occurences=1 #Initialisation du compteur,compte combien de fois ce caractère C apparaît

     # cas de base
    while occurences< len(s) and s[occurences] == caractère:
        occurences += 1 # recherche nombre de caractères identiques au premier

    # appel récursif

    return [(caractère,occurences)]+artcode_r(s[occurences:])
    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif




#### Fonction principale


def main():
    """
    ici on fait l'appel de la fonction 
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
