-- Script : 2-create_read_user.sql

-- Créer la base de données hbtn_0d_2 si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Créer l'utilisateur user_0d_2 avec le mot de passe user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accorder le privilège SELECT à l'utilisateur user_0d_2 sur la base de données hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
