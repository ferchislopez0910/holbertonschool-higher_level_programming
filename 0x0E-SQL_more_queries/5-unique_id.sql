-- Write a script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(id int NOT NULL DEFAULT '1', name VARCHAR(256), UNIQUE(id));