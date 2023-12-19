# Import de nos fonctions annexes créees précédement dans notre fichiers annexes
import Fonctions_annexes

# Import le bibbliothèque qui permet d'ouvrir une interface
from tkinter import * 

# Variable globale pour stocker la valeur de l'entrée
valeur_entree_globale = None

def creer_interface_input(fenetre, callback):
    def afficher_choix():
        global valeur_entree_globale
        valeur_entree_globale = str(entree.get()) # Permet d'entrer une valeur entre 1 et 2
        label_choix.config(text="Choix: " + str(valeur_entree_globale))
        callback(valeur_entree_globale) # Appel de notre fonction qui verifie si le valeur rentrée est bien 1 ou 2
        fenetre.destroy() # Permet de fermer automatiquement la fenêtre lorsqu'on clique sur valider

    entree = Entry(fenetre) # Permet à l'utilisateur de saisir du texte
    entree.pack()

    bouton = Button(fenetre, text="Valider", command=afficher_choix) # Création du bouton valider
    bouton.pack()

    label_choix = Label(fenetre) # Permet d'ouvrir la fenêtre 
    label_choix.pack()

def ouvrir_nouvelle_fenetre(callback):
    fenetre_2 = Toplevel()
    creer_interface_input(fenetre_2, callback)

    def quitter(): # Permet de quitter la fenêtre 
        print("Valeur saisie:", valeur_entree_globale) # Affiche la valeur que l'on a saisi
        fenetre_2.destroy()

    bouton_quitter = Button(fenetre_2, text="Quitter", command=quitter) # Permet de quitter la fenêtre lorsqu'on clique sur le bouton
    bouton_quitter.pack()

def traiter_choix(choix): # Permet de verifier que le nombre saisi soit bien 1 ou 2
    if choix in ["0", "1"]:
        print("Choix accepté:", choix)
        # Traitez le choix ici (par exemple, ouvrir une nouvelle fenêtre ou effectuer une action)

def traiter_choix_text(choix): 
    if isinstance(choix, str):
        print("Choix accepté:", choix)

def menu(): # Création du menu
    fenetre = Tk() # Création de la fenêtre
    
    fenetre.title("ChatBot") # Titre de notre fenêtre

    # Style personnalisé pour les labels
    style_label = {"font": ("Helvetica", 12), "borderwidth" : 2, "relief": "flat","wraplength" : -1,"anchor": "center"} # Stylisation de la fenêtre

    labels = [
        "Bienvenue dans ce ChatBot !",
        "Taper 0 pour poser des questions à notre ChatBot ",
        "Taper 1 pour obtenir des informations sur le ChatBot"
            ]

    for text in labels: # Boucle permettant de lire etd'afficher toutes les phrases dans notre fenêtre
        label = Label(fenetre, text=text, **style_label)
        label.pack()   
    
    creer_interface_input(fenetre, traiter_choix) # Appel notre fonction interface
    
    fenetre.mainloop()
    choix = valeur_entree_globale # Note la valeur entrée pour la comparer

    if choix == "0": # Conditions par rapport aux phrases précédentes
        fenetre = Tk()

        fenetre.title("Posez vos questions ! ")

        style_label = {"font": ("Helvetica", 12), "borderwidth" : 2, "relief": "flat","wraplength" : -1,"anchor": "center"}

        labels = [
            " Posez les questions que vous souhaitez "
        ]

        for text in labels:
            label = Label(fenetre,text = text,**style_label)
            label.pack()

        creer_interface_input(fenetre, traiter_choix_text)
        fenetre.mainloop()
        question = str(valeur_entree_globale)
        
        """appel la fonction qui traite le choix, donc la question"""
        
        reponse = Fonctions_annexes.answer(question) # Notre réponse

        fenetre1 = Tk()

        fenetre1.title(" Réponse ")

        style_label = {"font": ("Helvetica", 12), "borderwidth" : 2, "relief": "flat","wraplength" : -1,"anchor": "center"}

        label = [
            "Voici la réponse de notre ChatBot",
            str(reponse)
        ]

        for text in label:
            label = Label(fenetre1, text = text,**style_label)
            label.pack()

        fenetre.mainloop()

        menu()

    if choix == "1":

        fenetre = Tk()

        fenetre.title("Explications techniques du ChatBot")

        style_label = {"font": ("Helvetica", 12), "borderwidth" : 2, "relief": "flat","wraplength" : -1,"anchor": "center"}

        # Liste des textes pour chaque label
        texts = [
    "L'utilisation de ce chatbot est simple. Il suffit que vous posiez votre question et il tentera de vous répondre :)",
    "Une fois la question posée, il va analyser la question.",
    "Pour y répondre, le chatbot va parcourir sa base de donnée.",
    "Puis il va calculer la probabilité la plus élevée qu'un mot apparaisse pour répondre à cette question.",
    "Enfin, il générera la réponse la plus cohérente et la plus plausible.",
    "Pour sortir de ces explications, tapez 0.",
    "Si vous voulez encore plus d'informations, tapez 1."
                ]

        # Création et affichage de chaque label en utilisant une boucle
        for text in texts:
            label = Label(fenetre, text=text,**style_label)
            label.pack()
        
        
        creer_interface_input(fenetre, traiter_choix) # Même chose qu'au dessus
    
        fenetre.mainloop()
        choix = valeur_entree_globale
        print(choix)

        if choix == "0": # Permet de faire un retour en arrière
            menu()
        if choix == "1": 
            
            fenetre = Tk()

            fenetre.title("Informations sur le projet ChatBot")

            style_label = {"font": ("Helvetica", 12), "borderwidth" : 2, "relief": "flat","wraplength" : -1,"anchor": "center"}

            # Liste des textes pour chaque label
            texts = [
    "Ce chatbot a été créé pour notre projet du 1er semestre en Python.",
    "Ce projet a pour but de renforcer toutes nos compétences en Python.",
    "Si vous voulez encore plus de renseignements, nous vous invitons à consulter notre rapport sur le projet.",
    "Nous allons vous renvoyer au menu principal lorsque vous allez fermer la fenêtre."
                    ]

            # Création et affichage de chaque label en utilisant une boucle
            for text in texts:
                label = Label(fenetre, text=text,**style_label)
                label.pack()
            
            fenetre.mainloop()

            menu() # Retour en arrière

menu()




