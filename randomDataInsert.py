#coding: utf8

import os
import mysql.connector as MC
import random

def random_nom_modele():
    # Ne prend rien en parametre et renvoit un indice du tableau aleatoire plus 1
    tab_modele = ["Arkana", "Austral", "Clio", "Citadine 108", "Berline 408", "Break 508 SW", "Ë-C4X", "C4X", "ë-Berlingo", "Ampera-e", "Astra", "Mokka", "Bigster", "Duster", "Logan", "Arteon", "Golf", "Polo", "A1", "A6 E-tron", "Rs6", "Ariya", "Juke", "Nt400 Cabstar"]
    indice = random.randrange(0, len(tab_modele))
    
    return indice + 1

def couleur_aleatoire():
    # Ne prend rien en parametre et renvoit une couleur aleatoire parmi la liste ci-dessous
    tab_couleur = ["Rouge", "Bleu", "Vert", "Orange", "Jaune", "Rose", "Violet", "Blanc", "Noir", "Gris"]
    indice = random.randrange(0, len(tab_couleur))
    
    return tab_couleur[indice]

def lieu_aleatoire():
    # Ne prend rien en parametre et renvoit une ville aleatoire parmi la liste ci-dessous
    tab_ville = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille",
    "Rennes", "Reims", "Saint-Étienne", "Toulon", "Le Havre", "Grenoble", "Dijon", "Angers", "Nimes", "Clermont-Ferrand", "Rouen"]
    indice = random.randrange(0, len(tab_ville))
    
    return tab_ville[indice]

def kilometrage_aleatoire():
    # Ne prend rien en parametre et renvoit un kilometrage aleatoire dans l'intervalle [0, 350000]
    return random.randrange(0, 350000)

def prix_aleatoire():
    # Ne prend rien en parametre et renvoit un prix aleatoire dans l'intervalle [500, 150000]
    return random.randrange(500, 150000)

def annee_aleatoire():
    # Ne prend rien en parametre et renvoit une annee aleatoire dans l'intervalle [2010, 2025]
    return random.randrange(2010, 2025)

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
    for i in range(0, 100):
        insertion_de_donnees(random_nom_modele(), couleur_aleatoire(), kilometrage_aleatoire(), prix_aleatoire(), lieu_aleatoire(), annee_aleatoire())
    print("Donner ajouter a la base de donnée !")
except KeyboardInterrupt:
    # En cas de ctrl + c
    print("\nProgramme arrete.")