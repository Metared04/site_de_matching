/*
----------------------------------------------------------------------------------------------------------------
-- On recrée la base de données --------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
*/

DROP DATABASE IF EXISTS `voiture_database`;
CREATE DATABASE IF NOT EXISTS `voiture_database`;
USE `voiture_database`;

/*
----------------------------------------------------------------------------------------------------------------
-- On crée des tables -----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
*/

CREATE TABLE IF NOT EXISTS `marque_voiture`(
	`id_marque` INT NOT NULL,
	`nom_marque` VARCHAR(65) NOT NULL,
	
	CONSTRAINT `pk_id_marque` PRIMARY KEY (`id_marque`)
);

CREATE TABLE IF NOT EXISTS `modele_voiture`(
	`id_modele` INT NOT NULL AUTO_INCREMENT,
	`nom_modele` VARCHAR(65) NOT NULL,
	`id_marque` INT NOT NULL,
	
	CONSTRAINT `pk_id_modele` PRIMARY KEY(`id_modele`),
	CONSTRAINT `fk_nom_marque` FOREIGN KEY(`id_marque`) REFERENCES marque_voiture(`id_marque`)
);

CREATE TABLE IF NOT EXISTS `offre_voiture`
(
	`id_offre` INT NOT NULL AUTO_INCREMENT, 
	`id_modele` INT NOT NULL,
	`couleur_voiture` VARCHAR(65) NOT NULL, 
	`lieu_voiture` varchar(50) NOT NULL,
	`kilometrage_voiture` INT,
	`prix_voiture` DECIMAL(6,2) NOT NULL,
	`annee_voiture` DATE NOT NULL,
	
	CONSTRAINT `pk_id_offre` PRIMARY KEY(`id_offre`),	
	CONSTRAINT `fk_nom_modele` FOREIGN KEY(`id_modele`) REFERENCES modele_voiture(`id_modele`)
);

/*
----------------------------------------------------------------------------------------------------------------
-- On y ajoute des données -------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
*/

INSERT INTO marque_voiture (id_marque, nom_marque)
VALUES
(1, 'Renault'),
(2, 'Peugeot'),
(3, 'Citroën'),
(4, 'Opel'),
(5, 'Dacia'),
(6, 'Volkswagen'),
(7, 'Audi'),
(8, 'Nissan');

INSERT INTO modele_voiture (nom_modele, id_marque)
VALUES
('Arkana', 1),
('Austral', 1),
('Clio', 1),
('Citadine 108', 2),
('Berline 408', 2),
('Break 508 SW', 2),
('Ë-C4X', 3),
('C4X', 3),
('ë-Berlingo', 3),
('Ampera-e', 4),
('Astra', 4),
('Mokka', 4),
('Bigster', 5),
('Duster', 5),
('Logan', 5),
('Arteon', 6),
('Golf', 6),
('Polo', 6),
('A1', 7),
('A6 E-tron', 7),
('Rs6', 7),
('Ariya', 8),
('Juke', 8),
('Nt400 Cabstar', 8);

INSERT INTO offre_voiture (id_modele, couleur_voiture, lieu_voiture, kilometrage_voiture, prix_voiture, annee_voiture)
VALUES 


/*
----------------------------------------------------------------------------------------------------------------
-- Test de requêtes : ------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
*/

SELECT nom_marque
FROM marque_voiture
INNER JOIN modele_voiture ON marque_voiture.id_marque = modele_voiture.id_marque;

SELECT 
    (SELECT nom_marque FROM marque_voiture WHERE id_marque = o.id_marque) AS marque,
    (SELECT nom_modele FROM modele_voiture WHERE id_modele = o.id_modele) AS modele,
    o.couleur_voiture AS couleur
FROM 
    offre_voiture o;

SELECT mv.nom_marque AS marque, mo.nom_modele AS modele, o.couleur_voiture AS couleur
FROM offre_voiture o
INNER JOIN modele_voiture mo ON o.id_modele = mo.id_modele
INNER JOIN marque_voiture mv ON mo.id_marque = mv.id_marque;

SELECT mv.nom_marque AS marque, mo.nom_modele AS modele, o.couleur_voiture AS couleur
FROM offre_voiture o
INNER JOIN modele_voiture mo ON o.id_modele = mo.id_modele
INNER JOIN marque_voiture mv ON mo.id_marque = mv.id_marque
WHERE rayon_voiture <= 50;