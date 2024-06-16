-- 1. Создайте новую таблицу FemaleMarvelCharacters,
-- содержащую только женских персонажей.
CREATE TABLE FemaleMarvelCharacters AS
SELECT *
FROM MarvelCharacters
WHERE sex = 'Female Characters';

-- 2. Создайте новую таблицу CharactersByYear, 
-- содержащую количество персонажей, появившихся в каждом году.
CREATE TABLE CharactersByYear AS
SELECT year, COUNT(*) as count
FROM MarvelCharacters
GROUP BY year;

-- 3. Создайте таблицу MaleFemaleMarvelCharactersByEyeAndHair,
-- которая содержит количество мужских и женских персонажей 
-- Marvel для каждой комбинации цвета волос и глаз, 
-- отсортированное по убыванию количества персонажей для каждого пола.
-- Исключите из результатов персонажей, у которых не указаны цвет волос или глаз.
CREATE TABLE MaleFemaleMarvelCharactersByEyeAndHair AS
SELECT
	sex,
	eye,
	hair,
	COUNT(*) AS cnt
FROM
	MarvelCharacters
WHERE
	eye IS NOT NULL AND 
	hair IS NOT NULL AND
--	sex IN ('Male Characters', 'Female Characters')
	sex LIKE '%male%'
GROUP BY
	sex,
	eye,
	hair
ORDER BY
	sex,
	cnt DESC;

SELECT DISTINCT identify FROM MarvelCharacters;

SELECT COUNT(*) FROM MarvelCharacters;

UPDATE MarvelCharacters
SET identify = 'Secret identity'
WHERE identify = 'Secret Identity';

--Secret Identity: id 1
--Public Identity: id 2
--No Dual Identity: id 3
--Known to Authorities Identity: id 4

SELECT DISTINCT align FROM MarvelCharacters;
SELECT DISTINCT eye FROM MarvelCharacters;
SELECT DISTINCT hair FROM MarvelCharacters;
SELECT DISTINCT sex FROM MarvelCharacters;
SELECT DISTINCT gsm FROM MarvelCharacters;
SELECT DISTINCT alive FROM MarvelCharacters;


CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    class TEXT  -- учебная группа
);


INSERT INTO Students (name, age, class)
VALUES
    ('Мария', 23, 'Python 316'),
    ('Анна', 32, 'Python316'),
    ('Елена', 32, 'PYTHON316'),
    ('Макс', 32, 'PYTHON 316'),
    ('Роман', 35, 'Python 319'),
    ('Андрей', 35, 'Python 319'),
    ('Василий', 35, 'Python 319');


CREATE TABLE Classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name
);

CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    class_id INTEGER,  -- id учебной группы
    
    FOREIGN KEY (class_id) REFERENCES Classes(id)  -- поле class_id таблицы Students связывается с полем id таблицы Classes
);

INSERT INTO Classes (name)
VALUES
    ('Python 316'),
    ('Python 319'),
    ('Python 322'),
    ('QA 314');

INSERT INTO Students (name, age, class_id)
VALUES
    ('Мария', 23, 1),
    ('Анна', 32, 1),
    ('Елена', 32, 1),
    ('Макс', 32, 1),
    ('Роман', 35, 2),
    ('Андрей', 35, 2),
    ('Василий', 35, 3);
    

SELECT
    s.name,
    s.age,
    c.name
FROM
    Students AS s
        JOIN Classes AS c ON s.class_id = c.id;


SELECT
    s.name AS student_name,
    s.age AS age,
    c.name AS class
FROM
    Students AS s
        INNER JOIN Classes AS c ON s.class_id = c.id;
    

SELECT
    s.name AS student_name,
    s.age AS age,
    c.name AS class
FROM
    Classes AS c
        INNER JOIN Students AS s ON c.id = s.class_id;


INSERT INTO Students (name, age)
VALUES
    ('Виталий', 73),
    ('Эдуард', 27),
    ('Катерина', 34);

INSERT INTO Classes (name)
VALUES (NULL);


SELECT
    c.name AS class,
    s.name AS student_name,
    s.age AS age
FROM
    Students AS s
        LEFT JOIN Classes AS c ON s.class_id = c.id;


SELECT
    c.name AS class,
    s.name AS student_name,
    s.age AS age
FROM
    Students AS s
        RIGHT JOIN Classes AS c ON s.class_id = c.id;


SELECT
    c.name AS class,
    s.name AS student_name,
    s.age AS age
FROM
    Classes AS c
        LEFT JOIN Students AS s ON c.id = s.class_id;


SELECT
    c.name AS class,
    s.name AS student_name,
    s.age AS age
FROM
    Classes AS c
        FULL JOIN Students AS s ON c.id = s.class_id;
        
        
SELECT
    c.name AS class,
    s.name AS student_name
FROM
    Classes AS c
        CROSS JOIN Students AS s
WHERE
    s.name IS NOT NULL AND
    c.name IS NOT NULL
                

SELECT
    c.name AS class,
    s.name AS student_name
FROM
    Classes AS c
        CROSS JOIN Students AS s
WHERE
    s.name IS NOT NULL AND
    c.name IS NOT NULL;


-- Виды JOIN
-- INNER JOIN - возвращает строки, которые есть в обеих таблицах
-- Он же - JOIN

-- LEFT JOIN - возвращает все строки из левой таблицы и соответствующие строки из правой
-- RIGHT JOIN - возвращает все строки из правой таблицы и соответствующие строки из левой
-- FULL JOIN - возвращает все строки из обеих таблиц

