#coding: utf8

import os
import mysql.connector as MC
import random

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def demander_nom_marque():
    tab_marque = ["Renault", "Peugeot", "Citroen", "Opel", "Dacia", "Volkswagen", "Audi", "Nissan"]
    marque_correcte = 0
    id_marque = -1
    print("Choisissez une marque parmi la liste ci-dessous :\n\n  Renault  |  Peugeot  |  Citröen  |  Opel  |  Dacia  |  Volkswagen  |  Audi  |  Nissan  \n")
    while marque_correcte == 0:
        entre_utilisateur = input(">>>>>  ")
        
        for i in range(0, len(tab_marque)):
            if entre_utilisateur.lower() == tab_marque[i].lower():
                marque_correcte = 1
                id_marque = i+1
    
    return id_marque

def demander_nom_modele(id_marque):
    modele_correct = 0
    id_modele = id_marque
    tab_modele = ["Arkana", "Austral", "Clio", "Citadine 108", "Berline 408", "Break 508 SW", "Ë-C4X", "C4X", "ë-Berlingo", "Ampera-e", "Astra", "Mokka", "Bigster", "Duster", "Logan", "Arteon", "Golf", "Polo", "A1", "A6 E-tron", "Rs6", "Ariya", "Juke", "Nt400 Cabstar"]
    tab_choix = []
    for i in range(0, 3):
        tab_choix.append(tab_modele[id_marque * 3 - (3 - i)])
    
    print(f"Choisissez un modele parmi la liste ci-dessous :\n\n  {tab_choix[0]}  |  {tab_choix[1]}  |  {tab_choix[2]}\n")

    while modele_correct == 0:
        
        entre_utilisateur = input(">>>>>  ")
        valeur = 0
        for i in range(0, len(tab_choix)):
            if entre_utilisateur.lower() == tab_choix[i].lower():
                valeur = i
                modele_correct = 1
    id_modele = (id_modele*3) - (3 - valeur) + 1

    return id_modele

def donner_couleur():
    couleur_correcte = 0
    tab_couleur = ["Rouge", "Bleu", "Vert", "Orange", "Jaune", "Rose", "Violet", "Blanc", "Noir", "Gris"]
    couleur_choisit = ""
    print("Choisissez une couleur parmi la liste ci-dessous :\n\n  Rouge  |  Bleu  |  Vert  |  Orange  |  Jaune  |  Rose  |  Violet  |  Blanc  |  Noir  |  Gris  \n")
    while couleur_correcte == 0:
        entre_utilisateur = input(">>>>>  ")
        for c in tab_couleur:
            if entre_utilisateur.lower() == c.lower():
                couleur_choisit = c
                couleur_correcte = 1
    
    return couleur_choisit

def donner_lieu():
    ville_correcte = 0
    
    tab_ville = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille",
    "Rennes", "Reims", "Saint-Étienne", "Toulon", "Le Havre", "Grenoble", "Dijon", "Angers", "Nimes", "Clermont-Ferrand", "Rouen"]
    
    ville_choisit = ""
    print("Choisissez une ville parmi la liste ci-dessous :\n\n  Paris  |  Marseille  |  Lyon  |  Toulouse  |  Nice  |  Nantes  |  Montpellier  |  Strasbourg  |  Bordeaux  |  Lille  |  Rennes  |  Reims  |  Saint-Étienne  |  Toulon  |  Le Havre  |  Grenoble  |  Dijon  |  Angers  |  Nimes  |  Clermont-Ferrand  |  Rouen\n")
    while ville_correcte == 0:
        entre_utilisateur = input(">>>>>  ")
        for v in tab_ville:
            if entre_utilisateur.lower() == v.lower():
                ville_choisit = v
                ville_correcte = 1
    
    return ville_choisit

def donner_kilometrage():
    valeur_correcte = 0
    print("Entrez un kilometrage : \n")
    while valeur_correcte == 0:
        try:
            entre_utilisateur = input(">>>>>  ")
            kilometrage = int(entre_utilisateur)
            if(kilometrage >= 0):
                valeur_correcte = 1
        except ValueError:
            print("Vous devez entrer une valeur positive")
    
    return kilometrage

def donner_prix():
    valeur_correcte = 0
    print("Entrez un prix (tapez point '.' pour mettre une virgule) : \n")
    while valeur_correcte == 0:
        try:
            entre_utilisateur = input(">>>>>  ")
            prix = float(entre_utilisateur)
            if(prix > 0):
                valeur_correcte = 1
        except ValueError:
            print("Vous devez entrer une valeur positive")
    
    return prix

def donner_annee():
    valeur_correcte = 0
    print("Entrez l'annee de la voiture : \n")
    while valeur_correcte == 0:
        try:
            entre_utilisateur = input(">>>>>  ")
            annee = int(entre_utilisateur)
            if(annee > 1970):
                valeur_correcte = 1
        except ValueError:
            print("L'âge de la voiture doit etre superieur a 1970.\n")
    
    return annee

def demande_de_donnees():
    clear_screen()
    id_marque_voiture = demander_nom_marque()
    clear_screen()
    id_modele_voiture = demander_nom_modele(id_marque_voiture)
    clear_screen()
    couleur_voiture = donner_couleur()
    clear_screen()
    kilometrage_voiture = donner_kilometrage()
    clear_screen()
    prix_voiture = donner_prix()
    clear_screen()
    ville = donner_lieu()
    clear_screen()
    annee_voiture = donner_annee()

    insertion_de_donnees(id_modele_voiture, couleur_voiture, kilometrage_voiture, prix_voiture, ville, annee_voiture)

def insertion_de_donnees(id_modele, couleur, kilometrage, prix, ville, annee):
    annee = f"{annee}-01-01"
    try:
        conn = MC.connect(host = 'localhost', database = 'voiture_database', user = 'root', password = '')
        cursor = conn.cursor()
        
        req = 'INSERT INTO offre_voiture (id_modele, couleur_voiture, lieu_voiture, kilometrage_voiture, prix_voiture, annee_voiture) VALUES(%s, %s, %s, %s, %s, %s)'
        infos = (id_modele, couleur, ville, kilometrage, prix, annee)
        
        cursor.execute(req, infos)
        conn.commit()
        
        print("Donner ajouter à la base de donnée !")
        
    except MC.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

try:
    demande_de_donnees()
except KeyboardInterrupt:
    print("\nProgramme arrete.")