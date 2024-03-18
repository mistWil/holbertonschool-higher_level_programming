-- Script : list_records_with_names.sql

-- Lister tous les enregistrements avec un nom dans la table second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
