--
-- File generated with SQLiteStudio v3.1.1 on Sat Jun 16 12:20:55 2018
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: book
CREATE TABLE book (BookID INTEGER PRIMARY KEY, Title CHAR, Author CHAR, Price DECIMAL);
INSERT INTO book (BookID, Title, Author, Price) VALUES (1, 'Code', ' Charles Petzold', 290);
INSERT INTO book (BookID, Title, Author, Price) VALUES (2, 'Algorithms', ' Robert Sedgewick', 350);
INSERT INTO book (BookID, Title, Author, Price) VALUES (3, 'Think python', 'Allen B.Drowney', 475);
INSERT INTO book (BookID, Title, Author, Price) VALUES (4, 'The Society of Mind', ' Marvin Minsky', 380);
INSERT INTO book (BookID, Title, Author, Price) VALUES (5, 'Hacker''s Delight', ' Henry S. Warren Jr.', 235);
INSERT INTO book (BookID, Title, Author, Price) VALUES (6, 'Programming Pearls', ' Jon L. Bentley', 410);
INSERT INTO book (BookID, Title, Author, Price) VALUES (8, 'Reviewing C++', ' Alex Maureau', 280);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
