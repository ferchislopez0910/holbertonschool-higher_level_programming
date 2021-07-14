-- Write a script that creates the table force_name on your MySQL server.
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) IS NOT null);
INSERT INTO force_name (id, name) VALUES (89, 'Holberton School');