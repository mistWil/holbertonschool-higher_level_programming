-- Script : create_unique_id_table.sql

-- Créer la table unique_id si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
