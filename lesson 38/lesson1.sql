-- 1. Выбрать ВСЁ из таблицы MarvelCharacters
SELECT *
FROM MarvelCharacters;


-- 2. Выбрать столбцы name и align из таблицы MarvelCharacters
SELECT name, align
FROM MarvelCharacters;


-- 3. Выбрать столбцы name, year, sex, eye из таблицы MarvelCharacters с условием, что цвет глаз золотой и год появления 1976
SELECT name, year, sex, eye
FROM MarvelCharacters
WHERE eye = "Gold Eyes" AND year = 1976;


-- 4. Выбрать столбцы name, year, sex, eye из таблицы MarvelCharacters с условием, что год появления после 1989 (влючительно) и цвет глаз чёрный или голубой
SELECT 
  name,
  year,
  sex,
  eye
FROM 
  MarvelCharacters
WHERE
  year >= 1989 AND 
  (eye = "Blue Eyes" OR eye = "Black Eyes");


-- без скобок получился совсем другой запрос
-- это выборка всех строк, удовлетворяющих следующим условиям: год после 1989 с голубыми глзами или чёрные глаза вне зависимости от года
SELECT 
  name,
  year,
  sex,
  eye
FROM 
  MarvelCharacters
WHERE
  year >= 1989 AND
  eye = "Blue Eyes" OR eye = "Black Eyes";


-- 5. Логические операторы
/*
() - первый приоритет
NOT - второй приоритет
AND - третий приоритет
OR - четвертый приоритет
*/


-- 6. Вывести столбцы name, align, hair из таблицы MarvelCharacters с условием, что волосы красные, отсутсвуют или персонаж лысый
SELECT name, align, hair
FROM MarvelCharacters
WHERE hair IN ("No Hair", "Bald", "Red Hair");

-- Эта запись эквивалентна
SELECT name, align, hair
FROM MarvelCharacters
WHERE hair = "No Hair" OR hair = "Bald" OR hair = "Red Hair";


-- 7. Вывести столбцы name, hair, eye из таблицы MarvelCharacters с условием, что год появления 1991
SELECT name, hair, eye
FROM MarvelCharacters
WHERE year = 1991;
-- не обязательно выводить поле по которому мы фильтруем


-- 8. Вывести уникальные значения столбца sex
SELECT DISTINCT sex
FROM MarvelCharacters;


-- 9. Вывести столбцы name, year, align из таблицы MarvelCharacters с условием, что год появления между 1990 и 1999, а так же сортировать по году по возрастанию
-- если нам нужна сортировка по возростанию, то можно не указывать ASC
SELECT name, year, align
FROM MarvelCharacters
WHERE year >= 1990 AND year <= 1999
ORDER BY year ASC;

-- если нам нужна сортировка по убыванию, то нужно указать DESC
SELECT name, year, align
FROM MarvelCharacters
WHERE year >= 1990 and year <= 1999
ORDER BY year DESC;

-- та же выборка с сортировкой по year по убыванию и с исключением не заполненных align
SELECT
  name,
  year,
  align
FROM
  MarvelCharacters
WHERE
  year >= 1990 AND
  year <= 1999 AND
  align NOT NULL
ORDER BY 
  year DESC;

-- та же выборка с сортировкой по year по убыванию, затем по align по возростанию, затем по name по возростанию и с исключением не заполненных align
SELECT
  name,
  year,
  align
FROM
MarvelCharacters
WHERE
  year >= 1990 AND
  year <= 1999 AND
  align NOT NULL
ORDER BY 
  year DESC,
  align ASC,
  name ASC;


-- 10. Вывести 5 самых старых лысых злодеев не старее 2000 года, но пропустить первые 20 строк, а так же исключить персонажей с неуказанными глазами или с неуказанным полом
SELECT
  name,
  eye,
  sex
FROM
  MarvelCharacters
WHERE
  align = "Bad Characters" AND
  hair = "Bald" AND
  year >= 2000 AND
  sex NOT NULL AND
  eye NOT NULL
ORDER BY
  year DESC
LIMIT 5
OFFSET 20
