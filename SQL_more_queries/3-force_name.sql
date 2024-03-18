-- Script : create_force_name_table.sql

-- Créer la table force_name si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS force_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
