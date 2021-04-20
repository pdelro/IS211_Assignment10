import sqlite3 as lite
import sys

people_data = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

pet_data = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

person_pet_data = [
    (1,1),
    (1,2),
    (2,3),
    (2,4),
    (3,5),
    (4,6)
]


if __name__ == "__main__":
    try:
        con = lite.connect('pets.db')

        with con:
            cur = con.cursor()

            cur.execute('DROP TABLE IF EXISTS person')
            cur.execute('CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)')
            cur.executemany('INSERT INTO person VALUES(?, ?, ?, ?)', people_data)
            cur.execute('DROP TABLE IF EXISTS pet')
            cur.execute('CREATE TABLE pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)')
            cur.execute('DROP TABLE IF EXISTS person_pet')
            cur.executemany('INSERT INTO person VALUES(?, ?, ?, ?, ?)', pet_data)
            cur.execute('CREATE TABLE person_pet(person_id INTEGER, pet_id)')
            cur.executemany('INSERT INTO person VALUES(?, ?)', person_pet_data)

    except lite.Error as e:
        print(f"Error: {e.args[0]}")
        sys.exit(1)

    finally:
        if con:
            con.close()