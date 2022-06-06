# Clean Up
#DROP DATABASE natl;

# Create
CREATE DATABASE natl;
USE natl;

CREATE TABLE user (
	id int NOT NULL AUTO_INCREMENT,
    username varchar(255),
    password varchar(255),
    access_id varchar(1024),
    PRIMARY KEY (id)
);

CREATE TABLE list (
	id int NOT NULL AUTO_INCREMENT,
    user_id int,
	name varchar(255),
	description varchar(255),
    is_done boolean,
	PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE SET NULL,
);

CREATE TABLE task (
	id int NOT NULL AUTO_INCREMENT,
    list_id int,
	name varchar(255),
	description varchar(255),
    is_done boolean,
	PRIMARY KEY (id),
    FOREIGN KEY (list_id) REFERENCES list(id) ON DELETE SET NULL,
);