GET_ANIMAL_BY_ID = """
    SELECT * from new_animals
    WHERE animal_id = :1
"""
GET_ANIMAL_BY_ID_FULL = """
    SELECT
         new_animals.animal_id, 
         new_animals.out_age, 
         new_animals.name,
         new_animals.birth,
         new_animals.out_month, 
         new_animals.out_year,
         animal_type.a_type as 'type',
         animal_breed.breed as 'breed',
         animal_color1.color as 'color1',
         animal_color2.color as 'color2',
         out_program.program as 'program',
         out_condition.condition as 'condition'
    FROM new_animals
    LEFT JOIN animal_type
    ON animal_type.id = new_animals.type_id
    LEFT JOIN animal_breed
    ON animal_breed.id = new_animals.breed_id
    LEFT JOIN animal_color as animal_color1
    ON animal_color1.id = new_animals.color1_id
    LEFT JOIN animal_color as animal_color2
    ON animal_color2.id = new_animals.color2_id
    LEFT JOIN out_program
    ON out_program.id = new_animals.program_id
    LEFT JOIN out_condition
    ON out_condition.id = new_animals.condition_id
     
    WHERE new_animals.animal_id = :1
"""
