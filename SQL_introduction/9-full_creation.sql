-- Script that creates a table second_table in the database hbtn_0c_0 and add multiples rows
-- second_table description: id INT, name VARCHAR(256), score INT
-- If the table second_table already exists, your script should not fail
-- Creates records: id=1,name="John",score=10; id=2,name="Alex",score=3; id=3,name="Bob",score=14; id=4,name="George",score=8
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
