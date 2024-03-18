-- Script : 5-full_table.sql

-- Afficher la description complète de la table first_table
SELECT
    TABLE_SCHEMA AS 'Database',
    TABLE_NAME AS 'Table',
    CREATE_TABLE AS 'Create Table'
FROM
    information_schema.TABLES
WHERE
    TABLE_SCHEMA = 'hbtn_0c_0'
    AND TABLE_NAME = 'first_table';
