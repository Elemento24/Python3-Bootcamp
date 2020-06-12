INSERT INTO dogs
    (name,age,breed)
VALUES('Champ', 4, 'Husky');

INSERT INTO dogs
    (name,age,breed)
VALUES('Rose', 1, 'Chihuahua');

INSERT INTO dogs
    (name,age,breed)
VALUES('Moose', 3, 'Lab');

INSERT INTO dogs
    (name,age,breed)
VALUES('Piggy', 6, 'Corgi');

--  We can insert data into a DB, using a file
--  We just write the insert statements inside a file
--  And then we use the command 'sqlite3 <file_name>.db', which opens up the SQL shell ...
--  ... and connect to the Database file
--  After that, we use '.read <file_name>.sql' inside the SQLITE shell
--  It executes the file, and stores the data inside our DB file
--  To see if the data is stored inside the DB file or not, we can use the command ...
--  ... 'SELECT * FROM <tabel_name>;', which shows us all the data, that we store inside the DB