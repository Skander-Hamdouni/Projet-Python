#Import de la bibliotheque os
import os
import math
import random

# Code donné par le sujet permettant de récupérer les noms des fichiers prend en paramètre un chemin
def list_of_files(directory):
    files_names = [] # Créer le tableau des noms récupérer
    for filename in os.listdir(directory):  # Parcours tout les fichiers
        if filename[-4:] == ".txt": # Vérifie que le fichier soit bien un fichier texte
            files_names.append(filename) 
    return files_names # renvoi un tableau de chaîne de caractère

# Test la fonction list_of_files
#assert list_of_files('./speeches') == ['Nomination_Chirac1.txt', 'Nomination_Chirac2.txt', 'Nomination_Giscard dEstaing.txt', 'Nomination_Hollande.txt', 'Nomination_Macron.txt', 'Nomination_Mitterrand1.txt', 'Nomination_Mitterrand2.txt', 'Nomination_Sarkozy.txt']
files_name = list_of_files('./speeches')
Nombre_fichiers = len(files_name)

# Dictionnaire de test

dict_test = {
            "jean" : 5,
             "pierre" : 1,
             "Yves" : 5 }

"""                                                                     """
"""           Première parti, création des fonctions de base            """
"""                                                                     """

# Fonction utilisée juste après pour surpprimer les doublons de notre liste de noms, prend un tableau en argument
def supprime_doublon(tab): 
    sans_doublon = [] # Créer le nouveau tableau sans doublons
    for nom in tab:
        if nom not in sans_doublon: # Si le mot n'est pas das le nouveau tableau on l'ajoute, s'il y est déjà on ne fait rien
            sans_doublon.append(nom)
    return sans_doublon # Renvoi un tableau

#Test permettant de vérifier si la fonction marche correctement
#assert supprime_doublon([3,4,5,6,3,6]) == [3,4,5,6] 
#assert supprime_doublon([3,4,5,5,6,3,6,5,1]) == [3,4,5,6,1]
#assert supprime_doublon([4,3,3,3,3,4,4,4,5]) == [4,3,5]

# Création de la fonction qui permet de remplacer un caractere dans un mot, prend en argument un mot, le caractère que l'on change et le caractère par lequel on le change
def remplacer(mot, character, caractere_nouveau):
    new = "" # Sera le nouveau mot
    for i in range(len(mot)): # Boucle qui parcourt tout le mot
        if mot[i] == character: # Si le caractere du mot est égale au caractere que l'on veut remplacer
            new += caractere_nouveau # Alors on ajoute ce caractère au nouveau mot
        else:
            new += mot[i] # Sinon on écrit juste le caractère à la position i
    return new # Renvoi une chaine de caractère

# Test de la fonction
#assert remplacer("Je suis la", "s", "k") == "Je kuik la"

# Récupère les noms des présidents et supprime tout les nombres et les types des fichiers
def noms_presidents(): 
    liste_présidents = [] # Initialise un tableau vide
    nom = list_of_files("./speeches")
    for fichiers in nom: # Parcours tout les fichiers
        fichiers = fichiers[11:][:-4] # Supprime la ponctuation et le format ( .txt )
        for car in fichiers : # Parcours tout les caractères du mot
            if 48<=ord(car)<=57 : # Supprime les chiffres
                fichiers = remplacer(fichiers,car,"") # Et les espaces
        liste_présidents.append(fichiers)
    liste_présidents = supprime_doublon(liste_présidents) # Appele de notre fonction créee précédement 
    return liste_présidents # Renvoi un tableau

#assert noms_presidents() == ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy'] # Test la fonction  noms_presidents


# Récupère les noms des présidents et supprime tout les nombres et les types des fichiers, prend en argument un tableau
def Liste_noms_presidents(Liste): 
    liste_présidents = []  # Tableau qui récupère les noms
    for fichiers in Liste: # Parcours tout les noms de fichiers
        fichiers = fichiers[19:][:-4] # garde seulment le nom ( supprime le .txt et le Nomination_ )
        for car in fichiers :
            if 48<=ord(car)<=57 : # permet de supprimer les chiffres
                fichiers = remplacer(fichiers,car,"") # En les remplacant par des espaces
        liste_présidents.append(fichiers)
    liste_présidents = supprime_doublon(liste_présidents) # Appele de notre fonction créee précédement 
    return liste_présidents # renvoi un tableau composé de chaîne de caractère

# Test de la fonction
#assert Liste_noms_presidents(files_name) == ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']

# Associe les noms des présidents à leurs prénoms
def prenoms_présidents(nom): 
    prenoms_noms = { "Giscard dEstaing" : "Valérie",
                    "Macron" : "Emmanuel",
                    "Chirac" : "Jacques",           # --> On le créer son forme de dictionnaire
                    "Hollande" : "François",
                    "Mitterrand" : "François",
                    "Sarkozy" : "Nicolas"}
    return prenoms_noms[nom] # renvoi le prénom du président

# Test de la fonction 
#assert prenoms_présidents("Macron") == "Emmanuel"

# Permet de convertir un mot composé de majuscules en un mot composé que de minuscules, prend en argument un mot
def minuscules(mot):
    nouveau_mot = "" # initialisation du nouveau mot
    for i in range(len(mot)): # Parcourt tout le mot
        lettre = mot[i]
        valeur = ord(lettre)
        if valeur >= 65 and valeur <= 90: # Si le code ASSCI de la lettre est compris entre ces valeurs
            valeur += 32 # Alors on lui ajoute 32 pour le tranformer en minuscules
            lettre_minuscules = chr(valeur)
            nouveau_mot += lettre_minuscules # Puis on l'ajoute à notre chaîne de caractère
        else:
            nouveau_mot += lettre # Si la lettre est déjà minuscule on l'ajoute directement à notre chaîne de caractère
    return nouveau_mot # Renvoi une chaîne de caractère 

#Test permettant de vérifier si la fonction minuscules marche
#assert minuscules("MartiN") == "martin" 
#assert minuscules("Je M aPpElLe MaRtIn") == "je m appelle martin"

# Fonction permettant de supprimertout les caractères de ponctuation
def ponctuation(texte):
    # Liste de ponctuations à supprimer, sans l'apostrophe et le trait d'union
    ponctuaList = "!#$%&()*+,./:;<=>?@[]^_`{|}~"
    
    # Remplacer les contractions spécifiques
    texte = texte.replace("n'", "ne ")
    texte = texte.replace("j'", "je ")
    texte = texte.replace("d'","du ")

    # Traiter les contractions "l'"
    new_texte = ""
    i = 0
    while i < len(texte):
        if texte[i:i+2] == "l'" or texte[i:i + 2] == "L'":  # Recherche de la contraction "l'" et "L'"
            # Choisir aléatoirement entre "le " et "la "
            new_texte += random.choice(["le ", "la "])
            i += 2  # Passer l'apostrophe et le caractère suivant
        else:
            new_texte += texte[i]
            i += 1
    texte = new_texte
    
    # Remplacer les traits d'union par des espaces
    texte = texte.replace('-', ' ')
    
    # Supprimer les autres caractères de ponctuation
    texte_propre = ""
    for char in texte:
        if char not in ponctuaList:
            texte_propre += char
        else:
            texte_propre += ' '

    # Supprimer les espaces superflus
    texte_propre = " ".join(texte_propre.split())
    
    return texte_propre

def cleaned_fichier():
    # Lister tous les fichiers dans le répertoire 'speeches'
    liste = supprime_doublon(list_of_files("./speeches"))
    for nom_fichiers in liste: # Permet de lire tout les noms des fichiers
        with open("./speeches/" + nom_fichiers, "r", encoding='utf-8') as f:
            contenu = f.read() # li le fichier
        contenu_minuscule = minuscules(contenu) # La fonction minuscules permet de convertir les caractères en caractères minuscules
        contenu_cleaned = ponctuation(contenu_minuscule)
        # Créer un nouveau fichier dans le répertoire 'cleaned'
        with open("./speeches/Cleaned/" + 'Cleaned_' + nom_fichiers, "w", encoding='utf-8') as nouveau_fichier: # Création des nouveaux fichiers
            nouveau_fichier.write(contenu_cleaned)
    return nouveau_fichier

cleaned_fichier()

# Création de la fonction Cleaned qui prend en argument un texte et qui le nettoi de sa ponctuation et de ces majuscules
def cleaned(texte):
    contenu_minuscule = minuscules(texte) # La fonction minuscules permet de convertir les caractères en caractères minuscules
    contenu_cleaned = ponctuation(contenu_minuscule) # Appel de la fonction qui supprime la ponctuation
    return contenu_cleaned # renvoi une chaîne de caractère


"""                                                               """
"""        Partie début de création de l'algorithme TF-IDF        """
"""                                                               """


# Créer une fonction permettant de convertir un texte en un tableau de mot
def tableau_chaine_caractere(texte):
    mots = [] # Initialise un tableau vide
    mot_actuel = '' # Initialise une chaîne de caractère vide
    for caractere in texte: # Parcours tout les mots du texte
        if caractere != ' ': # Si le caractère n'est pas un espace 
            mot_actuel += caractere # On l'ajoute à notre mot
        else:
            mots.append(mot_actuel) # Sinon ajoute le mot à la liste 
            mot_actuel = ''
    mots.append(mot_actuel)  # Ajoute le mot à la liste    
    return mots # Renvoi un tableau de mot

# Test de la fonction
#assert tableau_chaine_caractere("je suis la je suis present") == ['je', 'suis', 'la', 'je', 'suis', 'present']

# Créer la fonctions qui permet de trouver les mots en occurrences du texte
def occurences(tableau):
    occurences = {} # Créer un dictionnaire pour stocker chaque mots (Keys) avec sont nombres d'occurences ( values )
    for i in range(len(tableau)): # Parcourt tout les éléments du tableau
        if tableau[i] not in occurences: # Si la clef n'est pas encore attribuiée dans le dictionnaire
            occurences[tableau[i]] = 1 # On l'initialise à 1
        else: # Si la clef est déjà assigniée dans le dictionnaire
            occurences[tableau[i]] += 1 # Ajoute +1 à l'occurence
    return occurences # Renvoi un dictionnaire où chaque mot et une keys et chaque score est une values
            
# Test de la fonction
#assert occurences(['je', 'suis', 'la', 'je', 'suis', 'present']) == {'je': 2, 'suis': 2, 'la': 1, 'present': 1}

# Fonction permettant de lire le contenu de tout les fichiers en même temps, ne prend aucun argument
def FileUnited():
    contenu = ""
    for afile in list_of_files("./speeches/Cleaned") : # Permet de parcourir tout les noms des fichiers cleaned
        with open("./speeches/Cleaned/" + afile,"r",encoding="utf-8" ) as f: # Parcour tout les fichiers
            contenu += f.read() # li le fichier
        mot = tableau_chaine_caractere(contenu) # Convertit le contenu en chaîne de caractère
    return mot # Renvoi un tableau


# Fonction qui permet de lire le contenu d'un seul fichier
def ContenuToTable(filename) :
    with open ("./" + filename, "r", encoding= "utf-8") as f: # Encoding utf-8 permet que toutes les lettres s'affichent correctment sans caractère special
        contenu = f.read()
    mot = tableau_chaine_caractere(contenu) # Permet de convertir le texte du fichier en un tableau de mot
    return mot # Renvoi un tableau

# Fonction qui permet de savoir si un mot_rechercher est présent dans un fichier
def presence(nom_fichier, mot_recherche):
    with open(nom_fichier, "r", encoding="utf-8") as fichier: # Permet lire le fichier choisi
        for ligne in fichier: # Parourt toutes les lignes du texte
            mots = tableau_chaine_caractere(ligne) # Converti le mot en un tableau
            for mot in mots: # Parcourt tout les mots du tableau
                if mot == mot_recherche: # Si le mot qu'on cherche est dans le tableau 
                    return True # Renvoi un booléen
    return False # Renvoi un booléen


"""                                                   """
"""                  Création TF                      """
"""                                                   """

# Fonction TF qui prend en paramètre un chemin et un mot, permet de trouver le nombre d'occurrence d'un seul mot dans un fichier
def TF(directory, mot) :
    count = 0 # Intialisation de notre compteur d'occurrence
    with open (directory, "r", encoding = "utf-8") as f: # Parcour le fichier
        contenu = f.read()
        mots = contenu.split()
        for item in mots : # Pour tout les éléments du tableau mots
            if item == mot : # Si la valeur du tableau est égale au mot que l'on cherche 
                count += 1 # +1 à notre compteur d'occurrence
        return count # Renvoi un entier
    
# Test de la fonction
#assert TF("./speeches/Cleaned/Cleaned_Nomination_Sarkozy.txt", "veut" ) == 14

# Création de TFListe qui prend en argument directement un tableau de mot et qui cherche un mot dans ce tableau
def TFliste (Liste, mot) : 
    count = 0 # Initialisation du compteur 
    for item in Liste : # Parcour tout le tableau
        if item == mot : # Si la valeur du tableau est égale au mot qu'on cherche
            count += 1 # +1 au compteur
    return count # Renvoi un entier

# Test de la fonction
#assert TFliste(['bonjour','salut','bonjour','aurevoir'],'bonjour') == 2


"""                                      """
"""           La matrice TF-IDF          """
"""                                      """

# Fonction qui créer la matrice TF-IDF et prend en argument un chemin
def matrice_tfidf(directory): 
    matrice = []  # Liste pour stocker les données
    tab_fichiers = list_of_files(directory)  # Récupère le noms des fichiers
    nb_fichiers = len(tab_fichiers) # Compte le nombre de fichier 
    
    # Dictionnaire pour stocker les scores TF-IDF de chaque mot dans chaque fichier
    tfidf_dict = {}
    
    for i, fichier_nom in enumerate(tab_fichiers): # Emurate permet de conserver l'indice et la valeur de cette indice
        with open(os.path.join(directory, fichier_nom), "r", encoding="utf-8") as fichier: # Permet de lire les fichiers
            for ligne in fichier: 
                enleve = tableau_chaine_caractere(ligne) # Converti lles lignes du fichier en un tableau
                mots_comptes = set() # Comme dans un dictionnaire, set permet que chaque éléments soit unique et immuable
                for mot in enleve:  # Parcourt tout les mots du tableau
                    mot = mot.strip() 
                    
                    if mot not in mots_comptes: # si notre mot n'est pas présent dans mots_comptes
                        if mot not in tfidf_dict: # Si en plus il n'est pas dans e dictionnaire
                            tfidf_dict[mot] = [0.0] * nb_fichiers # On initialise le mot dans le dictionnaire et on lui assigne la valeur 0.0 pour tout les fichiers
                        
                        # Calcule le score TF
                        tf = TF(os.path.join(directory, fichier_nom), mot)
                        
                        # Calcule le score IDF
                        somme = sum(presence(os.path.join(directory, tab_fichiers[j]), mot) for j in range(nb_fichiers)) # Calcul IDF par compréhension

                        if somme != 0: # Si IDF est différent de 0
                            score_idf = round(math.log10(nb_fichiers / somme), 3) # On applique la formule du sujet
                        else:
                            score_idf = 0.0 # Sinon on note la valeur de 0
                        
                        # Calcule le score TF-IDF
                        tfidf = round(tf * score_idf, 3) # Calcul arrondi à 0.001 près
                        
                        tfidf_dict[mot][i] = tfidf # Entre le score TF-IDF dans le dictionnaire
                        mots_comptes.add(mot) # Ajoute le mot dans les mots compté
    
    for mot in tfidf_dict: # Parcourt toutes les keys du dictionnaire
        matrice.append([mot] + tfidf_dict[mot]) # Ajoute à la matrice le mot + le score TF-IDF
    
    return matrice # Renvoi un tableau de tableau


def matrice_tfidf_Vecteur(directory): 
    matrice = []  # Liste pour stocker les données
    tab_fichiers = list_of_files(directory) 
    nb_fichiers = len(tab_fichiers) 
    
    # Dictionnaire pour stocker les scores TF-IDF de chaque mot dans chaque fichier
    tfidf_dict = {}
    
    for i, fichier_nom in enumerate(tab_fichiers): 
        with open(os.path.join(directory, fichier_nom), "r", encoding="utf-8") as fichier: 
            for ligne in fichier: 
                enleve = tableau_chaine_caractere(ligne) 
                mots_comptes = set()
                for mot in enleve: 
                    mot = mot.strip() 
                    if mot not in mots_comptes:
                        if mot not in tfidf_dict:
                            tfidf_dict[mot] = [0.0] * nb_fichiers
                        
                        # Calcule le score TF
                        tf = TF(os.path.join(directory, fichier_nom), mot)
                        
                        # Calcule le score IDF
                        somme = sum(presence(os.path.join(directory, tab_fichiers[j]), mot) for j in range(nb_fichiers))
                        if somme != 0:
                            score_idf = round(math.log10(nb_fichiers / somme), 3) #vérifiée 
                        else:
                            score_idf = 0.0
                        
                        # Calcule le score TF-IDF
                        tfidf = round(tf * score_idf, 3)
                        
                        tfidf_dict[mot][i] = tfidf
                        mots_comptes.add(mot)
    
    for mot in tfidf_dict:
        matrice.append(tfidf_dict[mot])
    
    return matrice

# Création pour que l'affichage de la matrice soit joli, prend en paramètre une matrice
def print_matrice(matrice):
    for sous_tableau in matrice: # Parcourt tout les sous tableau
        print(sous_tableau) # Et les affiche un à un 

#matrice = matrice_tfidf('./speeches/Cleaned/')
#print(matrice)
#matrice_tf_idf = print_matrice(matrice)
#print(matrice_tf_idf)

"""                                                                 """
"""     Création des fonctions de 'test' de la matrice TF-IDF       """
"""                                                                 """

# FOnction qui trouve tout les mots ayant un score TF-IDF égale à 0, prend un tableau de tableau e argument
def score_tfidf_0(TableauDeTableau):
    n = len(TableauDeTableau)
    new_tab = [] # Initialisation de notre tableau
    somme = 0
    for i in range(n): 
        for j in range (1, len(TableauDeTableau[i])) : # Commence à l'indice 1 pour exclure la colonne des mots
            somme += TableauDeTableau[i][j] # Permet de faire la somme d'une ligne 
        if somme == 0 :
            new_tab.append(TableauDeTableau[i][0]) # SI somme = 0 alors on l'ajoute à notre tableau
        somme = 0  # On réinitialise la somme à 0 
    return new_tab # Renvoi un tableau

# Test de la fonction
#assert score_tfidf_0(matrice) == ['messieurs', 'les', '', 'mesdames', 'en', 'ce', 'je', 'la', 'de', 'l', 'une', 'a', 'france', 'qui', 'se', 'et', 'dans', 'le', 'peuple', 'aux', 'que', 'son', 'histoire', 'pour', 'qu', 'par', 'des', 'j', 'il', 'est', 'mais', 'faire', 'du']

# Fonction qui trouve les mots ayant le socre TF-IDF le plus élevé, prend en argument une matrice
def mots_tfidf_max(matrice_tfidf):
    mots_max = [] # Initialisation du tableau générale
    
    for i in range(1, len(matrice_tfidf[0])):  # Commence à l'indice 1 pour exclure la colonne des mots
        mots_max_fichier = [] # Initialisation du tableau spécifique à un seul fichier
        score_max = 0.0 # On part du principe que le score le plus élevé est 0
        
        for ligne in matrice_tfidf: # Parcourt les lignes de la matrice
            mot = ligne[0]
            score_tfidf = ligne[i]
            
            if score_tfidf > score_max: # Si la valeur du sous tableau  > que valeur max donc 0.0 dans notre cas de base
                mots_max_fichier = [mot]  #
                score_max = score_tfidf   # --> on change les valeurs maximum
            elif score_tfidf == score_max:
                mots_max_fichier.append(mot) # SI un mot à le même score que le maximum, alors on l'ajoute aussi au tableau
        
        mots_max.append(mots_max_fichier) # On ajoute dans le tableau générale tout les sous tableau crée précedemment
    
    return mots_max # Renvoi un tableau de tableau

# Test de vérification de la faonction
#assert mots_tfidf_max(matrice) == [['voudrais'], ['doit'], ['president'], ['avant'], ['À'], ['ville'], ['obligation', 'faut'], ['pense']]

# Fonction qui permet de trouver quel est / quels sont les mots plus répétés par UN président, cette fonction prend le noms d'un président en argument
def recurrence_mot_presidents(president) : 
    Ordre = { "Chirac" : [0,1], "Giscard dEstaing" : [2],
              "Hollande" : [3], "Macron" : [4],              # ---> dictionnaire des noms et leurs fichiers associés
                "Mitterrand" : [5,6],"Sorkozy" : [7]}
    postdict = Ordre.get(president, None) # Permet de trouver la liste d'indice associé au nom, si le nom n'existe pas elle renvoi None
    resultat = []
    for item in postdict :  # Pour toutes les valeurs de postdict
        resultat.append(mots_tfidf_max(matrice_tfidf("./speeches/Cleaned/"))[item]) # Note dans un tableau les mots les plus répété ( donc score TF-IDF élevé ) d'un président 
    return resultat # Renvoi un tableau de tableau ou juste un tableau en fonctin du nombre de fichier 

# Test de la fonction
#assert recurrence_mot_presidents("Chirac") == [['voudrais'], ['doit']]

# Fonction qui permet de trouver quels présidents ont évoqué un certain mot, prend en argument un mot
def mot_evoque(mot) :
    tab = list_of_files("./speeches/Cleaned/") 
    Liste = []
    maxi = ""
    count = 0
    for file in tab : # Trouve tout les noms des fichiers
        with open (os.path.join("./speeches/Cleaned/" + file), "r", encoding="utf-8") as fichier:  # Li ces fichiers
            scoreTF = TF("./speeches/Cleaned/" + file, mot) # Caclcule le socre TF du mot dans chque fichier
            if scoreTF != 0 : 
                if scoreTF > count : # si le score TF est supérieur à notre compte
                    maxi = file  # le maxi devient notre fichier
                    count = scoreTF # et le compte devient notre nombre d'occurence
                Liste.append(file) # on ajoute le nom du fichier à la liste
    Liste = "Les présidents qui ont parlé de " + str(mot) + " sont " + str(Liste_noms_presidents(Liste))  # ---> permet l'affichage
    maxi = "Celui qui en a le plus parlé c'est ", str(Liste_noms_presidents([maxi]))                      # ---> permet l'affichage
    return Liste, maxi # renvoi une chaine de caractère

# Fonction qui permet de trouver quel est le président qui a le plus parlé d'écologie
def ecologie() : 
    mots = ["climat"] # Liste de mot
    Liste = []
    tab = list_of_files("./speeches/Cleaned/") 
    for mot in mots : # Parcour tout les mots de la liste
        for file in tab : # Parcour le nom de tout les fichiers
            with open (os.path.join("./speeches/Cleaned/" + file), "r", encoding="utf-8") as fichier:  # Li les fichiers
                scoreTF = TF("./speeches/Cleaned/" + file, mot) # Calucle le score TF de notre mot du tableau
                if scoreTF != 0 :
                    Liste.append(file) # Ajoute le score à notre nouveau tableau
        Liste = "Les présidents qui ont parlé de " + str(mot) + " sont " + str([Liste_noms_presidents(Liste)]) # Affiche les noms des présidents qui ont le plus pronnoncé ces mots
    return Liste # Renvoi une chaîne de caractère

# Test de la focntion
#assert ecologie() == "Les présidents qui ont parlé de climat sont [['Macron']]"

# Fonction qui trouve quels sont les mots qui ont le plus petit score TF-IDF, prend en argument une matrice
def mots_tfidf_min(matrice_tfidf):
    mots_min = []
    for i in range(1, len(matrice_tfidf[0])):  # Commence à l'indice 1 pour exclure la colonne des mots
        mots_min_fichier = []
        score_min = float('inf')  # Initialise avec une valeur infinie
        for ligne in matrice_tfidf: # parcour les lignes de la matrice
            mot = ligne[0]
            score_tfidf = ligne[i]
            if score_tfidf < score_min: # si le score est inférieur à notre minimum
                mots_min_fichier = [mot]
                score_min = score_tfidf # Alors ce socre devient le minimum
            elif score_tfidf == score_min: # si le score est égale au minimum, alors on l'ajoute au tableau
                mots_min_fichier.append(mot)
        mots_min.append(mots_min_fichier)
    return mots_min # Renvoi un tableau 


"""                                              """
""" Partie traitemant de la question utilisateur """
"""                                              """

# Fonction permettant de convertir notre question en un tableau de mot, ces mots sont préalablement nettoyés
def tokenisation_question(chaine_caractere): 
    new_chaine = cleaned(chaine_caractere)    # Nettoi la question
    tab = tableau_chaine_caractere(new_chaine)  # Converti la question en chaîne de caractère
    return tab # Renvois un tableau 

#assert tokenisation_question("Je suis là je suis présent") == ['je', 'suis', 'là', 'je', 'suis', 'présent']

# Focntion qui permet de trouver les mots en communs entre notre matrice TF-IDF et la question de l'utilisateur
def intersection_question_text(tableau, directory):  # ---> paramètres : tableau ( notre question ) et un chemin pour calculer la matrices des documents
    doc = list_of_files(directory)
    mots_documents = set()

    # Créer un ensemble de tous les mots dans tous les documents
    for fichier in doc:
        with open(os.path.join(directory, fichier), 'r', encoding="utf-8") as f: # Li les fichiers de notre directory
            texte = f.read()
            nettoyer = cleaned(texte)
            tableau_nettoyer = tableau_chaine_caractere(nettoyer)
            mots_documents.update(tableau_nettoyer) # ajoute le tableau

    # Trouver l'intersection
    intersection = [mot for mot in tableau if mot in mots_documents] # Boucle par compréhension

    return intersection # Renvpi un tableau de mot

# Test de la fonction
#tab = ['pomme','je', 'suis', 'là', 'je', 'suis', 'présent','Carl']
#dirct = './speeches/Cleaned/'
#assert intersection_question_text(['pomme','je', 'suis', 'là', 'je', 'suis', 'présent','Carl'],'./speeches/') == ['je', 'suis', 'là', 'je', 'suis', 'présent']

# Fonction qui calcule le score TF-IDF de la question
def scorequestion(question):
    Matrice = [] # Initialisation de notre nouvelle matrice
    directory = "./speeches/Cleaned/"
    question = tokenisation_question(question) # Ici notre question est transformée sous forme de tableau
    tab_fichiers = list_of_files(directory)
    nb_fichiers = len(tab_fichiers)
    for mot in question: # Parcourt tout les mots de la question
        TF = TFliste(question, mot) # Trouve le score TF de tout les mots
        somme = sum(presence(os.path.join(directory, fichier), mot) for fichier in tab_fichiers) # Calcul le nombre de document dans lequel est présent le mot
        if somme != 0:
            score_idf = round(math.log10(nb_fichiers / somme), 3) # Calcul du score IDF
        else:
            score_idf = 0.0   # Si il apparaît nul part on l'initialise à 0
        tfidf = TF * score_idf # Calcul du score TF-IDF
        Matrice.append([mot, tfidf]) # Ajoute un sous-tableau [mot, tfidf] à la matrice
    return Matrice # Renvoi un tableau de sous-tableaux

# Test de la fonction
#question = "Comment allez vous ?"
#print(scorequestion(question))
#assert scorequestion(question) == ['comment', 0.903, 'allez', 0.0, 'vous', 0.204]

# Fonction qui permet de calculer le score TF de la question, prend en paramètre une question
def scorequestion(question, matrice):

    MatriceQuestion = []

    directory = "./speeches/Cleaned/"

    question = tokenisation_question(question)  # Suppose to tokenize the question

    tab_fichiers = list_of_files(directory)  # Suppose to list all files in the directory

    nb_fichiers = len(tab_fichiers)  

    # Pour chaque mot dans la matrice (chaque ligne représente un mot)

    for i in range(len(matrice)):

        mot = matrice[i][0]  # Le mot est le premier élément de chaque ligne

        if mot in question:

            TF = TFliste(question, mot)  # Calcul du TF pour le mot dans la question

            scores_idf = matrice[i][1:]  # Les scores IDF sont déjà calculés dans la matrice

            tfidf_scores = [TF * idf for idf in scores_idf]  # Multiplication du TF par chaque IDF

            MatriceQuestion.append(tfidf_scores)

        else:

            MatriceQuestion.append([0.0] * nb_fichiers)  # Zéros pour les mots non présents dans la question

    return MatriceQuestion # Renvoi une matrice


# Fonction qui réalise le produit scalaire entre 2 vecteurs
def scalaire(matrice1, matrice2):
    def scalaire(row1, row2):
        return sum(i * j for i, j in zip(row1, row2)) # Return un entier

    return sum(scalaire(row1, row2) for row1, row2 in zip(matrice1, matrice2))


# Fonction qui calcule la norme d'un vecteur 2D
def calcul_similarite(tfidf_question, tfidf_document, correspondance_question, correspondance_liste):
    tfidf_question_aligned = [0] * len(correspondance_liste)
    for i, mot in enumerate(correspondance_liste):
        mot_str = str(mot)  # Convertir le mot en chaîne de caractères
        if mot_str in correspondance_question: # Parcour tout les mots
            index_mot_question = correspondance_question.index(mot_str)
            tfidf_question_aligned[i] = tfidf_question[index_mot_question]

    dot_product = sum(q * d for q, d in zip(tfidf_question_aligned, tfidf_document))
    norm_question = sum(q ** 2 for q in tfidf_question_aligned) ** 0.5 # Calcul des normes
    norm_document = sum(d ** 2 for d in tfidf_document) ** 0.5

    if norm_question == 0 or norm_document == 0: # Si les 2 normes valent 0
        return 0

    cos_sim = dot_product / (norm_question * norm_document)
    return cos_sim # Renvoi un entier



# Focntion qui permet d'avoir les noms des fichiers nettoyé
def get_nom_fichier_cleaned(nom_fichier_corpus):
    """
    Retourne le nom équivalent dans le répertoire "./cleaned".

    Parameters:
    nom_fichier_corpus (str): Nom du fichier dans le corpus.

    Returns:
    str: Nom équivalent dans le répertoire "./cleaned".
    """
    nom_base = os.path.splitext(nom_fichier_corpus) # Supprime l'extension
    nom_fichier_cleaned = os.path.join("./speeches/Cleaned", nom_base + ".txt")
    return nom_fichier_cleaned # Renvoi un tableau

# Calcul le score TF-IDF de la question
def score_mot_question(question) :
    Matrice = []
    directory = "./speeches/Cleaned/"
    question = tokenisation_question(question)
    tab_fichiers = list_of_files(directory) 
    nb_fichiers = len(tab_fichiers) 
    for mot in question :  # Parcour tout les mots de la question
        TF = TFliste(question, mot) # Calcul le score TF des mots de la question
        somme = sum(presence(os.path.join(directory, tab_fichiers[j]), mot) for j in range(nb_fichiers))
        if somme != 0:
            score_idf = round(math.log10(nb_fichiers / somme), 3) # Scocre IDF
        else:
            score_idf = 0.0     # Sinon à 0.0
        tfidf = TF * score_idf # Score TF-IDF
        Matrice.append(mot)
        Matrice.append(tfidf)
    return Matrice  # Renvoi la matrice


# Fonction qui cherche le document le plus pertinent, paramètre, matrice, vecteur ( float ), directory
def doc_pertinent(liste_tf_idf_question, matrice, correspondance_question, correspondance_liste, correspondance_colonne):
    maxi = -float('inf') # Initialise une valeur à moins l'infini
    indice_doc = 0
    for colonne in range(len(matrice[0])): # Parcourt toutes les colonnes
        new_ligne = []
        for indice_mot in range(len(matrice)):
            new_ligne.append(matrice[indice_mot][colonne])
        calcul_sim = calcul_similarite(liste_tf_idf_question, new_ligne, correspondance_question, correspondance_liste) # Calcul de notre similarité
        if calcul_sim > maxi:
            maxi = calcul_sim
            indice_doc = colonne
    return f'{correspondance_colonne[indice_doc]}' # Return le nom d'un document

def trouver_correspondance_liste(matrice_tfidf):
    correspondance_liste = []
    for ligne in matrice_tfidf:
        mot = ligne[0]  # Le premier élément de chaque ligne est le mot
        correspondance_liste.append(mot)
    return correspondance_liste

def trouver_correspondance_colonne(chemin_dossier):
    # Liste pour stocker les noms des fichiers (ou toute autre référence aux documents)
    correspondance_colonne = []

    # Parcourir le dossier contenant les documents et ajouter chaque nom de fichier à la liste
    for nom_fichier in sorted(os.listdir(chemin_dossier)):
        if nom_fichier.endswith('.txt'):  # Assurez-vous de filtrer par le bon type de fichier
            correspondance_colonne.append(nom_fichier)

    return correspondance_colonne # Renvoi un tab

"""
correspondance_colonne = trouver_correspondance_colonne("./speeches/Cleaned/")
matrice = matrice_tfidf_Vecteur('./speeches/Cleaned/')
question = "que penses-tu de la france ?"
question_tfidf_test = scorequestion(question, matrice)
directory = './speeches/Cleaned/'
correspondance_liste = trouver_correspondance_liste(matrice)"""


#print(doc_pertinent(question_tfidf_test,matrice, question, correspondance_liste, correspondance_colonne))


def trouver_mot_score_max(score_mot_question):
    max_score = -float('inf') # Initialise une valeur infini
    mot_max = None

    # Parcourir la liste par paires (mot, score)
    for i in range(0, len(score_mot_question), 2):
        mot = score_mot_question[i]
        score = score_mot_question[i + 1]

        if score > max_score: # Si on trouve un socre plus élévé
            max_score = score
            mot_max = mot

    return mot_max # Renvoi un mot

def trouver_phrase_avec_mot(mot, chemin_document):
    # Ouvrir le document et lire son contenu
    with open('./speeches/Cleaned/' + chemin_document, 'r', encoding='utf-8') as fichier:
        contenu = fichier.readlines()
        for phrase in contenu:
            # Vérifier si le mot est dans la phrase
            if mot in phrase:
                # Retourner la phrase complète qui contient le mot
                return f"«{phrase}.»"
    return "Le mot n'a pas été trouvé dans le document." # Return une "erreur"

# Fonction qui génère une reponse
def generer_reponse(question, reponseV1, question_starters):
    # Trouver le mot de démarrage dans la question
    mot_debut = question.split()[0].rstrip('?:!')  # Supprime les signes de ponctuation
    # Obtenir la phrase d'introduction à partir du dictionnaire de démarrage de question
    introduction = question_starters.get(mot_debut, "")

    # Extraire la phrase contenant le mot clé du document
    phrase = reponseV1

    # Si aucune phrase n'est trouvée, renvoyer un message approprié
    if not phrase:
        return "Je suis désolé, je ne peux pas trouver l'information demandée." # Return une "erreur"

    # Construire la réponse complète
    reponse = f"{introduction}{phrase}"

    # Assurer que la réponse commence par une majuscule et se termine par un point
    reponse = reponse[0].upper() + reponse[1:]  # Met en majuscule la 1ère lettre
    if not reponse.endswith('.'): # Rajoute un point à la fin s'il y en a pas
        reponse += '.'

    return reponse # Renvoi chaine de caractère

# Création de notre fonction qui va permètre de génrer une reponse dans notre main, prend en argumnet une question
def answer(question):
    cleaned_fichier()
    score_mot_questionn = score_mot_question(question)
    mot = trouver_mot_score_max(score_mot_questionn)
    question_starters = {
    "Comment": "Après analyse, ",
    "Pourquoi": "Car, ",                            """ Appel de toutes nos fonctions pour répondre à la question"""
    "Peux-tu": "Oui, bien sûr!"
    }
    correspondance_colonne = trouver_correspondance_colonne("./speeches/Cleaned/")
    matrice = matrice_tfidf_Vecteur('./speeches/Cleaned/')
    question_tfidf = scorequestion(question, matrice)
    correspondance_liste = trouver_correspondance_liste(matrice)
    chemin = doc_pertinent(question_tfidf, matrice, question, correspondance_liste, correspondance_colonne)
    reponseV1 = (trouver_phrase_avec_mot(mot,chemin))
    answer = generer_reponse(question,reponseV1, question_starters)
    return answer # Return une chaine de caractère
