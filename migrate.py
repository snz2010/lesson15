import sqlite3
from os.path import join, isfile

DB_PATH = 'animal.db'
SQL_PATH = 'sql'
CREATE_SQL = 'create.sql'
MIGRATION_SQL = 'migrate.sql'
MIGRATION_MAIN_SQL = 'fill_new.sql'


# получаем SQL команды из файла
def get_sql(file):
    content = ''
    if isfile(file):
        with open(file) as f:
            content = f.read()
    return content


# получаем идентификатор типа животного
def get_type_id(bid):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    query = f"SELECT `id` FROM animal_type WHERE a_type LIKE '%{bid}%'"
    cur.execute(query)
    id = cur.fetchone()[0]
    cur.close()
    con.close()
    return id


# получаем идентификатор породы животного
def get_breed_id(bid):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    query = f"SELECT `id` FROM animal_breed WHERE breed LIKE '%{bid}%'"
    cur.execute(query)
    id = cur.fetchone()[0]
    cur.close()
    con.close()
    return id


# получаем идентификатор окраса животного
def get_color_id(color):
    if color is None:
        return 0
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    query = f"SELECT `id` FROM animal_color WHERE color LIKE '%{color}%'"
    cur.execute(query)
    id = cur.fetchone()[0]
    cur.close()
    con.close()
    return id


# получаем идентификатор программы животного
def get_program_id(p):
    if p is None:
        return 0
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    query = f"SELECT `id` FROM out_program WHERE program LIKE '%{p}%'"
    cur.execute(query)
    id = cur.fetchone()[0]
    cur.close()
    con.close()
    return id


# получаем идентификатор состояния животного
def get_condition_id(сdit):
    if сdit is None:
        return 0
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    query = f"SELECT `id` FROM out_condition WHERE condition LIKE '%{сdit}%'"
    cur.execute(query)
    id = cur.fetchone()[0]
    cur.close()
    con.close()
    return id


# заполнение словаря данными из записи таблицы
def get_animal_data(tu_from_table, data):
    data["animal_id"] = tu_from_table[0]
    data["out_age"] = tu_from_table[1]
    data["name"] = tu_from_table[2]
    data["birth"] = tu_from_table[3]
    data["out_month"] = tu_from_table[4]
    data["out_year"] = tu_from_table[5]
    data["type_id"] = get_type_id(tu_from_table[6])
    data["breed_id"] = get_breed_id(tu_from_table[7])
    data["color1_id"] = get_color_id(tu_from_table[8])
    data["color2_id"] = get_color_id(tu_from_table[9])
    data["program_id"] = get_program_id(tu_from_table[10])
    data["condition_id"] = get_condition_id(tu_from_table[11])


# запись строчки данных в БД
def insert_str_in_db(d, counter):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO new_animals VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (counter, d["animal_id"], d["out_age"], d["name"], d["birth"], d["out_month"], d["out_year"], d["type_id"], d["breed_id"], d["color1_id"], d["color2_id"], d["program_id"], d["condition_id"]))
    # если в базе не стоит автокоммит ...
    con.commit()
    cur.close()
    con.close()


def main():
    # 1. Создаем подключение к БД
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    # 2. Cоздаем новые таблицы
    sql = get_sql(join(SQL_PATH, CREATE_SQL))  # файл с запросами на создание связанных таблиц
    cur.executescript(sql)
    # 2.1 переносим данные в зависимые таблицы
    # data_sql = get_sql(join(SQL_PATH, MIGRATION_SQL))  # файл с запросами на заполнение связанных таблиц
    # cur.executescript(data_sql)
    # 2.2 ВАРИАНТ ПОСТРОЧНОГО ЗАПОЛНЕНИЯ ТАБЛИЦЫ ЦВЕТОВ
    # получим цвета из исходной таблицы - заполняем таблицу цветов
    # cur.executescript("""INSERT INTO animal_color (color)
    # SELECT DISTINCT TRIM(color1) as color FROM animals
    # UNION SELECT DISTINCT TRIM(color2) as color FROM animals WHERE color2 IS NOT NULL;
    # """)
    # что получилось?
    # cur.execute("SELECT * FROM animal_color")
    # rows = cur.fetchall()
    # print(rows)
    # 3. заполняем основную таблицу # ВАРИАНТ 2: - построчное заполнение
    cur.execute("SELECT animal_id, age_upon_outcome, name, date_of_birth, outcome_month, outcome_year, animal_type, breed, trim(color1), trim(color2), outcome_subtype, outcome_type FROM animals")
    rows = cur.fetchall()
    counter = 0
    for row in rows:
        animal_data = {}
        get_animal_data(row, animal_data)
        insert_str_in_db(animal_data, counter)
        counter += 1
    print(f"в новую таблицу перенесено {counter} строк")
    # 3.1
    # data_sql = get_sql(join(SQL_PATH, MIGRATION_MAIN_SQL))  # ВАРИАНТ 1: файл с запросом на заполнение осн. таблицы
    # cur.executescript(data_sql) # при такой форме заполнения (была в разборе ДЗ) - цвета заполняются некорректно!

    # закрываем
    cur.close()
    con.close()


if __name__ == '__main__':
    main()
