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
--7. Найти имена персонажей, имя которых начинается на "Phoenix"
SELECT name
FROM MarvelCharacters
WHERE name LIKE "Phoenix%";


--ПРАКТИКА
--8. Сделать выборку персонажей (имя, год, количество появлений), где год между 1960 и 1970, и количество появлений больше 10
SELECT 
    name,
    year,
    appearances
FROM
    MarvelCharacters
WHERE
    year BETWEEN 1960 AND 1970 AND
    appearances > 10 AND
    appearances NOT NULL
ORDER BY
    appearances;


--ПРАКТИКА
--9. Найдите персонажей, в имени которых есть "captain" и которые появлялись больше 10 раз
SELECT 
    name,
    year,
    appearances
FROM
    MarvelCharacters
WHERE
    name LIKE "%captain%" AND
    appearances > 10 AND
    appearances NOT NULL
ORDER BY
    appearances;


--10. Выведите пол и количество персонажей
SELECT 
    sex AS пол,
    COUNT(*) AS количество_персонажей
FROM
    MarvelCharacters
WHERE
    пол NOT NULL
GROUP BY
    пол;


--11. Выведите год и количество персонажей
SELECT 
    sex AS пол,
    COUNT(*) AS количество_персонажей
FROM
    MarvelCharacters
WHERE
    пол NOT NULL
GROUP BY
    пол;


--12. Выведите год и количество с количеством появлений больше 350
SELECT 
    year AS год,
    COUNT(*) AS количество_персонажей
FROM
    MarvelCharacters
WHERE
    год NOT NULL
GROUP BY
    год
HAVING
    количество_персонажей > 350
ORDER BY
    год


--13. Выведите цвет глаз и количество персонажей с цветными глазными яблоками
SELECT 
    eye AS цвет_глаз,
    COUNT(*) AS количество_персонажей
FROM
    MarvelCharacters
WHERE
    eye LIKE "%eyeballs%"
GROUP BY
    eye
ORDER BY
    COUNT(*) DESC;


--14. Выведите цвет глаз и количество появлений персонажей
SELECT 
    eye AS цвет_глаз,
    SUM(appearances) AS количество_появлений
FROM
    MarvelCharacters
WHERE
    eye NOT NULL
GROUP BY
    eye
ORDER BY
    SUM(appearances) DESC


--15. Выведите год и количество появлений персонажей, количество персонажей и среднее количество появлений (с округлением до 2 знака после запятой) по годам
SELECT 
    year AS год,
    SUM(appearances) AS количество_появлений,
    COUNT(appearances) AS количество_персонажей,
    ROUND(AVG(appearances), 2) AS среднее_количество_персонажей
FROM
    MarvelCharacters
WHERE
    year NOT NULL
GROUP BY
    year
ORDER BY
    year


--16. Выведите год и количество появлений персонажей, где количество появлений максимальное
SELECT 
    year AS год,
    name AS имя,
    MAX(appearances) AS количество_появлений
FROM
    MarvelCharacters
WHERE
    year NOT NULL
GROUP BY
    year
ORDER BY
    year


--ПРАКТИКА
--17. Сгруппировать персонажей по годам, получить минимальное количество и имя персонажа. Выбрать имя, год, минимальное количество появлений
--18. Сгруппировать пероснажей по годам, получить максимальное колчество и имя персонажа. Выбрать имя, год, максимальное количество появлений. Количество появлений 50 и больше
