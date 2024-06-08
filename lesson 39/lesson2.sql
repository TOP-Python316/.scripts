-- Повторили:

-- SELECT
-- FROM
-- WHERE
-- ORDER BY
-- DESC
-- ASC
/*
() - первый приоритет
NOT - второй приоритет
AND - третий приоритет
OR - четвертый приоритет
*/
-- IN
-- LIMIT
-- OFFSET

-- CREATE TABLE MarvelCharacters (
--     id               INTEGER PRIMARY KEY AUTOINCREMENT,
--     page_id          INTEGER,
--     name             TEXT,
--     urlslug          TEXT,
--     identify         TEXT,
--     ALIGN            TEXT,
--     EYE              TEXT,
--     HAIR             TEXT,
--     SEX              TEXT,
--     GSM              TEXT,
--     ALIVE            TEXT,
--     APPEARANCES      INTEGER,
--     FIRST_APPEARANCE TEXT,
--     Year             INTEGER
-- );


-- 1. Вывести имя, год появления и количество появлений персонажах в период с 1940 по 1950 годах, число появлений которых больше 5, отсортированных по году и количеству появлений
SELECT
    name,
    year,
    appearances
FROM
    MarvelCharacters
WHERE 
    (year BETWEEN 1940 AND 1950) AND
    appearances NOT NULL AND
    appearances > 5
ORDER BY
    year,
    appearances DESC;


--2. Вывести имя и год появления персонажей, начинающихся на А
-- % означает любое количество любых символов
-- _ означает один любой символ
SELECT name, year
FROM MarvelCharacters
WHERE name LIKE "A%";


--3. Вывести имя и год появления персонажей, оканчивающихся на "Earth-616" и имеющих в имени три символа
SELECT name, year
FROM MarvelCharacters
WHERE name LIKE "___ (Earth-616)";


--4. Вывести имя и год появления персонажей, имеющих в имени "Earth", но при этом не "Earth-616"
SELECT 
    name,
    year
FROM
    MarvelCharacters
WHERE
    name LIKE "%(Earth%)" AND
    name NOT LIKE "%(Earth-616)";


--5. Вывести имя и год появления персонажей, начинающихся на "A" с произвольным количеством символов, пробелом, а затем снова "A" с произвольным количеством символов.
SELECT 
    name,
    year
FROM
    MarvelCharacters
WHERE
    name LIKE "A% A%";


--6. Вывести имя и год появления персонажей, начинающихся на "SpIdeR", при этом ищется в любом регистре
SELECT 
    name,
    year
FROM
    MarvelCharacters
WHERE
    name LIKE "SpIdeR%";


--ПРАКТИКА
--1. Найти имена персонажей, имя которых начинается на "Phoenix"
--2. Сделать выборку персонажей (имя, год, количество появлений), где год между 1960 и 1970, и количество появлений больше 10
--3. Найдите персонажей, в имени которых есть "captain" и которые появлялись больше 10 раз