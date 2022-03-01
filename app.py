from flask import Flask, jsonify
import sqlite3
import query

app = Flask(__name__)

DB_PATH = 'animal.db'


def serial_row(row: sqlite3.Row):
    return {key: row[key] for key in row.keys()}


# выдаем по запросу содержимое таблицы new_animals для определенного animal_id
@app.route('/<animal_id>')
def get_by_id(animal_id):
    conn: sqlite3.Connection = app.config['db']
    cur = conn.cursor()
    cur.execute(query.GET_ANIMAL_BY_ID, (animal_id,))  # передаем параметр в запрос
    row = cur.fetchone()
    cur.close()
    return jsonify(serial_row(row))


# выдаем по запросу развернутое содержимое таблицы
@app.route('/<animal_id>/full')
def full_by_id(animal_id):
    conn: sqlite3.Connection = app.config['db']
    cur = conn.cursor()
    cur.execute(query.GET_ANIMAL_BY_ID_FULL, (animal_id,))  # передаем параметр в запрос
    row = cur.fetchone()
    cur.close()
    return jsonify(serial_row(row))


if __name__ == '__main__':
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.row_factory = sqlite3.Row  # ??
    app.config['db'] = con
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        con.close()
