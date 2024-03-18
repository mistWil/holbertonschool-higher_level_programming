-- Script : list_score_counts.sql

-- Lister le nombre d'enregistrements avec le même score
SELECT score, COUNT(*) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY number DESC;
