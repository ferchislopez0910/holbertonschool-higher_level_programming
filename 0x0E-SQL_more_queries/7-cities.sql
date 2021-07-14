-- 
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `state_id` INT NOT NULL AUTO_INCREMENT,
    `name ` VARCHAR(256) NOT NULL,
    UNIQUE (id),
    PRIMARY KEY(`id`),
    FOREIGN KEY (id, states)
);
