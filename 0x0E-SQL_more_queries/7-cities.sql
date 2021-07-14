-- 
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    PRIMARY KEY(`id`),
    `id` INT NOT NULL AUTO_INCREMENT,
    `state_id` INT NOT NULL AUTO_INCREMENT,
    `state_id` VARCHAR(256) NOT NULL,
    FOREIGN KEY (id, states)
);
