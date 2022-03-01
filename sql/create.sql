-- запросы на создание связанных таблиц
CREATE TABLE IF NOT EXISTS animal_type (
id integer PRIMARY KEY autoincrement,
-- тип животного
a_type VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS animal_breed (
id integer PRIMARY KEY autoincrement,
-- порода
breed VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS animal_color (
id integer PRIMARY KEY autoincrement,
-- цвет окраса
color VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS out_program (
id integer PRIMARY KEY autoincrement,
-- в какой программе участвует
program VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS out_condition (
id integer PRIMARY KEY autoincrement,
-- в каком состоянии находится
condition VARCHAR(255) NOT NULL
);

-- запрос на создание основной таблицы
CREATE TABLE if not EXISTS new_animals (
-- статичные данные - в самой таблице
id INTEGER PRIMARY KEY AUTOINCREMENT,
animal_id VARCHAR(10) not NULL,
out_age VARCHAR(25) not NULL,
name VARCHAR(255),
birth TEXT NOT NULL,
out_month integer NOT NULL,
out_year integer NOT NULL,
-- данные из связанных таблиц
type_id integer NOT NULL,
breed_id integer NOT NULL,
color1_id integer,
color2_id integer,
program_id integer,
condition_id integer,
-- настройка связей
FOREIGN KEY (type_id) REFERENCES animal_type(id),
FOREIGN KEY (breed_id) REFERENCES animal_breed(id),
FOREIGN KEY (color1_id) REFERENCES animal_color(id),
FOREIGN KEY (color2_id) REFERENCES animal_color(id),
FOREIGN KEY (program_id) REFERENCES out_program(id),
FOREIGN KEY (condition_id) REFERENCES out_condition(id)
)
