-- Active: 1718932996174@@127.0.0.1@5432@PerfprofESGAE



CREATE TABLE Enseignants (
    ID_enseignant INT PRIMARY KEY,
    Nom VARCHAR(255),
    Prénom VARCHAR(255),
    Classe VARCHAR(255),
    Date_embauche DATE
);
SELECT * FROM Administrateurs;
SELECT * FROM Enseignants;
SELECT * FROM Classes;
SELECT * FROM Moyennes_Générales;
SELECT * FROM Taux;
SELECT * FROM semestre;
SELECT * FROM Enseigne;
--
-- Dumping data for table `Enseignants`
--

INSERT INTO Enseignants (ID_enseignant, Nom, Prénom, Classe, Date_embauche)
VALUES
	(1, 'Makosso', 'Luc', 'Gestion d''entreprise', '2010-09-14'),
	(2, 'Mabiala', 'Honorine', 'Gestion d''entreprise', '2012-04-22'),
	(3, 'Bemba', 'Firmin', 'Gestion d''entreprise', '2013-11-11'),
	(4, 'Ngoma', 'Élise', 'Gestion d''entreprise', '2015-06-05'),
	(5, 'Bakala', 'Clarisse', 'Gestion d''entreprise', '2017-02-18'),
	(6, 'Moungali', 'Pascal', 'Gestion d''entreprise', '2018-10-01'),
	(7, 'Kibouedi', 'Véronique', 'Gestion d''entreprise', '2020-07-15'),
	(8, 'Tchicaya', 'Gaston', 'Gestion d''entreprise', '2021-12-03'),
	(9, 'Loutombo', 'Danielle', 'Gestion d''entreprise', '2014-08-29'),
	(10, 'Makaya', 'Yannick', 'Gestion d''entreprise', '2016-01-14'),
	(11, 'Matondo', 'Patrice', 'Informatique', '2011-10-19'),
	(12, 'Loundou', 'Léa', 'Informatique', '2013-05-27'),
	(13, 'Makosso', 'Thierry', 'Informatique', '2014-12-15'),
	(14, 'Mabiala', 'Marie', 'Informatique', '2016-07-09'),
	(15, 'Bemba', 'Christian', 'Informatique', '2018-03-25'),
	(16, 'Ngoma', 'Christelle', 'Informatique', '2019-11-10'),
	(17, 'Bakala', 'Pierre', 'Informatique', '2021-08-04'),
	(18, 'Moungali', 'Sophie', 'Informatique', '2023-02-19'),
	(19, 'Kibouedi', 'Jules', 'Informatique', '2015-09-13'),
	(20, 'Tchicaya', 'Lisette', 'Informatique', '2017-04-28'),
    (21, 'Moukala', 'Léon', 'Gestion d''entreprise', '2019-09-14'),
    (22, 'Makouala', 'Béatrice', 'Gestion d''entreprise', '2021-06-22'),
    (23, 'Bassoumba', 'Hugues', 'Gestion d''entreprise', '2023-01-11'),
    (24, 'Mbemba', 'Christiane', 'Gestion d''entreprise', '2016-08-05'),
    (25, 'Boukadia', 'Dieudonné', 'Gestion d''entreprise', '2018-03-18'),
    (26, 'Mouanda', 'Flore', 'Gestion d''entreprise', '2020-11-01'),
    (27, 'Makoussa', 'Serge', 'Gestion d''entreprise', '2022-07-15'),
    (28, 'Ngokana', 'Elodie', 'Gestion d''entreprise', '2014-04-03'),
    (29, 'Banzouzi', 'Franck', 'Gestion d''entreprise', '2015-09-29'),
    (30, 'Mampouya', 'Céline', 'Gestion d''entreprise', '2017-02-14'),
    (31, 'Moutsinga', 'Arnaud', 'Informatique', '2020-11-19'),
    (32, 'Moukoko', 'Sylvie', 'Informatique', '2022-06-27'),
    (33, 'Bikoula', 'David', 'Informatique', '2014-01-15'),
    (34, 'Moussoki', 'Lydie', 'Informatique', '2016-06-09'),
    (35, 'Makoundi', 'Michel', 'Informatique', '2018-01-25'),
    (36, 'Mbemba', 'Rosalie', 'Informatique', '2019-09-10'),
    (37, 'Boukou', 'Serge', 'Informatique', '2021-04-04'),
    (38, 'Moutouari', 'Nathalie', 'Informatique', '2013-11-20'),
    (39, 'Mbanzoulou', 'Robert', 'Informatique', '2015-04-15'),
    (40, 'Makanda', 'Claire', 'Informatique', '2017-09-30'),
    (41, 'Moutima', 'Gérard', 'Gestion d''entreprise', '2012-07-12'),
    (42, 'Moukouéké', 'Suzanne', 'Gestion d''entreprise', '2014-02-18'),
    (43, 'Bikiéla', 'Patrick', 'Gestion d''entreprise', '2015-09-17'),
    (44, 'Mouanda', 'Marcelle', 'Gestion d''entreprise', '2017-04-05'),
    (45, 'Mboungou', 'Brigitte', 'Gestion d''entreprise', '2019-01-19'),
    (46, 'Boudzoumou', 'Guy', 'Gestion d''entreprise', '2020-08-03'),
    (47, 'Makani', 'Chantal', 'Gestion d''entreprise', '2022-03-18'),
    (48, 'Moukoumbi', 'Paul', 'Gestion d''entreprise', '2013-12-04'),
    (49, 'Bouka', 'Juliette', 'Gestion d''entreprise', '2015-05-30'),
    (50, 'Moutou', 'Sosthène', 'Gestion d''entreprise', '2016-10-14'),
    (51, 'Mabika', 'Aline', 'Informatique', '2011-07-19'),
    (52, 'Mouendzi', 'Charles', 'Informatique', '2013-02-27'),
    (53, 'Bimou', 'Stéphanie', 'Informatique', '2014-09-15'),
    (54, 'Mouanga', 'Jean', 'Informatique', '2016-04-09'),
    (55, 'Makouala', 'Sylvie', 'Informatique', '2018-11-25'),
    (56, 'Bakouala', 'Roger', 'Informatique', '2020-06-10'),
    (57, 'Mbanzouzi', 'Emilienne', 'Informatique', '2022-01-04'),
    (58, 'Mamona', 'Serge', 'Informatique', '2013-08-20'),
    (59, 'Moutoussamy', 'Cécile', 'Informatique', '2015-03-15'),
    (60, 'Moukanda', 'Patrick', 'Informatique', '2017-08-30'),
    (61, 'Makaya', 'Suzanne', 'Gestion d''entreprise', '2010-05-14'),
    (62, 'Mabiala', 'Joséphine', 'Gestion d''entreprise', '2012-12-22'),
    (63, 'Bemba', 'Clément', 'Gestion d''entreprise', '2014-07-11'),
    (64, 'Ngoma', 'Sylvie', 'Gestion d''entreprise', '2016-02-05'),
    (65, 'Bakala', 'Patrick', 'Gestion d''entreprise', '2018-09-18'),
    (66, 'Moungali', 'Marie', 'Gestion d''entreprise', '2020-04-01'),
    (67, 'Kibouedi', 'Gérard', 'Gestion d''entreprise', '2021-11-15'),
    (68, 'Tchicaya', 'Brigitte', 'Gestion d''entreprise', '2013-06-03'),
    (69, 'Loutombo', 'Jean', 'Gestion d''entreprise', '2015-01-29'),
    (70, 'Makaya', 'Isabelle', 'Gestion d''entreprise', '2017-07-14'),
    (71, 'Matondo', 'Michel', 'Informatique', '2020-06-19'),
    (72, 'Loundou', 'Alice', 'Informatique', '2022-01-27'),
    (73, 'Makosso', 'François', 'Informatique', '2013-08-15'),
    (74, 'Mabiala', 'Élodie', 'Informatique', '2015-03-09'),
    (75, 'Bemba', 'Pascal', 'Informatique', '2017-09-24'),
    (76, 'Ngoma', 'Sophie', 'Informatique', '2019-04-10'),
    (77, 'Bakala', 'Gaston', 'Informatique', '2021-11-04'),
    (78, 'Moungali', 'Carine', 'Informatique', '2012-12-20'),
    (79, 'Kibouedi', 'Robert', 'Informatique', '2014-07-15'),
    (80, 'Tchicaya', 'Suzanne', 'Informatique', '2016-02-29');


