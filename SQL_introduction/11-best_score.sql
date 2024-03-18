-- Script : list_high_score_records.sql

-- Afficher toutes les lignes avec un score >= 10 de la table second_table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
