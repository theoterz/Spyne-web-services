CREATE TABLE users (
id BIGSERIAL NOT NULL PRIMARY KEY,
username VARCHAR(50) NOT NULL,
password VARCHAR(50) NOT NULL,
balance DECIMAL NOT NULL);

INSERT INTO users(username, password, balance)
VALUES ('user1', 'user1', 50.0);

INSERT INTO users(username, password, balance)
VALUES ('user2', 'user2', 150.0);

INSERT INTO users(username, password, balance)
VALUES ('user3', 'user3', 75.0);

INSERT INTO users(username, password, balance)
VALUES ('user4', 'user4', 225.75);