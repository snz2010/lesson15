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

-- заполняем основную таблицу
INSERT INTO new_animals ( animal_id, out_age, name, birth, out_month, out_year,
type_id, breed_id, color1_id, color2_id, program_id, condition_id )
SELECT animal_id, age_upon_outcome, animals.name, date_of_birth, outcome_month, outcome_year,
animal_type.id as type_id,
animal_breed.id as breed_id,
color1.id as color1_id,
color2.id as color2_id,
out_program.id as program_id,
out_condition.id as condition_id
FROM animals
LEFT JOIN animal_type
    ON animal_type.a_type = animals.animal_type
LEFT JOIN animal_breed
    ON animal_breed.breed = animals.breed
LEFT JOIN animal_color as color1
    ON color1.color = animals.color1
LEFT JOIN animal_color as color2
    ON color2.color = animals.color2
LEFT JOIN out_program
    ON out_program.program = animals.outcome_subtype
LEFT JOIN out_condition
    ON out_condition.condition = animals.outcome_type;






