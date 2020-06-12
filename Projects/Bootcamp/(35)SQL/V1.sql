CREATE TABLE dogs
(
    name TEXT,
    breed TEXT,
    age INTEGER
);

-- It is conventional to write the syntax of sqlite in UPPERCASE, just to differentiate it

-- This is how we define an empty table in sqlite3, we have to write 'CREATE TABLE', followed ...
-- by the name of the table, that we want to have
-- Then we need to pass a list of all the columns, that we want to have in our table
-- We also need to define the type of data that we will be storing inside our columns

-- For storing our data inside a file, either we can use '.open <file_name>.db' in our shell
-- It will create a file for us and will store the data inside it
-- Or we can use the command 'sqlite3 <file_name>.db', which will do the same thing

-- Storing the data inside a file, makes sure that we don't lose our data, once we close the shell