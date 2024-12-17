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
	`rayon_voiture` INT NOT NULL,
	`kilometrage_voiture` INT,
	
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

INSERT INTO offre_voiture (id_modele, couleur_voiture, rayon_voiture, kilometrage_voiture)
VALUES 
(13, 'Rouge', 133, 147344),
(0, 'Vert', 142, 17423),
(15, 'Bleu', 40, 97395),
(16, 'Rouge', 54, 271138),
(16, 'Orange', 150, 228213),
(21, 'Jaune', 57, 15458),
(18, 'Vert', 70, 226902),
(11, 'Bleu', 37, 30404),
(8, 'Jaune', 76, 36573),
(0, 'Orange', 72, 231111),
(5, 'Rouge', 125, 157014),
(20, 'Rouge', 128, 852),
(10, 'Rose', 44, 204604),
(21, 'Rouge', 146, 188516),
(2, 'Vert', 22, 153754),
(15, 'Vert', 110, 173063),
(10, 'Orange', 17, 249),
(0, 'Vert', 149, 143014),
(6, 'Rose', 44, 173253),
(21, 'Bleu', 22, 171869),
(16, 'Rouge', 51, 291237),
(12, 'Rouge', 7, 293474),
(1, 'Rose', 74, 32206),
(9, 'Vert', 7, 90465),
(3, 'Rose', 64, 150287),
(19, 'Jaune', 9, 182233),
(5, 'Rouge', 95, 31083),
(1, 'Bleu', 9, 193892),
(19, 'Rouge', 4, 297790),
(23, 'Orange', 103, 59129),
(16, 'Vert', 29, 213724),
(19, 'Rose', 68, 253035),
(6, 'Orange', 16, 56879),
(5, 'Rouge', 28, 264520),
(18, 'Rose', 130, 292906),
(20, 'Bleu', 96, 108893),
(21, 'Rouge', 80, 226330),
(8, 'Vert', 15, 10566),
(6, 'Bleu', 64, 32357),
(16, 'Orange', 57, 242312),
(19, 'Orange', 58, 263758),
(7, 'Vert', 95, 132889),
(12, 'Rose', 31, 281443),
(11, 'Bleu', 105, 256841),
(13, 'Jaune', 46, 24394),
(5, 'Orange', 120, 289792),
(6, 'Bleu', 3, 106004),
(20, 'Rose', 21, 248727),
(12, 'Jaune', 148, 15821),
(17, 'Vert', 105, 176904),
(3, 'Rouge', 54, 84315),
(5, 'Orange', 21, 293896),
(5, 'Vert', 113, 213164),
(2, 'Jaune', 72, 17356),
(5, 'Bleu', 88, 225018),
(1, 'Vert', 24, 294608),
(23, 'Vert', 20, 160397),
(5, 'Rouge', 48, 37794),
(3, 'Orange', 17, 85880),
(14, 'Bleu', 12, 78352),
(4, 'Orange', 40, 281073),
(4, 'Orange', 93, 61454),
(10, 'Rouge', 12, 52782),
(7, 'Orange', 129, 67805),
(4, 'Rouge', 1, 178413),
(18, 'Jaune', 115, 144565),
(7, 'Jaune', 27, 173684),
(13, 'Rose', 22, 205296),
(23, 'Rouge', 140, 85839),
(15, 'Bleu', 83, 106198),
(18, 'Rose', 45, 257456),
(6, 'Orange', 50, 265944),
(13, 'Bleu', 121, 268635),
(19, 'Orange', 105, 132620),
(20, 'Jaune', 50, 13437),
(12, 'Bleu', 87, 80223),
(18, 'Rose', 38, 261361),
(2, 'Vert', 93, 112301),
(3, 'Jaune', 66, 183901),
(19, 'Orange', 46, 227849),
(9, 'Jaune', 62, 251557),
(10, 'Vert', 124, 146181),
(6, 'Jaune', 10, 48549),
(22, 'Bleu', 26, 198214),
(15, 'Rose', 95, 207415),
(11, 'Jaune', 111, 239),
(1, 'Jaune', 4, 98159),
(7, 'Bleu', 68, 55205),
(12, 'Bleu', 136, 287798),
(7, 'Rose', 73, 128384),
(16, 'Jaune', 93, 108995),
(22, 'Rose', 78, 295744),
(8, 'Jaune', 66, 224131),
(18, 'Bleu', 21, 46523),
(2, 'Rose', 104, 259983),
(16, 'Orange', 30, 285501),
(19, 'Orange', 24, 132906),
(23, 'Vert', 100, 268006),
(21, 'Orange', 3, 25173),
(8, 'Rouge', 44, 126707);

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