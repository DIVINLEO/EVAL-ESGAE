-- Database: PerfprofESGAE

-- DROP DATABASE IF EXISTS "PerfprofESGAE";

CREATE DATABASE "PerfprofESGAE"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
	-- Table Utilisateurs
CREATE TABLE utilisateurs (
    id_utilisateur SERIAL PRIMARY KEY,
    nom_complet VARCHAR(255) NOT NULL,
    adresse_mail VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(256) NOT NULL,
    telephone VARCHAR(9) NOT NULL
);

-- Table Classes
CREATE TABLE classes (
    id_classe SERIAL PRIMARY KEY,
    nom_classe VARCHAR(255) NOT NULL,
    année_scolaire VARCHAR(10) NOT NULL
);

-- Table Matière
CREATE TABLE matière (
    id_matière SERIAL PRIMARY KEY,
    nom_matière VARCHAR(50) NOT NULL
);

-- Table Enseignants
CREATE TABLE enseignants (
    id_enseignant SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prénom VARCHAR(255) NOT NULL,
    date_naissance DATE NOT NULL,
    genre CHAR(1) NOT NULL CHECK (genre IN ('H', 'F')),
    telephone VARCHAR(9),
    département VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    date_embauche DATE NOT NULL
);


-- Table Étudiants
CREATE TABLE étudiants (
    id_étudiant SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prénom VARCHAR(50) NOT NULL,
    date_naissance DATE NOT NULL,
    genre CHAR(1) NOT NULL CHECK (genre IN ('H', 'F')),
    id_classe INT NOT NULL,
    FOREIGN KEY (id_classe) REFERENCES classes(id_classe)
);




-- Table Semestre
CREATE TABLE semestre (
    id_semestre SERIAL PRIMARY KEY,
    id_classe INT NOT NULL,
    id_enseignant INT NOT NULL,
	id_matière INT NOT NULL,
    semestre INT NOT NULL CHECK (semestre IN (1, 2)),
    nom_semestre VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_classe) REFERENCES classes(id_classe),
	FOREIGN KEY (id_matière) REFERENCES matière(id_matière),
    FOREIGN KEY (id_enseignant) REFERENCES enseignants(id_enseignant)
);





-- Table Programme
CREATE TABLE programme (
    id_classe INT NOT NULL,
    id_matière INT NOT NULL,
    PRIMARY KEY (id_classe, id_matière),
    FOREIGN KEY (id_classe) REFERENCES classes(id_classe),
    FOREIGN KEY (id_matière) REFERENCES matière(id_matière)
);


-- Table Inscription
CREATE TABLE inscription (
    id_étudiant INT NOT NULL,
    id_classe INT NOT NULL,
    PRIMARY KEY (id_étudiant, id_classe),
    FOREIGN KEY (id_étudiant) REFERENCES étudiants(id_étudiant),
    FOREIGN KEY (id_classe) REFERENCES classes(id_classe)
);


-- Table Note
CREATE TABLE note (
    id_note SERIAL PRIMARY KEY,
    id_étudiant INT NOT NULL,
    id_enseignant INT NOT NULL,
    id_matière INT NOT NULL,
    note DECIMAL(5, 2) NOT NULL,
    commentaire TEXT,
    date_évaluation DATE NOT NULL,
    FOREIGN KEY (id_étudiant) REFERENCES étudiants(id_étudiant),
    FOREIGN KEY (id_enseignant) REFERENCES enseignants(id_enseignant),
    FOREIGN KEY (id_matière) REFERENCES matière(id_matière)
);


-- Table Enseigne
CREATE TABLE enseigne (
    id_enseignant INT NOT NULL,
    id_matière INT NOT NULL,
    id_classe INT NOT NULL,
    PRIMARY KEY (id_enseignant, id_matière, id_classe),
    FOREIGN KEY (id_enseignant) REFERENCES enseignants(id_enseignant),
    FOREIGN KEY (id_matière) REFERENCES matière(id_matière),
    FOREIGN KEY (id_classe) REFERENCES classes(id_classe)
);

SELECT * FROM utilisateurs;
SELECT * FROM classes;
SELECT * FROM matière;
SELECT * FROM enseignants;
SELECT * FROM étudiants;
SELECT * FROM semestre;
SELECT * FROM programme;
SELECT * FROM inscription;
SELECT * FROM note;
SELECT * FROM enseigne;

ALTER SEQUENCE utilisateurs_id_utilisateur_seq RESTART WITH 3;
select*from utilisateurs
DELETE FROM utilisateurs 
Where id_utilisateur=3;

INSERT INTO utilisateurs (nom_complet, adresse_mail, mot_de_passe, telephone)
VALUES ('Grace Zola', 'gracezola3@gmail.com', '2024', '065644334'),
('OUAZOLO Marie-Pierre', 'ouazolok@gmail.com', 'secret789', '069939531');


INSERT INTO classes (nom_classe, année_scolaire) VALUES
('TC1', '2023-2024'),
('TC2', '2023-2024'),
('TC3', '2023-2024'),
('TC4', '2023-2024'),
('TC5', '2023-2024'),
('TC6', '2023-2024'),
('TC7', '2023-2024'),
('TC8', '2023-2024'),
('TC9', '2023-2024'),
('TC10', '2023-2024'),
('TC11', '2023-2024'),
('TC12', '2023-2024'),
('TC13', '2023-2024'),
('TC14', '2023-2024'),
('TC15', '2023-2024'),
('TC16', '2023-2024'),
('TC17', '2023-2024'),
('TC18', '2023-2024'),
('TC19', '2023-2024'),
('TC20', '2023-2024'),
('TC21', '2023-2024'),
('TC22', '2023-2024'),
('PROGRAMMATION', '2023-2024'),
('ANAPRO', '2023-2024'),
('LPGL', '2023-2024'),
('LPABD', '2023-2024'),
('LPASR', '2023-2024'),
('CESAE1', '2023-2024'),
('CESAE2', '2023-2024');


INSERT INTO matière (nom_matière) VALUES
('SQL Server'),
('Django'),
('Linux'),
('MongoDB'),
('Oracle'),
('MySQL'),
('PostgreSQL'),
('Network Security'),
('Web Development'),
('Data Structures and Algorithms'),
('Cloud Computing'),
('Big Data'),
('Machine Learning'),
('Computer Networks'),
('Operating Systems'),
('Software Engineering'),
('Database Design'),
('Information Security'),
('Java'),
('Python'),
('Marketing'),
('Comptabilité'),
('Anglais'),
('Français'),
('Microsoft Excel'),
('Microsoft Word'),
('Microsoft Access'),
('Prospection'),
('Business plan'),
('Entrepreunariat');
 
 
 INSERT INTO enseignants (nom, prénom, date_naissance, genre, telephone, département, email, date_embauche) VALUES
('Ngoma', 'Jean', '1980-01-15', 'H', '060123456', 'Gestion d’Entreprise', 'ngoma.jean@uge.com', '2005-08-15'),
('Nkouka', 'Marie', '1985-03-22', 'F', '061234567', 'Marketing', 'nkouka.marie@uge.com', '2010-09-12'),
('Mbemba', 'Patrick', '1975-07-10', 'H', '050987654', 'Comptabilité', 'mbemba.patrick@uge.com', '2000-07-01'),
('Makaya', 'Sophia', '1990-12-05', 'F', '051234987', 'Finance', 'makaya.sophia@uge.com', '2015-01-10'),
('Mabiala', 'Alain', '1978-11-23', 'H', '040987321', 'Gestion de Projet', 'mabiala.alain@uge.com', '2003-04-20'),
('Sassou', 'Félicité', '1983-04-16', 'F', '061111111', 'Ressources Humaines', 'sassou.felicite@uge.com', '2008-05-15'),
('Mavoungou', 'Bruno', '1987-08-30', 'H', '060999999', 'Informatique', 'mavoungou.bruno@uge.com', '2012-11-25'),
('Nzobo', 'Claudine', '1972-05-14', 'F', '050888888', 'Droit', 'nzobo.claudine@uge.com', '1998-03-10'),
('Bokoko', 'Alphonse', '1981-09-18', 'H', '041234567', 'Économie', 'bokoko.alphonse@uge.com', '2007-09-01'),
('Kodia', 'Isabelle', '1979-06-12', 'F', '050123456', 'Gestion', 'kodia.isabelle@uge.com', '2002-02-20'),
('Bakala', 'Bernard', '1982-07-26', 'H', '066162626', 'Analyse Financière', 'bernard.bakala@example.com', '2009-11-15'),
('Bakou', 'Sophie', '1982-03-25', 'F', '061011121', 'Ressources Humaines', 'sophie.bakou@example.com', '2021-01-10'),
('Bouya', 'Eric', '1980-11-17', 'H', '064344454', 'Entrepreneuriat', 'eric.bouya@example.com', '2012-04-03'),
('Kounga', 'Pierre', '1976-12-03', 'H', '061920212', 'Informatique', 'pierre.kounga@example.com', '2016-08-12'),
('Koubemba', 'Thierry', '1987-04-19', 'H', '065556565', 'Innovation Technologique', 'thierry.koubemba@example.com', '2010-07-28'),
('Lemba', 'Jean-Pierre', '1983-03-11', 'H', '064950505', 'Logistique et Supply Chain', 'jeanpierre.lemba@example.com', '2011-01-07'),
('Loundou', 'Isabelle', '1986-05-09', 'F', '064041424', 'Management de Projet', 'isabelle.loundou@example.com', '2026-08-14'),
('Mabiala', 'Marie', '1985-08-22', 'F', '060405060', 'Finance', 'marie.mabiala@example.com', '2019-07-15'),
('Mabounda', 'Gérard', '1977-10-05', 'H', '063738393', 'Marketing Digital', 'gerard.mabounda@example.com', '2013-06-25'),
('Makanda', 'Jean', '1978-05-15', 'H', '060102030', 'Marketing', 'jean.makanda@example.com', '2020-09-01'),
('Mambou', 'Chantal', '1983-04-30', 'F', '062223242', 'Stratégie', 'chantal.mambou@example.com', '2023-04-01'),
('Mfoutou', 'Jacques', '1975-08-28', 'H', '063132333', 'Audit', 'jacques.mfoutou@example.com', '2014-10-18'),
('Mfoula', 'Florence', '1979-12-08', 'F', '065859596', 'Stratégie d''Entreprise', 'florence.mfoula@example.com', '2029-02-17'),
('Mouanga', 'Aline', '1974-09-02', 'F', '065253535', 'Systèmes d''Information', 'aline.mouanga@example.com', '2028-12-05'),
('Moussoki', 'Sylvie', '1980-06-08', 'F', '061617181', 'Logistique', 'sylvie.moussoki@example.com', '2022-02-15'),
('Moumba', 'François', '1984-08-14', 'H', '066768686', 'Marketing Stratégique', 'francois.moumba@example.com', '2008-03-30'),
('Nkodia', 'Christelle', '1984-01-20', 'F', '062829303', 'Communication', 'christelle.nkodia@example.com', '2024-03-10'),
('Nkounkou', 'Paul', '1974-11-10', 'H', '060708090', 'Comptabilité', 'paul.nkounkou@example.com', '2018-03-20'),
('Ngouabi', 'Suzanne', '1976-04-27', 'F', '067071717', 'Business Intelligence', 'suzanne.ngouabi@example.com', '2031-06-08'),
('Nsoni', 'Catherine', '1978-06-23', 'F', '064647484', 'Ressources Humaines', 'catherine.nsoni@example.com', '2027-09-19'),
('Ongali', 'Luc', '1987-09-18', 'H', '061314151', 'Management', 'luc.ongali@example.com', '2017-11-05'),
('Ossali', 'Marina', '1981-02-14', 'F', '063435363', 'Finance Internationale', 'marina.ossali@example.com', '2025-05-22'),
('Ouangolo', 'Estelle', '1985-02-03', 'F', '066465656', 'Gestion des Risques', 'estelle.ouangolo@example.com', '2030-04-22'),
('Ouabari', 'Robert', '1981-01-15', 'H', '067374747', 'Relations Internationales', 'robert.ouabari@example.com', '2007-09-10');

 
 INSERT INTO étudiants (nom, prénom, date_naissance, genre, id_classe) VALUES
('Koumba', 'Michel', '2000-02-20', 'H', 1),
('Loumou', 'Alice', '1999-03-15', 'F', 2),
('Nganga', 'Fabrice', '2001-04-10', 'H', 3),
('Tchicaya', 'Josiane', '2002-05-05', 'F', 4),
('Bakoua', 'Samuel', '1998-06-25', 'H', 5),
('Kivouvou', 'Antoinette', '1997-07-30', 'F', 6),
('Ondongo', 'Serge', '2000-08-10', 'H', 7),
('Mankessi', 'Laurence', '2001-09-12', 'F', 8),
('Ngolo', 'François', '1999-10-15', 'H', 9),
('Bissila', 'Juliette', '2002-11-20', 'F', 10),
('Kibangou', 'Daniel', '1998-12-05', 'H', 11),
('Mbou', 'Monique', '1997-01-25', 'F', 12),
('Sounga', 'Gilbert', '2000-02-17', 'H', 13),
('Moudoudou', 'Patricia', '2001-03-28', 'F', 14),
('Dibongi', 'Maxime', '1999-04-19', 'H', 15),
('Bikoka', 'Suzanne', '2002-05-23', 'F', 16),
('Tati', 'Alphonse', '2000-06-14', 'H', 17),
('Kouya', 'Catherine', '2001-07-07', 'F', 18),
('Matsima', 'René', '1998-08-01', 'H', 19),
('Kodia', 'Sylvie', '1997-09-16', 'F', 20),
('Massamba', 'Georges', '2000-10-10', 'H', 21),
('Nkossa', 'Martine', '2001-11-09', 'F', 22),
('Moukila', 'Alexandre', '1999-12-12', 'H', 23),
('Samba', 'Jacqueline', '2000-01-15', 'F', 24),
('Mbemba', 'Pierre', '1998-02-19', 'H', 25),
('Moukoko', 'Christelle', '2001-03-21', 'F', 26),
('Boukadia', 'Emmanuel', '1999-04-24', 'H', 27),
('Makita', 'Delphine', '2000-05-27', 'F', 28),
('Moungou', 'Roger', '1998-06-30', 'H', 29),
('Kanza', 'Jeanne', '2001-07-03', 'F', 1),
('Okemba', 'Michel', '1999-08-06', 'H', 2),
('Tchikaya', 'Marceline', '2000-09-09', 'F', 3),
('Boungou', 'David', '2001-10-13', 'H', 4),
('Menga', 'Suzanne', '1998-11-15', 'F', 5),
('Mayala', 'Laurent', '1997-12-18', 'H', 6),
('Ntsika', 'Pauline', '2000-01-21', 'F', 7),
('Dongo', 'Éric', '1999-02-23', 'H', 8),
('Louamba', 'Justine', '2001-03-26', 'F', 9),
('Nzengui', 'Patrick', '1999-04-28', 'H', 10),
('Nsona', 'Mireille', '2000-05-30', 'F', 11),
('Kimpolo', 'Alain', '1998-06-21', 'H', 12),
('Loufoua', 'Evelyne', '2001-07-15', 'F', 13),
('Mbongo', 'Jean-Pierre', '1999-08-17', 'H', 14),
('Moukala', 'Thérèse', '2000-09-19', 'F', 15),
('Pambou', 'Gilbert', '1998-10-21', 'H', 17),
('Loudi', 'Esther', '2001-11-23', 'F', 18),
('Kama', 'Vincent', '1999-12-25', 'H', 19),
('Yila', 'Françoise', '2000-01-27', 'F', 20),
('Bongo', 'Raymond', '1998-02-28', 'H', 21),
('Nzonzi', 'Patricia', '2001-03-31', 'F', 22),
('Koundou', 'Benoît', '1999-04-02', 'H',23),
('Mankou', 'Pauline', '2000-05-04', 'F', 24),
('Nkama', 'Alexis', '1998-06-06', 'H', 25),
('Nkouka', 'Séverine', '2001-07-08', 'F', 26),
('Ndinga', 'Félix', '1999-08-10', 'H', 27),
('Bouity', 'Joséphine', '2000-09-12', 'F', 28),
('Makosso', 'Pierre', '1998-10-14', 'H', 29),
('Nkoukou', 'Geneviève', '2001-11-16', 'F', 2),
('Kibamba', 'Thomas', '1999-12-18', 'H', 5),
('Mankayi', 'Blandine', '2000-01-20', 'F', 6),
('Koumba', 'Michel', '2000-02-20', 'H', 1),
('Loumou', 'Alice', '1999-03-15', 'F', 2),
('Nganga', 'Fabrice', '2001-04-10', 'H', 3),
('Tchicaya', 'Josiane', '2002-05-05', 'F', 4),
('Bakoua', 'Samuel', '1998-06-25', 'H', 5),
('Kivouvou', 'Antoinette', '1997-07-30', 'F', 6),
('Ondongo', 'Serge', '2000-08-10', 'H', 7),
('Mankessi', 'Laurence', '2001-09-12', 'F', 8),
('Ngolo', 'François', '1999-10-15', 'H', 9),
('Bissila', 'Juliette', '2002-11-20', 'F', 10),
('Kibangou', 'Daniel', '1998-12-05', 'H', 11),
('Mbou', 'Monique', '1997-01-25', 'F', 12),
('Sounga', 'Gilbert', '2000-02-17', 'H', 13),
('Moudoudou', 'Patricia', '2001-03-28', 'F', 14),
('Dibongi', 'Maxime', '1999-04-19', 'H', 15),
('Bikoka', 'Suzanne', '2002-05-23', 'F', 16),
('Tati', 'Alphonse', '2000-06-14', 'H', 17),
('Kouya', 'Catherine', '2001-07-07', 'F', 18),
('Matsima', 'René', '1998-08-01', 'H', 19),
('Kodia', 'Sylvie', '1997-09-16', 'F', 20),
('Massamba', 'Georges', '2000-10-10', 'H', 21),
('Nkossa', 'Martine', '2001-11-09', 'F', 22),
('Moukila', 'Alexandre', '1999-12-12', 'H', 23),
('Samba', 'Jacqueline', '2000-01-15', 'F', 24),
('Mbemba', 'Pierre', '1998-02-19', 'H', 25),
('Moukoko', 'Christelle', '2001-03-21', 'F', 26),
('Boukadia', 'Emmanuel', '1999-04-24', 'H', 27),
('Makita', 'Delphine', '2000-05-27', 'F', 28),
('Moungou', 'Roger', '1998-06-30', 'H', 29),
('Kanza', 'Jeanne', '2001-07-03', 'F', 1),
('Okemba', 'Michel', '1999-08-06', 'H', 2),
('Tchikaya', 'Marceline', '2000-09-09', 'F', 3),
('Boungou', 'David', '2001-10-13', 'H', 4),
('Menga', 'Suzanne', '1998-11-15', 'F', 5),
('Mayala', 'Laurent', '1997-12-18', 'H', 6),
('Ntsika', 'Pauline', '2000-01-21', 'F', 7),
('Dongo', 'Éric', '1999-02-23', 'H', 8),
('Louamba', 'Justine', '2001-03-26', 'F', 9),
('Nzengui', 'Patrick', '1999-04-28', 'H', 10),
('Nsona', 'Mireille', '2000-05-30', 'F', 11),
('Kimpolo', 'Alain', '1998-06-21', 'H', 12),
('Loufoua', 'Evelyne', '2001-07-15', 'F', 13),
('Mbongo', 'Jean-Pierre', '1999-08-17', 'H', 14),
('Moukala', 'Thérèse', '2000-09-19', 'F', 15),
('Pambou', 'Gilbert', '1998-10-21', 'H', 16),
('Loudi', 'Esther', '2001-11-23', 'F', 17),
('Kama', 'Vincent', '1999-12-25', 'H', 18),
('Yila', 'Françoise', '2000-01-27', 'F', 19),
('Bongo', 'Raymond', '1998-02-28', 'H', 20),
('Nzonzi', 'Patricia', '2001-03-31', 'F', 21),
('Koundou', 'Benoît', '1999-04-02', 'H', 22),
('Mankou', 'Pauline', '2000-05-04', 'F', 23),
('Nkama', 'Alexis', '1998-06-06', 'H', 24),
('Nkouka', 'Séverine', '2001-07-08', 'F', 25),
('Ndinga', 'Félix', '1999-08-10', 'H', 26),
('Bouity', 'Joséphine', '2000-09-12', 'F', 27),
('Makosso', 'Pierre', '1998-10-14', 'H', 28),
('Nkoukou', 'Geneviève', '2001-11-16', 'F', 29),
('Kibamba', 'Thomas', '1999-12-18', 'H', 1),
('Mankayi', 'Blandine', '2000-01-20', 'F', 2),
('Koumba', 'Michel', '2000-02-20', 'H', 3),
('Loumou', 'Alice', '1999-03-15', 'F', 4),
('Nganga', 'Fabrice', '2001-04-10', 'H', 5),
('Tchicaya', 'Josiane', '2002-05-05', 'F', 6),
('Bakoua', 'Samuel', '1998-06-25', 'H', 7),
('Kivouvou', 'Antoinette', '1997-07-30', 'F', 8),
('Ondongo', 'Serge', '2000-08-10', 'H', 9),
('Mankessi', 'Laurence', '2001-09-12', 'F', 10),
('Ngolo', 'François', '1999-10-15', 'H', 11),
('Bissila', 'Juliette', '2002-11-20', 'F', 12),
('Kibangou', 'Daniel', '1998-12-05', 'H', 13),
('Mbou', 'Monique', '1997-01-25', 'F', 14),
('Sounga', 'Gilbert', '2000-02-17', 'H', 15),
('Moudoudou', 'Patricia', '2001-03-28', 'F', 16),
('Dibongi', 'Maxime', '1999-04-19', 'H', 17),
('Bikoka', 'Suzanne', '2002-05-23', 'F', 18),
('Tati', 'Alphonse', '2000-06-14', 'H', 19),
('Kouya', 'Catherine', '2001-07-07', 'F', 20),
('Matsima', 'René', '1998-08-01', 'H', 21),
('Kodia', 'Sylvie', '1997-09-16', 'F', 22),
('Massamba', 'Georges', '2000-10-10', 'H', 23),
('Nkossa', 'Martine', '2001-11-09', 'F', 24),
('Moukila', 'Alexandre', '1999-12-12', 'H', 25),
('Samba', 'Jacqueline', '2000-01-15', 'F', 26),
('Mbemba', 'Pierre', '1998-02-19', 'H', 27),
('Moukoko', 'Christelle', '2001-03-21', 'F', 28),
('Boukadia', 'Emmanuel', '1999-04-24', 'H', 29),
('Makita', 'Delphine', '2000-05-27', 'F', 1),
('Moungou', 'Roger', '1998-06-30', 'H', 2),
('Kanza', 'Jeanne', '2001-07-03', 'F', 3),
('Okemba', 'Michel', '1999-08-06', 'H', 4),
('Tchikaya', 'Marceline', '2000-09-09', 'F', 5),
('Boungou', 'David', '2001-10-13', 'H', 6),
('Menga', 'Suzanne', '1998-11-15', 'F', 7),
('Mayala', 'Laurent', '1997-12-18', 'H', 8),
('Ntsika', 'Pauline', '2000-01-21', 'F', 9),
('Dongo', 'Éric', '1999-02-23', 'H', 10),
('Louamba', 'Justine', '2001-03-26', 'F', 1),
('Nzengui', 'Patrick', '1999-04-28', 'H', 2),
('Nsona', 'Mireille', '2000-05-30', 'F', 3),
('Kimpolo', 'Alain', '1998-06-21', 'H', 4),
('Loufoua', 'Evelyne', '2001-07-15', 'F', 5),
('Mbongo', 'Jean-Pierre', '1999-08-17', 'H', 6),
('Moukala', 'Thérèse', '2000-09-19', 'F', 7),
('Pambou', 'Gilbert', '1998-10-21', 'H', 8),
('Loudi', 'Esther', '2001-11-23', 'F', 9),
('Kama', 'Vincent', '1999-12-25', 'H', 10),
('Yila', 'Françoise', '2000-01-27', 'F', 1),
('Bongo', 'Raymond', '1998-02-28', 'H', 2),
('Nzonzi', 'Patricia', '2001-03-31', 'F', 3),
('Koundou', 'Benoît', '1999-04-02', 'H', 4),
('Mankou', 'Pauline', '2000-05-04', 'F', 5),
('Nkama', 'Alexis', '1998-06-06', 'H', 6),
('Nkouka', 'Séverine', '2001-07-08', 'F', 7),
('Ndinga', 'Félix', '1999-08-10', 'H', 8),
('Bouity', 'Joséphine', '2000-09-12', 'F', 9),
('Makosso', 'Pierre', '1998-10-14', 'H', 10),
('Nkoukou', 'Geneviève', '2001-11-16', 'F', 1),
('Kibamba', 'Thomas', '1999-12-18', 'H', 2),
('Mankayi', 'Blandine', '2000-01-20', 'F', 3);


 INSERT INTO inscription (id_étudiant, id_classe) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20),
(21, 21),
(22, 22),
(23, 23),
(24, 24),
(25, 25),
(26, 26),
(27, 27),
(28, 28),
(29, 29),
(30, 1),
(31, 2),
(32, 3),
(33, 4),
(34, 5),
(35, 6),
(36, 7),
(37, 8),
(38, 9),
(39, 10),
(40, 11),
(41, 12),
(42, 13),
(43, 14),
(44, 15),
(45, 16),
(46, 17),
(47, 18),
(48, 19),
(49, 20),
(50, 21),
(51, 22),
(52, 23),
(53, 24),
(54, 25),
(55, 26),
(56, 27),
(57, 28),
(58, 29),
(59, 1),
(60, 2),
(61, 3),
(62, 4),
(63, 5),
(64, 6),
(65, 7),
(66, 8),
(67, 9),
(68, 10),
(69, 11),
(70, 12),
(71, 13),
(72, 14),
(73, 15),
(74, 16),
(75, 17),
(76, 18),
(77, 19),
(78, 20),
(79, 21),
(80, 22),
(81, 23),
(82, 24),
(83, 25),
(84, 26),
(85, 27),
(86, 28),
(87, 29),
(88, 1),
(89, 2),
(90, 3),
(91, 4),
(92, 5),
(93, 6),
(94, 7),
(95, 8),
(96, 9),
(97, 10),
(98, 11),
(99, 12),
(100, 13),
(101, 14),
(102, 15),
(103, 16),
(104, 17),
(105, 18),
(106, 19),
(107, 20),
(108, 21),
(109, 22),
(110, 23),
(111, 24),
(112, 25),
(113, 26),
(114, 27),
(115, 28),
(116, 29),
(117, 1),
(118, 2),
(119, 3),
(120, 4),
(121, 5),
(122, 6),
(123, 7),
(124, 8),
(125, 9),
(126, 10),
(127, 11),
(128, 12),
(129, 13),
(130, 14),
(131, 15),
(132, 16),
(133, 17),
(134, 18),
(135, 19),
(136, 20),
(137, 21),
(138, 22),
(139, 23),
(140, 24),
(141, 25),
(142, 26),
(143, 27),
(144, 28),
(145, 29),
(146, 1),
(147, 2),
(148, 3),
(149, 4),
(150, 5),
(151, 6),
(152, 7),
(153, 8),
(154, 9),
(155, 10),
(156, 11),
(157, 12),
(158, 13),
(159, 14),
(160, 15),
(161, 16),
(162, 17),
(163, 18),
(164, 19),
(165, 20),
(166, 21),
(167, 22),
(168, 23),
(169, 24),
(170, 25),
(171, 26),
(172, 27),
(173, 28),
(174, 29),
(175, 1),
(176, 2),
(177, 3),
(178, 4),
(179, 5),
(180, 6);

 
 

INSERT INTO semestre (id_classe, id_enseignant, id_matière, semestre, nom_semestre) VALUES
-- Semestre 1
(1, 7, 6, 1, 'Semestre 1 - TC1'),   -- TC1, Bruno Mavoungou, MySQL
(2, 8, 7, 1, 'Semestre 1 - TC2'),   -- TC2, Claudine Nzobo, PostgreSQL
(3, 9, 8, 1, 'Semestre 1 - TC3'),   -- TC3, Alain Bokoko, Web Development
(4, 10, 9, 1, 'Semestre 1 - TC4'),  -- TC4, Isabelle Kodia, Anglais
(5, 11, 10, 1, 'Semestre 1 - TC5'), -- TC5, Bernard Bakala, Français
(6, 12, 11, 1, 'Semestre 1 - TC6'), -- TC6, Sophie Bakou, Oracle
(7, 13, 12, 1, 'Semestre 1 - TC7'), -- TC7, Pierre Kounga, Data Structures and Algorithms
(8, 14, 13, 1, 'Semestre 1 - TC8'), -- TC8, Thierry Koubemba, Cloud Computing
(9, 15, 14, 1, 'Semestre 1 - TC9'), -- TC9, Jean-Pierre Lemba, Logistique et Supply Chain
(10, 16, 15, 1, 'Semestre 1 - TC10'),  -- TC10, Marie Mabiala, Finance
(11, 17, 16, 1, 'Semestre 1 - TC11'),  -- TC11, Gérard Mabounda, Marketing Digital
(12, 18, 17, 1, 'Semestre 1 - TC12'),  -- TC12, Jean Makanda, Marketing
(13, 19, 18, 1, 'Semestre 1 - TC13'),  -- TC13, Chantal Mambou, Stratégie
(14, 20, 19, 1, 'Semestre 1 - TC14'),  -- TC14, Jacques Mfoutou, Audit
(15, 21, 20, 1, 'Semestre 1 - TC15'),  -- TC15, Florence Mfoula, Stratégie d'Entreprise
(16, 22, 21, 1, 'Semestre 1 - TC16'),  -- TC16, Aline Mouanga, Systèmes d'Information
(17, 23, 22, 1, 'Semestre 1 - TC17'),  -- TC17, Sylvie Moussoki, Logistique
(18, 24, 23, 1, 'Semestre 1 - TC18'),  -- TC18, François Moumba, Marketing Stratégique
(19, 25, 24, 1, 'Semestre 1 - TC19'),  -- TC19, Christelle Nkodia, Communication
(20, 26, 25, 1, 'Semestre 1 - TC20'),  -- TC20, Paul Nkounkou, Comptabilité
(21, 27, 26, 1, 'Semestre 1 - TC21'),  -- TC21, Suzanne Ngouabi, Business Intelligence
(22, 28, 27, 1, 'Semestre 1 - TC22'),  -- TC22, Catherine Nsoni, Ressources Humaines
(23, 29, 28, 1, 'Semestre 1 - PROGRAMMATION'),  -- PROGRAMMATION, Luc Ongali, Management
(24, 30, 29, 1, 'Semestre 1 - ANAPRO'),  -- ANAPRO, Marina Ossali, Finance Internationale
(25, 1, 30, 1, 'Semestre 1 - LPGL'),  -- LPGL, Estelle Ouangolo, Gestion des Risques
(26, 2, 1, 1, 'Semestre 1 - LPABD'),  -- LPABD, Robert Ouabari, Relations Internationales
-- Semestre 2
(1, 8, 1, 2, 'Semestre 2 - TC1'),    -- TC1, Marie Nkouka, Django
(2, 9, 2, 2, 'Semestre 2 - TC2'),    -- TC2, Patrick Mbemba, MongoDB
(3, 10, 3, 2, 'Semestre 2 - TC3'),   -- TC3, Sophia Makaya, Finance
(4, 11, 4, 2, 'Semestre 2 - TC4'),   -- TC4, Alain Mabiala, Gestion de Projet
(5, 12, 5, 2, 'Semestre 2 - TC5'),   -- TC5, Félicité Sassou, Ressources Humaines
(6, 13, 6, 2, 'Semestre 2 - TC6'),   -- TC6, Bruno Mavoungou, Informatique
(7, 14, 7, 2, 'Semestre 2 - TC7'),   -- TC7, Claudine Nzobo, Droit
(8, 15, 8, 2, 'Semestre 2 - TC8'),   -- TC8, Alphonse Bokoko, Économie
(9, 16, 9, 2, 'Semestre 2 - TC9'),   -- TC9, Isabelle Kodia, Gestion
(10, 17, 10, 2, 'Semestre 2 - TC10'),  -- TC10, Bernard Bakala, Analyse Financière
(11, 18, 11, 2, 'Semestre 2 - TC11'),  -- TC11, Sophie Bakou, Ressources Humaines
(12, 19, 12, 2, 'Semestre 2 - TC12'),  -- TC12, Pierre Kounga, Innovation Technologique
(13, 20, 13, 2, 'Semestre 2 - TC13'),  -- TC13, Thierry Koubemba, Logistique et Supply Chain
(14, 21, 14, 2, 'Semestre 2 - TC14'),  -- TC14, Jean-Pierre Lemba, Management de Projet
(15, 22, 15, 2, 'Semestre 2 - TC15'),  -- TC15, Marie Mabiala, Finance
(16, 23, 16, 2, 'Semestre 2 - TC16'),  -- TC16, Gérard Mabounda, Marketing Digital
(17, 24, 17, 2, 'Semestre 2 - TC17'),  -- TC17, Jean Makanda, Marketing
(18, 25, 18, 2, 'Semestre 2 - TC18'),  -- TC18, Chantal Mambou, Stratégie
(19, 26, 19, 2, 'Semestre 2 - TC19'),  -- TC19, Jacques Mfoutou, Audit
(20, 27, 20, 2, 'Semestre 2 - TC20'),  -- TC20, Florence Mfoula, Stratégie d'Entreprise
(21, 28, 21, 2, 'Semestre 2 - TC21'),  -- TC21, Aline Mouanga, Systèmes d'Information
(22, 29, 22, 2, 'Semestre 2 - TC22'),  -- TC22, Sylvie Moussoki, Logistique
(23, 30, 23, 2, 'Semestre 2 - PROGRAMMATION'),  -- PROGRAMMATION, François Moumba, Marketing Stratégique
(24, 1, 24, 2, 'Semestre 2 - ANAPRO'),  -- ANAPRO, Christelle Nkodia, Communication
(25, 2, 25, 2, 'Semestre 2 - LPGL'),  -- LPGL, Paul Nkounkou, Comptabilité
(26, 3, 26, 2, 'Semestre 2 - LPABD');  -- LPABD, Suzanne Ngouabi, Business Intelligence


INSERT INTO programme (id_classe, id_matière) VALUES
(1, 1), (1, 2), (1, 3),
(2, 4), (2, 5), (2, 6),
(3, 7), (3, 8), (3, 9),
(4, 10), (4, 11), (4, 12),
(5, 13), (5, 14), (5, 15),
(6, 16), (6, 17), (6, 18),
(7, 19), (7, 20), (7, 21),
(8, 1), (8, 2), (8, 3),
(9, 4), (9, 5), (9, 6),
(10, 7), (10, 8), (10, 9),
(11, 10), (11, 11), (11, 12),
(12, 13), (12, 14), (12, 15),
(13, 16), (13, 17), (13, 18),
(14, 19), (14, 20), (14, 21),
(15, 1), (15, 2), (15, 3),
(16, 4), (16, 5), (16, 6),
(17, 7), (17, 8), (17, 9),
(18, 10), (18, 11), (18, 12),
(19, 13), (19, 14), (19, 15),
(20, 16), (20, 17), (20, 18),
(21, 19), (21, 20), (21, 21),
(22, 1), (22, 2), (22, 3),
(23, 4), (23, 5), (23, 6),
(24, 7), (24, 8), (24, 9),
(25, 10), (25, 11), (25, 12),
(26, 13), (26, 14), (26, 15),
(27, 16), (27, 17), (27, 18),
(28, 19), (28, 20), (28, 21),
(29, 22), (29, 23), (29, 24),
(29, 25), (29, 26), (29, 27)
;


INSERT INTO note (id_étudiant, id_enseignant, id_matière, note, commentaire, date_évaluation)
VALUES
(1, 1, 1, 15.50, 'Bon travail.', '2023-01-15'),
(2, 2, 2, 12.00, 'Peut mieux faire.', '2023-01-20'),
(3, 3, 3, 14.50, 'Très bien.', '2023-02-25'),
(4, 4, 4, 16.00, 'Excellent.', '2023-03-10'),
(5, 5, 5, 10.00, 'Besoin de plus d’efforts.', '2023-03-20'),
(6, 6, 6, 11.00, 'Travail acceptable.', '2023-04-15'),
(7, 7, 7, 13.50, 'Bon progrès.', '2023-04-30'),
(8, 8, 8, 18.00, 'Exceptionnel.', '2023-05-10'),
(9, 9, 9, 9.50, 'Doit s’améliorer.', '2023-05-25'),
(10, 10, 10, 17.00, 'Très bon travail.', '2023-06-05'),
(11, 11, 11, 14.00, 'Bon effort.', '2023-06-15'),
(12, 12, 12, 13.00, 'Satisfaisant.', '2023-07-01'),
(13, 13, 13, 15.00, 'Bien fait.', '2023-07-10'),
(14, 14, 14, 12.50, 'Correct.', '2023-07-20'),
(15, 15, 15, 19.00, 'Excellent travail.', '2023-08-01'),
(16, 16, 16, 10.00, 'Satisfaisant.', '2023-08-15'),
(17, 17, 17, 8.50, 'Besoin d’amélioration.', '2023-09-01'),
(18, 18, 18, 11.55, 'Bon travail.', '2023-09-15'),
(19, 19, 19, 14.50, 'Très bien.', '2023-09-25'),
(20, 20, 20, 15.00, 'Bien fait.', '2023-10-05'),
(21, 21, 21, 12.00, 'Peut mieux faire.', '2023-10-15'),
(22, 22, 22, 16.50, 'Excellent.', '2023-10-25'),
(23, 23, 23, 13.00, 'Satisfaisant.', '2023-11-05'),
(24, 24, 24, 17.50, 'Très bon travail.', '2023-11-15'),
(25, 25, 25, 9.00, 'Doit s’améliorer.', '2023-11-25'),
(26, 26, 26, 11.00, 'Travail acceptable.', '2023-12-01'),
(27, 27, 27, 14.00, 'Bon effort.', '2023-12-10'),
(28, 28, 28, 19.50, 'Exceptionnel.', '2023-12-20'),
(29, 29, 29, 10.50, 'Besoin de plus d’efforts.', '2024-01-10'),
(30, 30, 30, 16.00, 'Très bon travail.', '2024-01-20'),
(31, 31, 1, 15.00, 'Très bien.', '2024-02-01'),
(32, 32, 2, 13.50, 'Bon progrès.', '2024-02-15'),
(33, 33, 3, 11.00, 'Travail acceptable.', '2024-02-28'),
(34, 34, 4, 18.00, 'Exceptionnel.', '2024-03-10'),
(35, 1, 5, 12.00, 'Peut mieux faire.', '2024-03-20'),
(36, 2, 6, 14.50, 'Très bien.', '2024-04-01'),
(37, 3, 7, 9.50, 'Doit s’améliorer.', '2024-04-15'),
(38, 4, 8, 17.00, 'Très bon travail.', '2024-04-30'),
(39, 5, 9, 10.00, 'Satisfaisant.', '2024-05-10'),
(40, 6, 10, 16.50, 'Excellent.', '2024-05-25'),
(41, 7, 11, 11.50, 'Bon travail.', '2024-06-05'),
(42, 9, 12, 14.00, 'Bon effort.', '2024-06-15'),
(43, 10, 13, 16.00, 'Satisfaisant.', '2024-06-30'),
(44, 11, 14, 8.50, 'Besoin d’amélioration.', '2024-07-10'),
(45, 12, 15, 19.00, 'Excellent travail.', '2024-07-20'),
(46, 13, 16, 10.50, 'Besoin de plus d’efforts.', '2024-08-01'),
(47, 14, 17, 17.50, 'Très bon travail.', '2024-08-15'),
(48, 15, 18, 13.00, 'Satisfaisant.', '2024-09-01'),
(49, 16, 19, 12.00, 'Peut mieux faire.', '2024-09-15'),
(50, 17, 20, 15.50, 'Bon travail.', '2024-09-25'),
(51, 18, 21, 18.00, 'Exceptionnel.', '2024-01-05'),
(52, 19, 22, 9.50, 'Doit s’améliorer.', '2024-01-15'),
(53, 20, 23, 14.00, 'Bon effort.', '2024-01-30'),
(54, 21, 24, 16.00, 'Très bon travail.', '2024-02-10'),
(55, 22, 25, 12.50, 'Correct.', '2024-02-20'),
(56, 23, 26, 15.00, 'Bien fait.', '2024-03-01'),
(57, 24, 27, 11.00, 'Travail acceptable.', '2024-03-15'),
(58, 25, 28, 17.00, 'Très bon travail.', '2024-03-30'),
(59, 26, 29, 10.00, 'Satisfaisant.', '2024-04-10'),
(60, 27, 30, 13.50, 'Bon progrès.', '2024-04-25'),
(61, 28, 1, 15.50, 'Bon travail.', '2024-05-05'),
(62, 29, 2, 13.00, 'Satisfaisant.', '2024-05-15'),
(63, 30, 3, 11.50, 'Bon travail.', '2024-05-28'),
(64, 31, 4, 16.50, 'Excellent.', '2024-06-10'),
(65, 32, 5, 9.00, 'Doit s’améliorer.', '2024-06-20'),
(66, 33, 6, 14.00, 'Bon effort.', '2024-07-01'),
(67, 34, 7, 17.00, 'Très bon travail.', '2024-07-15'),
(68, 1, 8, 12.00, 'Peut mieux faire.', '2024-07-30'),
(69, 2, 9, 19.00, 'Excellent travail.', '2024-08-10'),
(70, 3, 10, 10.50, 'Besoin de plus d’efforts.', '2024-08-25'),
(71, 4, 11, 14.50, 'Très bien.', '2024-09-05'),
(72, 5, 12, 8.00, 'Besoin d’amélioration.', '2024-09-15'),
(73, 6, 13, 16.50, 'Excellent.', '2023-12-30'),
(74, 7, 14, 12.00, 'Peut mieux faire.', '2024-01-10'),
(75, 8, 15, 14.50, 'Très bien.', '2024-01-20'),
(76, 9, 16, 11.50, 'Bon travail.', '2024-02-01'),
(77, 10, 17, 18.00, 'Exceptionnel.', '2024-02-15'),
(78, 11, 18, 10.00, 'Travail acceptable.', '2024-02-28'),
(79, 12, 19, 13.50, 'Bon progrès.', '2024-03-10'),
(80, 13, 20, 15.00, 'Bien fait.', '2024-03-25'),
(81, 14, 21, 17.00, 'Très bon travail.', '2024-04-05'),
(82, 15, 22, 9.00, 'Doit s’améliorer.', '2024-04-15'),
(83, 16, 23, 11.00, 'Travail acceptable.', '2024-04-30'),
(84, 17, 24, 14.00, 'Bon effort.', '2024-05-10'),
(85, 18, 25, 16.50, 'Excellent.', '2024-05-20'),
(86, 19, 26, 13.00, 'Satisfaisant.', '2024-06-01'),
(87, 20, 27, 15.50, 'Bon travail.', '2024-06-15'),
(88, 21, 28, 12.50, 'Correct.', '2024-06-30'),
(89, 22, 29, 8.50, 'Besoin d’amélioration.', '2024-07-10'),
(90, 23, 30, 19.00, 'Excellent travail.', '2024-07-20'),
(91, 24, 1, 10.50, 'Besoin de plus d’efforts.', '2024-08-01'),
(92, 25, 2, 17.50, 'Très bon travail.', '2024-08-15'),
(93, 26, 3, 13.50, 'Bon progrès.', '2024-08-30'),
(94, 27, 4, 15.00, 'Bien fait.', '2024-09-10'),
(95, 28, 5, 11.00, 'Travail acceptable.', '2024-09-20'),
(96, 29, 6, 16.00, 'Satisfaisant.', '2024-10-01'),
(97, 30, 7, 9.00, 'Doit s’améliorer.', '2024-10-15'),
(98, 31, 8, 14.00, 'Bon effort.', '2024-10-30'),
(99, 32, 9, 18.50, 'Exceptionnel.', '2024-11-10'),
(100, 33, 10, 12.00, 'Peut mieux faire.', '2024-11-25'),
(101, 34, 11, 14.00, 'Bon effort.', '2023-12-15'),
(102, 1, 12, 13.50, 'Bon progrès.', '2023-12-25'),
(103, 2, 13, 16.00, 'Satisfaisant.', '2024-01-05'),
(104, 3, 14, 10.00, 'Doit s’améliorer.', '2024-01-15'),
(105, 4, 15, 17.00, 'Très bon travail.', '2024-01-30'),
(106, 5, 16, 11.50, 'Bon travail.', '2024-02-10'),
(107, 6, 17, 15.50, 'Bien fait.', '2024-02-20'),
(108, 7, 18, 9.00, 'Besoin d’amélioration.', '2024-03-05'),
(109, 8, 19, 18.00, 'Exceptionnel.', '2024-03-15'),
(110, 9, 20, 12.50, 'Correct.', '2024-03-30'),
(111, 10, 21, 14.50, 'Très bien.', '2024-04-10'),
(112, 11, 22, 11.00, 'Travail acceptable.', '2024-04-20'),
(113, 12, 23, 19.00, 'Excellent travail.', '2024-05-05'),
(114, 13, 24, 8.50, 'Besoin d’amélioration.', '2024-05-15'),
(115, 14, 25, 16.50, 'Excellent.', '2024-05-30'),
(116, 15, 26, 13.00, 'Satisfaisant.', '2024-06-10'),
(117, 16, 27, 10.50, 'Besoin de plus d’efforts.', '2024-06-20'),
(118, 17, 28, 15.00, 'Bon travail.', '2024-07-05'),
(119, 18, 29, 12.00, 'Peut mieux faire.', '2024-07-15'),
(120, 19, 30, 17.00, 'Très bon travail.', '2024-07-30'),
(121, 20, 1, 11.00, 'Travail acceptable.', '2024-08-10'),
(122, 21, 2, 14.00, 'Bon effort.', '2024-08-20'),
(123, 22, 3, 17.50, 'Très bon travail.', '2024-09-05'),
(124, 23, 4, 9.50, 'Doit s’améliorer.', '2024-09-15'),
(125, 24, 5, 13.50, 'Bon progrès.', '2024-09-30'),
(126, 25, 6, 18.50, 'Exceptionnel.', '2024-10-10'),
(127, 26, 7, 12.00, 'Peut mieux faire.', '2024-10-20'),
(128, 27, 8, 16.00, 'Satisfaisant.', '2024-11-04'),
(129, 28, 9, 10.00, 'Travail acceptable.', '2024-11-14'),
(130, 29, 10, 14.00, 'Bon effort.', '2024-11-30'),
(131, 30, 11, 15.50, 'Bon travail.', '2024-12-10'),
(132, 31, 12, 11.50, 'Bon travail.', '2024-12-20'),
(133, 32, 13, 16.00, 'Satisfaisant.', '2023-01-05'),
(134, 33, 14, 10.50, 'Besoin de plus d’efforts.', '2023-01-15'),
(135, 34, 15, 17.50, 'Très bon travail.', '2023-01-30'),
(136, 1, 16, 12.50, 'Correct.', '2023-02-10'),
(137, 2, 17, 15.00, 'Bien fait.', '2023-02-20'),
(138, 3, 18, 8.00, 'Besoin d’amélioration.', '2023-03-05'),
(139, 4, 19, 18.00, 'Exceptionnel.', '2023-03-15'),
(140, 5, 20, 13.50, 'Bon progrès.', '2023-03-30'),
(141, 6, 21, 14.50, 'Très bien.', '2023-04-10'),
(142, 7, 22, 10.00, 'Doit s’améliorer.', '2023-04-20'),
(143, 8, 23, 18.00, 'Excellent travail.', '2023-05-05'),
(144, 9, 24, 9.00, 'Besoin d’amélioration.', '2023-05-15'),
(145, 10, 25, 16.00, 'Excellent.', '2023-05-30'),
(146, 11, 26, 14.00, 'Satisfaisant.', '2023-06-10'),
(147, 12, 27, 11.00, 'Travail acceptable.', '2023-06-20'),
(148, 13, 28, 15.50, 'Bon travail.', '2023-07-05'),
(149, 14, 29, 11.00, 'Peut mieux faire.', '2024-07-15'),
(150, 15, 30, 17.00, 'Très bon travail.', '2024-07-30'),
(151, 16, 1, 12.00, 'Peut mieux faire.', '2023-06-05'),
(152, 17, 2, 13.00, 'Satisfaisant.', '2023-06-15'),
(153, 18, 3, 15.00, 'Bien fait.', '2023-06-30'),
(154, 19, 4, 11.50, 'Bon travail.', '2023-07-10'),
(155, 20, 5, 19.00, 'Excellent travail.', '2023-07-20'),
(156, 21, 6, 10.00, 'Satisfaisant.', '2023-08-01'),
(157, 22, 7, 8.50, 'Besoin d’amélioration.', '2023-08-15'),
(158, 23, 8, 11.50, 'Bon travail.', '2023-08-30'),
(159, 24, 9, 14.50, 'Très bien.', '2023-09-10'),
(160, 25, 10, 15.00, 'Bien fait.', '2023-09-20'),
(161, 26, 11, 12.00, 'Peut mieux faire.', '2023-10-05'),
(162, 27, 12, 16.50, 'Excellent.', '2023-10-15'),
(163, 28, 13, 13.00, 'Satisfaisant.', '2023-10-30'),
(164, 29, 14, 17.50, 'Très bon travail.', '2023-11-10'),
(165, 30, 15, 9.00, 'Doit s’améliorer.', '2023-11-20'),
(166, 31, 16, 11.00, 'Travail acceptable.', '2023-12-01'),
(167, 32, 17, 14.00, 'Bon effort.', '2023-12-15'),
(168, 33, 18, 19.50, 'Exceptionnel.', '2023-12-30'),
(169, 34, 19, 10.50, 'Besoin de plus d’efforts.', '2023-12-10'),
(170, 1, 20, 16.00, 'Très bon travail.', '2023-12-20'),
(171, 2, 21, 18.00, 'Exceptionnel.', '2023-01-05'),
(172, 3, 22, 9.50, 'Doit s’améliorer.', '2023-01-15'),
(173, 4, 23, 14.00, 'Bon effort.', '2023-01-30'),
(174, 5, 24, 16.00, 'Très bon travail.', '2023-02-10'),
(175, 6, 25, 12.50, 'Correct.', '2023-02-20'),
(176, 7, 26, 15.00, 'Bien fait.', '2023-03-01'),
(177, 8, 27, 11.00, 'Travail acceptable.', '2023-03-15'),
(178, 9, 28, 17.00, 'Très bon travail.', '2023-03-30'),
(179, 10, 29, 10.00, 'Satisfaisant.', '2023-04-10'),
(180, 1, 30, 13.50, 'Bon progrès.', '2023-04-25');



 INSERT INTO enseigne (id_enseignant, id_matière, id_classe) VALUES

    -- Enseignant 1
    (1, 1, 1), (1, 2, 2), (1, 3, 3),
    (1, 10, 9), (1, 11, 10), (1, 12, 11),
    (1, 19, 9), (1, 20, 10), (1, 21, 11),
    -- Enseignant 2
    (2, 4, 4), (2, 5, 5), (2, 6, 6),
    (2, 13, 12), (2, 14, 13), (2, 15, 14),
    (2, 1, 12), (2, 2, 13), (2, 3, 14),
    -- Enseignant 3
    (3, 7, 7), (3, 8, 8), (3, 9, 9),
    (3, 16, 15), (3, 17, 16), (3, 18, 17),
    (3, 4, 15), (3, 5, 16), (3, 6, 17),
    -- Enseignant 4
    (4, 10, 10), (4, 11, 11), (4, 12, 12),
    (4, 19, 18), (4, 20, 19), (4, 21, 20),
    (4, 7, 18), (4, 8, 19), (4, 9, 20),
    -- Enseignant 5
    (5, 13, 13), (5, 14, 14), (5, 15, 15),
    (5, 1, 21), (5, 2, 22), (5, 3, 23),
    (5, 10, 21), (5, 11, 22), (5, 12, 23),
    -- Enseignant 6
    (6, 16, 16), (6, 17, 17), (6, 18, 18),
    (6, 1, 24), (6, 2, 25), (6, 3, 26),
    (6, 13, 24), (6, 14, 25), (6, 15, 26),
    -- Enseignant 7
    (7, 19, 19), (7, 20, 20), (7, 21, 21),
    (7, 16, 27), (7, 17, 28), (7, 18, 29),
    (7, 4, 27), (7, 5, 28), (7, 6, 29),
    -- Enseignant 8
    (8, 1, 22), (8, 2, 1), (8, 3, 2),
    (8, 10, 29), (8, 11, 1), (8, 12, 2),
    (8, 19, 29), (8, 20, 1), (8, 21, 2),
    -- Enseignant 9
    (9, 4, 3), (9, 5, 4), (9, 6, 5),
    (9, 13, 3), (9, 14, 4), (9, 15, 5),
    (9, 1, 3), (9, 2, 4), (9, 3, 5),
    -- Enseignant 10
    (10, 7, 6), (10, 8, 7), (10, 9, 8),
    (10, 17, 7), (10, 18, 8),
    (10, 4, 6), (10, 5, 7), (10, 6, 8),
    -- Enseignant 11
    (11, 7, 9), (11, 8, 10), (11, 9, 11),
    (11, 10, 9), (11, 11, 10), (11, 12, 11),
    (11, 19, 9), (11, 20, 10), (11, 21, 11),
    -- Enseignant 12
    (12, 10, 12), (12, 11, 13), (12, 12, 14),
    (12, 13, 12), (12, 14, 13), (12, 15, 14),
    (12, 1, 12), (12, 2, 13), (12, 3, 14),
    -- Enseignant 13
    (13, 16, 15), (13, 17, 16), (13, 18, 17),
    (13, 19, 18), (13, 20, 19), (13, 21, 20),
    (13, 7, 18), (13, 8, 19), (13, 9, 20),
    -- Enseignant 14
    (14, 13, 15), (14, 14, 16), (14, 15, 17),
    (14, 16, 18), (14, 17, 19), (14, 18, 20),
    (14, 19, 21), (14, 20, 22), (14, 21, 23),
    -- Enseignant 15
    (15, 1, 21), (15, 2, 22), (15, 3, 23),
    (15, 10, 21), (15, 11, 22), (15, 12, 23),
    (15, 16, 27), (15, 17, 28), (15, 18, 29),
    -- Enseignant 16
    (16, 4, 27), (16, 5, 28), (16, 6, 29),
    (16, 1, 24), (16, 2, 25), (16, 3, 26),
    (16, 13, 24), (16, 14, 25), (16, 15, 26),
    -- Enseignant 17
    (17, 7, 27), (17, 8, 28), (17, 9, 29),
    (17, 10, 29), (17, 11, 1), (17, 12, 2),
    (17, 1, 22), (17, 2, 1), (17, 3, 2),
    -- Enseignant 18
    (18, 4, 3), (18, 5, 4), (18, 6, 5),
    (18, 13, 3), (18, 14, 4), (18, 15, 5),
    (18, 10, 3), (18, 11, 4), (18, 12, 5),
    -- Enseignant 19
    (19, 7, 6), (19, 8, 7), (19, 9, 8),
    (19, 16, 15), (19, 17, 16), (19, 18, 17),
    (19, 4, 15), (19, 5, 16), (19, 6, 17),
    -- Enseignant 20
    (20, 19, 19), (20, 20, 20), (20, 21, 21),
    (20, 1, 24), (20, 2, 25), (20, 3, 26),
    (20, 7, 27), (20, 8, 28), (20, 9, 29),
    -- Enseignant 21
    (21, 10, 29), (21, 11, 1), (21, 12, 2),
    (21, 16, 27), (21, 17, 28), (21, 18, 29),
    (21, 19, 29), (21, 20, 1), (21, 21, 2),
    -- Enseignant 22
    (22, 4, 6), (22, 5, 7), (22, 6, 8),
    (22, 13, 6), (22, 14, 7), (22, 15, 8),
    (22, 1, 9), (22, 2, 10), (22, 3, 11),
    -- Enseignant 23
    (23, 7, 12), (23, 8, 13), (23, 9, 14),
    (23, 16, 15), (23, 17, 16), (23, 18, 17),
    (23, 4, 15), (23, 5, 16), (23, 6, 17),
    -- Enseignant 24
    (24, 19, 18), (24, 20, 19), (24, 21, 20),
    (24, 7, 18), (24, 8, 19), (24, 9, 20),
    (24, 10, 21), (24, 11, 22), (24, 12, 23),
    -- Enseignant 25
    (25, 1, 24), (25, 2, 25), (25, 3, 26),
    (25, 10, 21), (25, 11, 22), (25, 12, 23),
    (25, 16, 27), (25, 17, 28), (25, 18, 29),
    -- Enseignant 26
    (26, 4, 27), (26, 5, 28), (26, 6, 29),
    (26, 19, 29), (26, 20, 1), (26, 21, 2),
    (26, 7, 27), (26, 8, 28), (26, 9, 29),
    -- Enseignant 27
    (27, 10, 29), (27, 11, 1), (27, 12, 2),
    (27, 13, 3), (27, 14, 4), (27, 15, 5),
    (27, 1, 3), (27, 2, 4), (27, 3, 5),
    -- Enseignant 28
    (28, 4, 6), (28, 5, 7), (28, 6, 8),
    (28, 7, 9), (28, 8, 10), (28, 9, 11),
    (28, 16, 15), (28, 17, 16), (28, 18, 17),
    --Enseignant 29
    (29, 19, 18), (29, 20, 19), (29, 21, 20),
    (29, 10, 9), (29, 11, 10), (29, 12, 11),
    (29, 7, 27), (29, 8, 28), (29, 9, 29),
    -- Enseignant 30
    (30, 13, 6), (30, 14, 7), (30, 15, 8),
    (30, 16, 27), (30, 17, 28), (30, 18, 29),
    (30, 19, 29), (30, 20, 1), (30, 21, 2),
    -- Enseignant 31
    (31, 1, 3), (31, 2, 4), (31, 3, 5),
    (31, 4, 6), (31, 5, 7), (31, 6, 8),
    (31, 7, 9), (31, 8, 10), (31, 9, 11),
    -- Enseignant 32
    (32, 10, 12), (32, 11, 13), (32, 12, 14),
    (32, 13, 15), (32, 14, 16), (32, 15, 17),
    -- Enseignant 32 
    (32, 16, 18), (32, 17, 19), (32, 18, 20),
    (32, 19, 21), (32, 20, 22), (32, 21, 23),
    -- Enseignant 33
    (33, 1, 21), (33, 2, 22), (33, 3, 23),
    (33, 4, 24), (33, 5, 25), (33, 6, 26),
    (33, 7, 27), (33, 8, 28), (33, 9, 29),
    -- Enseignant 34
    (34, 10, 29), (34, 11, 1), (34, 12, 2),
    (34, 13, 3), (34, 14, 4), (34, 15, 5),
    (34, 16, 6), (34, 17, 7), (34, 18, 8);








 


