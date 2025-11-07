CREATE TABLE files (
    id INT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    directory VARCHAR(255) NOT NULL
);
INSERT INTO files (filename, directory) VALUES ('file1.txt', 'directory1');
INSERT INTO files (filename, directory) VALUES ('file2.txt', 'directory2');
INSERT INTO files (filename, directory) VALUES ('file3.txt', 'directory3');
SELECT * FROM files;