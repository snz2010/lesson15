-- заполняем таблицу типов животных
INSERT INTO animal_type (a_type)
SELECT DISTINCT animal_type FROM animals;

-- заполняем таблицу пород
INSERT INTO animal_breed (breed)
SELECT DISTINCT breed FROM animals;

-- заполняем таблицу цветов
INSERT INTO animal_color (color)
SELECT DISTINCT TRIM(color1) as color FROM animals
UNION
SELECT DISTINCT TRIM(color2) as color FROM animals WHERE color2 IS NOT NULL;

-- заполняем таблицу программы помощи животным
INSERT INTO out_program (program)
SELECT DISTINCT outcome_subtype FROM animals WHERE outcome_subtype is not NULL;

-- заполняем таблицу состояния
INSERT INTO out_condition (condition)
SELECT DISTINCT outcome_type FROM animals WHERE outcome_type is not NULL;







