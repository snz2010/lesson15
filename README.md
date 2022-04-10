## Домашняя работа по уроку 15


### Миграция данных (файл migrate.py) из таблицы "animals" в таблицу "new_animals":


    * 1. Создаем подключение к БД с помощью метода sqlite3.connect

    * 2. Проектируем новую, приведенную к нормальной форме базу данных (таблица "new_animals" и 5 вспомогательных таблиц)

    * 3. Пишем SQL-запросы для её создания (файл create.sql)

    * 4. ПЕРЕНОСИМ данные в новые таблицы:

	* 4.1 migrate.sql, fill_5_tables.sql - файлы для заполнения связанных таблиц

	* 4.2 migrate.py, fill_main_table.sql - файлы заполнения основной таблицы "new_animals"

    * 4. Приложение Flask по запросу /<itemid> (например /2) вернёт информацию об одном объекте

    * 5. Приложение Flask по запросу /<itemid>/full (например /2) вернёт информацию в расширенном виде


query.py - файл для SQL-запросов С ПАРАМЕТРАМИ к БД для выдачи во вьюшку 2х вариантов - полного(GET_ANIMAL_BY_ID_FULL) и нет(GET_ANIMAL_BY_ID) 

delete_all_tables.sql - файл для чистки новых таблиц


