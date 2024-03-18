-- Script : create_id_not_null_table.sql

-- Créer la table id_not_null si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
