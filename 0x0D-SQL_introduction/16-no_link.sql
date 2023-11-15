-- Script to list records from 'second_table' with a name value, ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
