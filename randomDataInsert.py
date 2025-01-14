import os
import mysql.connector as MC
import random

def random_nom_modele():
    tab_modele = ["Arkana", "Austral", "Clio", "Citadine 108", "Berline 408", "Break 508 SW", "Ë-C4X", "C4X", "ë-Berlingo", "Ampera-e", "Astra", "Mokka", "Bigster", "Duster", "Logan", "Arteon", "Golf", "Polo", "A1", "A6 E-tron", "Rs6", "Ariya", "Juke", "Nt400 Cabstar"]
    indice = random.randrange(0, len(tab_modele))
    
    return indice

def get_indice_marque(i):
    return i / 3

def couleur_aleatoire():
    tab_couleur = ["Rouge", "Bleu", "Vert", "Orange", "Jaune", "Rose", "Violet", "Blanc", "Noir", "Gris"]
    indice = random.randrange(0, len(tab_couleur))
    
    return tab_couleur[indice]

def lieu_aleatoire():
    tab_ville = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille",
    "Rennes", "Reims", "Saint-Étienne", "Toulon", "Le Havre", "Grenoble", "Dijon", "Angers", "Nimes", "Clermont-Ferrand"]
    indice = random.randrange(0, len(tab_ville))
    
    return tab_ville[indice]

def kilometrage_aleatoire():
    return random.randrange(0, 350000)

def prix_aleatoire():
    return random.uniform(500, 150000)

def annee_aleatoire():
    return random.randrange(2010, 2025)

def insertion_de_donnees(id_modele, couleur, kilometrage, prix, ville, annee):
    annee = f"{annee}-01-01"
    try:
        conn = MC.connect(host = 'localhost', database = 'voiture_database', user = 'root', password = '')
        cursor = conn.cursor()
        
        req = 'INSERT INTO offre_voiture (id_modele, couleur_voiture, lieu_voiture, kilometrage_voiture, prix_voiture, annee_voiture) VALUES(%s, %s, %s, %s, %s, %s)'
        infos = (id_modele, couleur, ville, kilometrage, prix, annee)
        
        cursor.execute(req, infos)
        conn.commit()
        
        # print("Donner ajouter a la base de donnée !")
        
    except MC.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

try:
    for i in range(0, 70):
        insertion_de_donnees(get_indice_marque(random_nom_modele()), couleur_aleatoire(), kilometrage_aleatoire(), prix_aleatoire(), lieu_aleatoire(), annee_aleatoire())
    print("Les données ont ete ajouter !")
except KeyboardInterrupt:
    print("\nProgramme arrete.")