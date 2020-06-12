INSERT INTO dogs
    (name,age,breed)
VALUES('Maggie', 4, 'Terrier');

INSERT INTO dogs
    (name,age,breed)
VALUES('River', 7, 'Husky');

INSERT INTO dogs
    (name,age,breed)
VALUES('Archer', 8, 'Pitbull');

INSERT INTO dogs
    (name,age,breed)
VALUES('Ram', 2, 'Pug');

-- When we say 'SELECT *', it basically means to select all the Columns, instead of all the rows 
-- Sqlite allows us to select particular columns with the help of following Syntax:
-- 'SELECT <column_name> FROM <table_name>' or 'SELECT <col1_name>, <col2_name> FROM <table_name>'

-- We can also select based on certain conditions with the help of following syntax:
-- 'SELECT * FROM dogs WHERE name IS "Piggy";'
-- 'SELECT * FROM dogs WHERE breed IS "Husky";'
-- 'SELECT * FROM dogs WHERE breed IS NOT "Chihuahua";'
-- 'SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND breed IS NOT "Pug";'

-- We can also select things based on if they have certain characters or not, using the syntax:
-- 'SELECT * FROM dogs WHERE name LIKE "%gg%";'
-- The above code will select all the dogs, in whose name there are 2 consecutive G(s)
-- '%' stands for the rest of characters
-- If we just use ... LIKE "gg", then it will select the dogs whose names are "gg"