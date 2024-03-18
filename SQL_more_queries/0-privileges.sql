-- Ce script affiche les privilèges accordés aux utilisateurs user_0d_1 et user_0d_2 sur le serveur MySQL (localhost).

-- Afficher les privilèges de l'utilisateur user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Afficher les privilèges de l'utilisateur user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
