#coding: utf8

import os
import mysql.connector as MC

# Ne prend rien en parametre, sert juste à "clear" le terminal
def clear_screen():
    # Si on est sur windows on fait un cls
    if os.name == 'nt':
        os.system('cls')
    else:
        # Sinon on fait un clear
        os.system('clear')

def demander_nom_marque():
    # Ne prend rien en parametre et renvoit l'id de la marque (un entier) d'une voiture demander au preable a l'utilisateur
    
    # On cree notre liste de marque
    tab_marque = ["Renault", "Peugeot", "Citroen", "Opel", "Dacia", "Volkswagen", "Audi", "Nissan"]
    marque_correcte = 0
    id_marque = -1
    print("Choisissez une marque parmi la liste ci-dessous :\n\n  Renault  |  Peugeot  |  Citröen  |  Opel  |  Dacia  |  Volkswagen  |  Audi  |  Nissan  \n")
    # Tant que l'utilisateur n'ecrit pas une marque correctement
    while marque_correcte == 0:
        # On demande une entree (une marque) a l'utilisateur
        entre_utilisateur = input(">>>>>  ")
        # On parcourt notre tableau de marque
        for i in range(0, len(tab_marque)):
            # Si on retrouve une marque
            if entre_utilisateur.lower() == tab_marque[i].lower():
                # On peut quitter la boucle
                marque_correcte = 1
                # On recupere l'indice
                id_marque = i+1
    # Et on le renvoit
    return id_marque

def demander_nom_modele(id_marque):
    # Prend en parametre l'id de la marque (un entier) car le modele depend de la marque
    # et renvoit l'id du modele 
    modele_correct = 0
    id_modele = id_marque
    # On cree notre liste de modele
    tab_modele = ["Arkana", "Austral", "Clio", "Citadine 108", "Berline 408", "Break 508 SW", "Ë-C4X", "C4X", "ë-Berlingo", "Ampera-e", "Astra", "Mokka", "Bigster", "Duster", "Logan", "Arteon", "Golf", "Polo", "A1", "A6 E-tron", "Rs6", "Ariya", "Juke", "Nt400 Cabstar"]
    tab_choix = []
    # Parmi tous ces modeles, on prend les 3 modeles assosies a la marque correspondante
    for i in range(0, 3):
        tab_choix.append(tab_modele[id_marque * 3 - (3 - i)])
    
    print(f"Choisissez un modele parmi la liste ci-dessous :\n\n  {tab_choix[0]}  |  {tab_choix[1]}  |  {tab_choix[2]}\n")
    # Tant que l'utilisateur n'ecrit pas un modele correctement
    while modele_correct == 0:
        # On demande une entree (un modele) a l'utilisateur
        entre_utilisateur = input(">>>>>  ")
        valeur = 0
        # On parcourt notre tableau de modele
        for i in range(0, len(tab_choix)):
            # Si on retrouve un modele
            if entre_utilisateur.lower() == tab_choix[i].lower():
                # On recupere l'indice
                valeur = i
                # On peut quitter la boucle
                modele_correct = 1
    id_modele = (id_modele*3) - (3 - valeur) + 1
    # Et on le renvoit
    return id_modele

def donner_couleur():
    # Ne prend rien en parametre et renvoit la couleur (une chaine de caractere) d'une voiture demander au preable a l'utilisateur
    couleur_correcte = 0
    # On cree notre liste de couleur
    tab_couleur = ["Rouge", "Bleu", "Vert", "Orange", "Jaune", "Rose", "Violet", "Blanc", "Noir", "Gris"]
    couleur_choisit = ""
    print("Choisissez une couleur parmi la liste ci-dessous :\n\n  Rouge  |  Bleu  |  Vert  |  Orange  |  Jaune  |  Rose  |  Violet  |  Blanc  |  Noir  |  Gris  \n")
    # Tant que l'utilisateur n'ecrit pas une couleur correctement
    while couleur_correcte == 0:
        # On demande une entree (une couleur) a l'utilisateur
        entre_utilisateur = input(">>>>>  ")
        # On parcourt notre tableau de couleur
        for c in tab_couleur:
            # Si on retrouve une couleur
            if entre_utilisateur.lower() == c.lower():
                # On recupere la couleur
                couleur_choisit = c
                # On peut quitter la boucle
                couleur_correcte = 1
    # Et on la renvoit
    return couleur_choisit

def donner_lieu():
    # Ne prend rien en parametre et renvoit la localisation (une chaine de caractere) d'une voiture demander au preable a l'utilisateur
    ville_correcte = 0
    # On cree notre liste de ville
    tab_ville = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille",
    "Rennes", "Reims", "Saint-Étienne", "Toulon", "Le Havre", "Grenoble", "Dijon", "Angers", "Nimes", "Clermont-Ferrand", "Rouen"]
    
    ville_choisit = ""
    print("Choisissez une ville parmi la liste ci-dessous :\n\n  Paris  |  Marseille  |  Lyon  |  Toulouse  |  Nice  |  Nantes  |  Montpellier  |  Strasbourg  |  Bordeaux  |  Lille  |  Rennes  |  Reims  |  Saint-Étienne  |  Toulon  |  Le Havre  |  Grenoble  |  Dijon  |  Angers  |  Nimes  |  Clermont-Ferrand  |  Rouen\n")
    # Tant que l'utilisateur n'ecrit pas une ville correctement
    while ville_correcte == 0:
        # On demande une entree (une ville) a l'utilisateur
        entre_utilisateur = input(">>>>>  ")
        # On parcourt notre tableau de ville
        for v in tab_ville:
            # Si on retrouve une ville
            if entre_utilisateur.lower() == v.lower():
                # On recupere la ville
                ville_choisit = v
                # On peut quitter la boucle
                ville_correcte = 1
    # Et on la renvoit
    return ville_choisit

def donner_kilometrage():
    # Ne prend rien en parametre et renvoit le kilometrage (un entier) d'une voiture demander au preable a l'utilisateur
    valeur_correcte = 0
    print("Entrez un kilometrage : \n")
    # Tant que l'utilisateur n'ecrit pas le kilometrage correctement
    while valeur_correcte == 0:
        try:
            # On demande une valeur a l'utilisateur
            entre_utilisateur = input(">>>>>  ")
            # On convertit cette valeur en int
            kilometrage = int(entre_utilisateur)
            # Si la valeur respecte la condition (une valeur positif)
            if(kilometrage >= 0):
                # On peut quitter la boucle
                valeur_correcte = 1
        # Si la valeur n'est pas convertissable en entier
        except ValueError:
            print("Vous devez entrer une valeur positive")
    # Et on le renvoit
    return kilometrage

def donner_prix():
    # Ne prend rien en parametre et renvoit le prix (un reel positif, un float) d'une voiture demander au preable a l'utilisateur
    valeur_correcte = 0
    print("Entrez un prix (tapez point '.' pour mettre une virgule) : \n")
    # Tant que l'utilisateur n'ecrit pas le prix correctement
    while valeur_correcte == 0:
        try:
            # On demande une valeur a l'utilisateur
            entre_utilisateur = input(">>>>>  ")
            # On convertit cette valeur en float
            prix = float(entre_utilisateur)
            # Si la valeur respecte la condition (une valeur positif strictement, on va avoir des voitures gratos non plus)
            if(prix > 0):
                # On peut quitter la boucle
                valeur_correcte = 1
        # Si la valeur n'est pas convertissable en float
        except ValueError:
            print("Vous devez entrer une valeur positive")
    # Et on le renvoit
    return prix

def donner_annee():
    # Ne prend rien en parametre et renvoit l'annee (un entier) d'une voiture demander au preable a l'utilisateur
    valeur_correcte = 0
    print("Entrez l'annee de la voiture : \n")
    # Tant que l'utilisateur n'ecrit pas l'annee correctement
    while valeur_correcte == 0:
        try:
            # On demande une valeur a l'utilisateur
            entre_utilisateur = input(">>>>>  ")
            # On convertit cette valeur en int
            annee = int(entre_utilisateur)
            # Si la valeur respecte la condition (une valeur superieur strictement a 1970)
            if(annee > 1970):
                # On peut quitter la boucle
                valeur_correcte = 1
        # Si la valeur n'est pas convertissable en entier
        except ValueError:
            print("L'âge de la voiture doit etre superieur a 1970.\n")
    # Et on la renvoit
    return annee

def demande_de_donnees():
    # Fonction qui appel toutes les fonctions de demande et recupere leurs donnees
    clear_screen()
    # On demande la marque
    id_marque_voiture = demander_nom_marque()
    clear_screen()
    # On demande le modele, dependant de la marque evidement
    id_modele_voiture = demander_nom_modele(id_marque_voiture)
    clear_screen()
    # On demande la couleur de la voiture
    couleur_voiture = donner_couleur()
    clear_screen()
    # On demande son kilometrage
    kilometrage_voiture = donner_kilometrage()
    clear_screen()
    # On demande son prix
    prix_voiture = donner_prix()
    clear_screen()
    # On demande sa location
    ville = donner_lieu()
    clear_screen()
    # Et on demande son age
    annee_voiture = donner_annee()
    
    # On appelle la fonction insertion_de_donnees dans laquelle on passe en parametre toutes les valeurs recupere precedement
    insertion_de_donnees(id_modele_voiture, couleur_voiture, kilometrage_voiture, prix_voiture, ville, annee_voiture)

def insertion_de_donnees(id_modele, couleur, kilometrage, prix, ville, annee):
    # Prend en parametre l'id du modele de la voiture (un entier), sa couleur (un string), son kilometrage (un entier),
    # son prix (un reel positif, float), sa location (un string) et son annee (un entier)
    # et renvoit rien. Elle insert les variables prises en parametre dans une base de données
    
    #On formate l'annee de sorte qu'elle soit bien du type date pour notre BD
    annee = f"{annee}-01-01"
    try:
        # On se connecte à la base de donnéees
        conn = MC.connect(host = 'localhost', database = 'voiture_database', user = 'root', password = '')
        # On definit notre curseur
        cursor = conn.cursor()
        # On definit notre requete
        req = 'INSERT INTO offre_voiture (id_modele, couleur_voiture, lieu_voiture, kilometrage_voiture, prix_voiture, annee_voiture) VALUES(%s, %s, %s, %s, %s, %s)'
        # On y ajoute les parametres
        infos = (id_modele, couleur, ville, kilometrage, prix, annee)
        # On lance la requete
        cursor.execute(req, infos)
        # Et on commit la requete pour sauvegarder les modifications dans notre base de donnéees
        conn.commit()
        
        print("Donner ajouter à la base de donnée !")
        
    except MC.Error as err:
        # Si il y a une erreur dans notre bd on l'ecrit
        print(err)
    finally:
        # Sinon on referme la connection
        if(conn.is_connected()):
            cursor.close()
            conn.close()

# Code principale

try:
    demande_de_donnees()
except KeyboardInterrupt:
    # En cas de ctrl + c
    print("\nProgramme arrete.")