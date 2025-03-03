#coding: utf8

import os
import mysql.connector as MC

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def connection_a_la_base_de_donnees():
    try:
        conn = MC.connect(host = 'localhost', database = 'voiture_database', user = 'root', password = '')
        if conn.is_connected():
            return conn
    except MC.Error as err:
        print(err)
        return None

def demander_prix_minimum():
    clear_screen()
    prix_min = float(input("Prix minimum : "))
    return prix_min

def demander_prix_maximum():
    clear_screen()
    prix_max = float(input("Prix maximum : "))
    return prix_max

def demander_prix():
    clear_screen()
    prix = float(input("Prix : "))
    return prix

def demander_annee_minimum():
    clear_screen()
    annee_min = input("Année minimum (AAAA-MM-JJ) : ")
    return annee_min
    
def demander_annee_maximum():
    clear_screen()
    annee_max = input("Année maximum (AAAA-MM-JJ) : ")
    return annee_max

def demander_annee():
    clear_screen()
    annee = input("Année (AAAA-MM-JJ) : ")
    return annee

def demander_kilometrage_minimum():
    clear_screen()
    kilometrage_min = int(input("Kilométrage minimum : "))
    return kilometrage_min

def demander_kilometrage_maximum():
    clear_screen()
    kilometrage_max = int(input("Kilométrage maximum : "))
    return kilometrage_max

def demander_kilometrage():
    clear_screen()
    kilometrage = int(input("Kilométrage : "))
    return kilometrage

def demander_marque():
    clear_screen()
    print("Choisissez parmi ces marques : \nRenault, Peugeot, Citroen, Opel, Dacia, Volkswagen, Audi, Nissan : ")
    tableau_marque = ["Renault", "Peugeot", "Citroen", "Opel", "Dacia", "Volkswagen", "Audi", "Nissan"]
    entre_correcte = 0
    while entre_correcte == 0:
        marque = input(">>>>>  ")
        for m in tableau_marque:
            if marque.lower() == m.lower():
                entre_correcte = 1
    return marque

def demander_modele():
    clear_screen()
    print("Choisissez parmi ces marques : \nArkana, Austral, Clio, Citadine 108, Berline 408, Break 508 SW, \nE-C4X, C4X, E-Berlingo, Ampera-e, Astra, Mokka, \nBigster, Duster, Logan, Arteon, Golf, Polo, \nA1, A6 E-tron, Rs6, Ariya, Juke, Nt400 Cabstar : ")
    tableau_modele = ["Arkana", "Austral", "Clio", "Citadine 108", "Berline 408", 
    "Break 508 SW", "Ë-C4X", "C4X", "ë-Berlingo", "Ampera-e", "Astra", "Mokka", "Bigster", 
    "Duster", "Logan", "Arteon", "Golf", "Polo", "A1", "A6 E-tron", "Rs6", "Ariya", "Juke", "Nt400 Cabstar"]
    entre_correcte = 0
    while entre_correcte == 0:
        modele = input(">>>>>  ")
        for m in tableau_modele:
            if modele.lower() == m.lower():
                entre_correcte = 1
    return modele

def demander_couleur():
    clear_screen()
    print("Choisissez parmi ces couleurs : \nRouge, Bleu, Vert, Orange, Jaune, Rose, Violet, Blanc, Noir, Gris")
    tableau_couleur = ["Rouge", "Bleu", "Vert", "Orange", "Jaune", "Rose", "Violet", "Blanc", "Noir", "Gris"]
    entre_correcte = 0
    while entre_correcte == 0:
        couleur = input(">>>>>  ")
        for c in tableau_couleur:
            if couleur.lower() == c.lower():
                entre_correcte = 1
    return couleur

def demander_lieu():
    clear_screen()
    print("Choisissez par ces lieu :\nParis, Marseille, Lyon, Toulouse, Nice, Nantes, Montpellier, Strasbourg, Bordeaux, Lille, Rennes, Reims, Saint-Étienne, Toulon, Le Havre, Grenoble, Dijon, Angers, Nimes, Clermont-Ferrand")
    tableau_lieu = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille",
    "Rennes", "Reims", "Saint-Étienne", "Toulon", "Le Havre", "Grenoble", "Dijon", "Angers", "Nimes", "Clermont-Ferrand"]
    entre_correcte = 0
    while entre_correcte == 0:
        lieu = input(">>>>>  ")
        for l in tableau_lieu:
            if lieu.lower() == l.lower():
                entre_correcte = 1
    return lieu

def demande_reponse():
    reponse_correct = 0
    while reponse_correct == 0:
        entre = input(" [Y] Oui  [N] Non  [E] Egal: ")
        if entre == "y" or entre == "Y" or entre == "o" or entre == "O":
            return 2
        elif entre == "n" or entre == "N":
            return 1
        elif entre == "e" or entre == "E":
            return 0

def demander_filtres():
    #Cree un dico qui va contenir les filtres
    filtres = {}
    
    filtre_prix = input("Filtrer par prix ?\n [Y] Oui  [N] Non  [E] Egal: ").lower()
    if(filtre_prix == "y"):
        filtres['prix_minimum'] = demander_prix_minimum()
        filtres['prix_maximum'] = demander_prix_maximum()
    elif(filtre_prix == "e"):
        filtres['prix'] = demander_prix()
    
    filtre_annee = input("Filtrer par annee ?\n [Y] Oui  [N] Non  [E] Egal: ").lower()
    if(filtre_annee == "y"):
        filtres['annee_minimum'] = demander_annee_minimum()
        filtres['annee_maximum'] = demander_annee_maximum()
    elif(filtre_annee == "e"):
        filtres['annee_maximum'] = demander_annee()
    
    filtre_kilometrage = input("Filtrer par kilometrage ?\n [Y] Oui  [N] Non  [E] Egal: ").lower()
    if(filtre_kilometrage == "y"):
        filtres['kilometrage_minimum'] = demander_kilometrage_minimum()
        filtres['kilometrage_maximum'] = demander_kilometrage_maximum()
    elif(filtre_kilometrage == "e"):
        filtres['kilometrage'] = demander_kilometrage()
    
    filtre_marque = input("Filtrer par marque ?\n [Y] Oui  [N] Non: ").lower()
    if(filtre_marque == "y"):
        filtres['marque'] = demander_marque()
        
    filtre_modele = input("Filtrer par modele ?\n [Y] Oui  [N] Non: ").lower()
    if(filtre_modele == "y"):
        filtres['modele'] = demander_modele()
    
    filtre_couleur = input("Filtrer par couleur ?\n [Y] Oui  [N] Non: ").lower()
    if(filtre_couleur == "y"):
        filtres['couleur'] = demander_couleur()
    
    filtre_lieu = input("Filtrer par lieu ?\n [Y] Oui  [N] Non: ").lower()
    if(filtre_lieu == "y"):
        filtres['lieu'] = demander_lieu()
    
    return filtres

def afficher_les_offres_filtres(filtres):
    co = connection_a_la_base_de_donnees()
    if co:
        try:
            cursor = co.cursor(dictionary=True)
            
            req = """
            SELECT mv.nom_marque, m.nom_modele, o.couleur_voiture, o.lieu_voiture, 
            o.kilometrage_voiture, o.prix_voiture, o.annee_voiture 
            FROM offre_voiture o
            JOIN modele_voiture m ON o.id_modele = m.id_modele
            JOIN marque_voiture mv ON m.id_marque = mv.id_marque
            WHERE 1=1
            """
            
            conditions = []
            valeurs = []
            
            if 'prix_minimum' in filtres:
                conditions.append("o.prix_voiture >= %s")
                valeurs.append(filtres['prix_minimum'])

            if 'prix_maximum' in filtres:
                conditions.append("o.prix_voiture <= %s")
                valeurs.append(filtres['prix_maximum'])
            
            if 'prix' in filtres:
                conditions.append("o.prix_voiture = %s")
                valeurs.append(filtres['prix'])

            if 'annee_minimum' in filtres:
                conditions.append("o.annee_voiture >= %s")
                valeurs.append(filtres['annee_minimum'])

            if 'annee_maximum' in filtres:
                conditions.append("o.annee_voiture <= %s")
                valeurs.append(filtres['annee_maximum'])
            
            if 'annee' in filtres:
                conditions.append("o.prix_voiture = %s")
                valeurs.append(filtres['annee'])

            if 'kilometrage_minimum' in filtres:
                conditions.append("o.kilometrage_voiture >= %s")
                valeurs.append(filtres['kilometrage_minimum'])

            if 'kilometrage_maximum' in filtres:
                conditions.append("o.kilometrage_voiture <= %s")
                valeurs.append(filtres['kilometrage_maximum'])
            
            if 'kilometrage' in filtres:
                conditions.append("o.prix_voiture = %s")
                valeurs.append(filtres['kilometrage'])

            if 'marque' in filtres:
                conditions.append("mv.nom_marque = %s")
                valeurs.append(filtres['marque'])

            if 'modele' in filtres:
                conditions.append("m.nom_modele = %s")
                valeurs.append(filtres['modele'])

            if 'lieu' in filtres:
                conditions.append("o.lieu_voiture = %s")
                valeurs.append(filtres['lieu'])

            if 'couleur' in filtres:
                conditions.append("o.couleur_voiture = %s")
                valeurs.append(filtres['couleur'])
            
            if conditions:
                req += " AND " + " AND ".join(conditions)

            cursor.execute(req, valeurs)
            offres = cursor.fetchall()
            compteur = 0
            if offres:
                for ligne in offres:
                    print("+--------------------------------------------------------------------------------------------------------------------+")
                    print(f"\n  {ligne['nom_modele']}\t({ligne['nom_marque']})                               \t{ligne['prix_voiture']} €, {ligne['annee_voiture']}\n\t\t\t\t\t\t\t\t\t\t\t\t\t\n  {ligne['couleur_voiture']}\t {ligne['kilometrage_voiture']} km\t\t\t À : {ligne['lieu_voiture']}\n")
                    compteur += 1
                print("+--------------------------------------------------------------------------------------------------------------------+\n")
            else:
                afficher_les_offres_sans_filtres()
            print(f"Resultat(s) : {compteur}")
        except MC.Error as err:
            print(f"{err}")
        finally:
            if co.is_connected():
                cursor.close()
                co.close()
    
def afficher_les_offres_sans_filtres():
    print("Voici la liste des offres :")
    co = connection_a_la_base_de_donnees()
    
    if co:
        try:
            cursor = co.cursor()
            
            req = """
            SELECT mv.nom_marque, m.nom_modele, o.couleur_voiture, o.lieu_voiture, 
            o.kilometrage_voiture, o.prix_voiture, o.annee_voiture 
            FROM offre_voiture o
            JOIN modele_voiture m ON o.id_modele = m.id_modele
            JOIN marque_voiture mv ON m.id_marque = mv.id_marque
            """
            cursor.execute(req)
            offres_non_filtres = cursor.fetchall()
            compteur = 0
            for offre in offres_non_filtres:
                print("+--------------------------------------------------------------------------------------------------------------------+")
                print(f"\n  {offre[1]}\t{offre[0]}                               \t{offre[5]} €, {offre[6]}\n\t\t\t\t\t\t\t\t\t\t\t\t\t\n  {offre[2]}  À : {offre[3]}  {offre[4]} km")
                compteur += 1        
        except MC.Error as err:
            print(f"{err}")
        finally:
            if co.is_connected():
                cursor.close()
                co.close()

# Code Principale

try:
    print("Filtrer les offres ?\n [Y] Oui  [N] Non: ")
    clear_screen()
    filtres = demander_filtres()
    if filtres:
        afficher_les_offres_filtres(filtres)
    else:
        print("Aucun filtre appliqué.")
        afficher_les_offres_sans_filtres()
except KeyboardInterrupt:
    print("\nProgramme arrêté.")