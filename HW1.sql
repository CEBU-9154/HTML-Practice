CREATE TABLE student (
SNO TEXT PRIMARY KEY,
SNAME TEXT,
STATUS INTEGER,
CITY TEXT);

INSERT INTO student (SNO,SNAME,STATUS,CITY) VALUES
    ('S1','Smith',20,'London'),
    ('S2','Jones',10,'Paris'),
    ('S3','Blake',30,'Paris');

SELECT * FROM student WHERE STATUS > 15;