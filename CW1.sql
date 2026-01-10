CREATE TABLE supplier (
SNO TEXT PRIMARY KEY,
SNAME TEXT,
STATUS INTEGER,
CITY TEXT);

INSERT INTO supplier (SNO,SNAME,STATUS,CITY) VALUES
    ('S1','Smith',20,'London'),
    ('S2','Jones',10,'Paris'),
    ('S3','Blake',30,'Paris');

SELECT * FROM supplier;