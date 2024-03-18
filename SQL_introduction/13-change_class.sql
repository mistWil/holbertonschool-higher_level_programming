-- Script : remove_low_score_records.sql

-- Supprimer tous les enregistrements avec un score <= 5 de la table second_table
DELETE FROM second_table
WHERE score <= 5;
