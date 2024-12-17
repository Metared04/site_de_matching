def demanderNomMarque():
    tabMarque = ["Renault", "Peugeot", "Citroën", "Opel", "Dacia", "Volkswagen", "Audi", "Nissan"]
    marqueCorrect = 0
    idMarque = -1
    
    while marqueCorrect == 0:
        entreUtilisateur = input('[ Renault, Peugeot, Citröen, Opel, Dacia, Volkswagen, Audi, Nissan ] \nChoisissez une marque : ')
        
        for i in range(0, len(tabMarque)):
            if entreUtilisateur.lower() == tabMarque[i].lower():
                marqueCorrect = 1
                idMarque = i+1
    
    return idMarque

def demanderNomModele(idMarque):
    modeleCorrect = 0
    idModele = idMarque
    tabModele = ["Arkana", "Austral", "Clio", "Citadine 108", "Berline 408", "Break 508 SW", "Ë-C4X", "C4X", "ë-Berlingo", "Ampera-e", "Astra", "Mokka", "Bigster", "Duster", "Logan", "Arteon", "Golf", "Polo", "A1", "A6 E-tron", "Rs6", "Ariya", "Juke", "Nt400 Cabstar"]
    tabChoix = []
    for i in range(0, 3):
        tabChoix.append(tabModele[idMarque * 3 - (3 - i)])
    
    print("[ ")
    for i in range(0,len(tabChoix)):
        print("{}, ".format(tabChoix[i]))
    print(" ]\n")

    while modeleCorrect == 0:
        
        entreUtilisateur = input("Entrez un modele : ")
        valeur = 0
        for i in range(0, len(tabChoix)):
            if entreUtilisateur.lower() == tabChoix[i].lower():
                valeur = i
                modeleCorrect = 1
    idModele = (idModele*3) - (3 - valeur) + 1

    return idModele

def donner_couleur():
    couleurCorrect = 0
    tabCouleur = ["Rouge", "Bleu", "Vert", "Orange", "Jaune", "Rose", "Violet", "Blanc", "Noir"]
    couleurChoisit = ""
    while couleurCorrect == 0:
        entreUtilisateur = input("Entrez une couleur : ")
        for c in tabCouleur:
            if entreUtilisateur.lower() == c.lower():
                couleurChoisit = c
                couleurCorrect = 1
    
    return couleurChoisit

def insertionDeDonnees():
    idMarqueVoiture = demanderNomMarque()
    idModeleVoiture = demanderNomModele(idMarqueVoiture)
    couleurVoiture = donner_couleur()