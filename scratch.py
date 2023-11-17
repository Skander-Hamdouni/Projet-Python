#Import de la bibliotheque os
import os

# Code donné par le sujet permettant de récupérer les noms des fichiers
def list_of_files(directory):
    files_names = [] # Créer le tableau des noms récupérer
    for filename in os.listdir(directory): 
        if filename[-4:] == ".txt":
            files_names.append(filename) 
    return files_names

# Test la fonction list_of_files
assert list_of_files('./speeches') == ['Nomination_Chirac1.txt', 'Nomination_Chirac2.txt', 'Nomination_Giscard dEstaing.txt', 'Nomination_Hollande.txt', 'Nomination_Macron.txt', 'Nomination_Mitterrand1.txt', 'Nomination_Mitterrand2.txt', 'Nomination_Sarkozy.txt']


def supprime_doublon(tab): # Fonction utilisée juste après pour surpprimer les doublons de notre liste de noms
    sans_doublon = []
    for nom in tab:
        if nom not in sans_doublon:
            sans_doublon.append(nom)
    return sans_doublon

assert supprime_doublon([3,4,5,6,3,6]) == [3,4,5,6] #Test permettant de vérifier si la fonction est bonne
assert supprime_doublon([3,4,5,5,6,3,6,5,1]) == [3,4,5,6,1]
assert supprime_doublon([4,3,3,3,3,4,4,4,5]) == [4,3,5]

# Création de la fonction qui permet de remplacer un caractere dans un mot
def remplacer(mot, character, caractere_nouveau):
    new = ""
    for i in range(len(mot)): # Boucle qui parcourt tout le mot
        if mot[i] == character: # Si le caractere du mot est égale au caractere que l'on veut remplacer
            new += caractere_nouveau # Alors on ajoute ce caractère au nouveau mot
        else:
            new += mot[i] # Sinon on écrit juste le caractère à la position i
    return new

assert remplacer("Je suis la", "s", "k") == "Je kuik la"


def noms_presidents(): # Récupère les noms des présidents et supprime tout les nombres et les types des fichiers
    liste_présidents = []
    nom = list_of_files("./speeches")
    for fichiers in nom:
        fichiers = fichiers[11:][:-4]
        for car in fichiers :
            if 48<=ord(car)<=57 :
                fichiers = remplacer(fichiers,car,"")
        liste_présidents.append(fichiers)
    liste_présidents = supprime_doublon(liste_présidents) # Appele de notre fonction créee précédement 
    return liste_présidents

assert noms_presidents() == ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy'] # Test la fonction  noms_presidents


def prenoms_présidents(): # Associe les noms des présidents à leurs prénoms
    prenoms_noms = { "Giscard dEstaing" : "Valérie",
                    "Macron" : "Emmanuel",
                    "Chirac" : "Jacques",           # --> On le créer son forme de dictionnaire
                    "Hollande" : "François",
                    "Mitterrand" : "François",
                    "Sarkozy" : "Nicolas"}
    return prenoms_noms

def minuscules(mot):
    nouveau_mot = ""
    for i in range(len(mot)):
        lettre = mot[i]
        valeur = ord(lettre)
        if valeur >= 65 and valeur <= 90:
            valeur += 32
            lettre_minuscules = chr(valeur)
            nouveau_mot += lettre_minuscules
        else:
            nouveau_mot += lettre
    return nouveau_mot

assert minuscules("Axel") == "axel" #Test permettant de vérifier si la fonction minuscules marche
assert minuscules("Je M aPpElLe AxEl") == "je m appelle axel"

# Fonction permettant de supprimertout les caractères de ponctuation
def ponctuation(mot):
    ponctuaList = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~" # Liste des caractères à supprimer
    mot_del = "" # Nouveaux mot sans les caractères de ponction
    for i in range(len(mot)): # Boucle qui parcourt tout le mot
        if mot[i] in ponctuaList :  # Si la lettre du mot est dans "ponctuaList"
            mot_cleaned = " " # On ajoute un espace
            mot_del += mot_cleaned 
        else: # Si il n'est pas pas dans  "ponctuaList"
            mot_del += mot[i] # On ajoute juste la lettre
    return mot_del # On return le mot sans les caracteres de ponctuation

assert ponctuation("je suis l'eau qu'il boit.") == "je suis l eau qu il boit " # Test le foction ponctuation

def cleaned():
    # Lister tous les fichiers dans le répertoire 'speeches'
    liste = supprime_doublon(list_of_files("./speeches"))
    for nom_fichiers in liste: # Permet de lire tout les noms des fichiers
        with open("./speeches/" + nom_fichiers, "r") as f:
            contenu = f.read() # li le fichier
        contenu_minuscule = minuscules(contenu) # La fonction minuscules permet de convertir les caractères en caractères minuscules
        contenu_cleaned = ponctuation(contenu_minuscule)
        # Créer un nouveau fichier dans le répertoire 'cleaned'
        with open("./speeches/Cleaned" + nom_fichiers, "w") as nouveau_fichier: # Création des nouveaux fichiers
            nouveau_fichier.write(contenu_cleaned)
    return nouveau_fichier

cleaned()

""" Partie création de l'algorithme TF-IDF """

# Créer une fonction permettant de convertir un texte en un tableau de mot

def tableau_chaine_caractere(texte):
    # La méthode split permet de séparer les mots lorqu'il y a un espace et les convertit en tableau
    mots = texte.split() 
    return mots

assert tableau_chaine_caractere("je suis la je suis present") == ['je', 'suis', 'la', 'je', 'suis', 'present']

# Créer la fonctions qui permet de trouver les mots en occurrences du texte
def occurences(tableau):
    occurences = {} # Créer un dictionnaire pour stocker chaque mots (Keys) avec sont nombres d'occurences ( values )
    for i in range(len(tableau)): # Parcourt tout les éléments du tableau
        if tableau[i] not in occurences: # Si la clef n'est pas encore attribuiée dans le dictionnaire
            occurences[tableau[i]] = 1
        else: # Si la clef est déjà assigniée dans le dictionnaire
            occurences[tableau[i]] += 1 # Ajoute 1 à l'occurence
    return occurences
            

assert occurences(['je', 'suis', 'la', 'je', 'suis', 'present']) == {'je': 2, 'suis': 2, 'la': 1, 'present': 1}