import sqlite3
from os.path import join, isfile

DB_PATH = 'animal.db'
SQL_PATH = 'sql'
CREATE_SQL = 'create.sql'
MIGRATION_SQL = 'migrate.sql'


# получаем SQL команды из файла
def get_sql(file):
    content = ''
    if isfile(file):
        with open(file) as f:
            content = f.read()
    return content


def main():
    # 1. создаем новые таблицы
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sql = get_sql(join(SQL_PATH, CREATE_SQL))
    cur.executescript(sql)
    # 2. переносим данные
    data_sql = get_sql(join(SQL_PATH, MIGRATION_SQL))
    cur.executescript(data_sql)

    cur.close()
    con.close()


if __name__ == '__main__':
    main()
