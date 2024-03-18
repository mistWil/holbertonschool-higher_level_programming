-- Script : list_cities_with_states.sql

-- Sélectionner les villes avec les noms de leurs états correspondants
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
