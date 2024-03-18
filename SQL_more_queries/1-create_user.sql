-- Script : create_user_0d_1.sql

-- Créer l'utilisateur user_0d_1 s'il n'existe pas déjà et lui accorder tous les privilèges sur le serveur MySQL
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges à l'utilisateur user_0d_1 sur le serveur MySQL
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Actualiser les privilèges pour refléter les changements
FLUSH PRIVILEGES;
