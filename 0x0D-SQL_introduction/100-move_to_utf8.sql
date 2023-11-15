-- Script to convert 'hbtn_0c_0' database, 'first_table', and 'name' field to UTF8

-- Select the database
USE hbtn_0c_0;

-- Convert the entire table, affecting all character columns
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
