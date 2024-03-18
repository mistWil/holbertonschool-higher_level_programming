-- Script : list_california_cities.sql

-- Sélectionner l'ID de l'État de Californie
SET @state_id := (SELECT id FROM states WHERE name = 'California');

-- Sélectionner toutes les villes de Californie en utilisant l'ID de l'État
SELECT cities.id, cities.name
FROM cities
WHERE state_id = @state_id
ORDER BY cities.id ASC;
