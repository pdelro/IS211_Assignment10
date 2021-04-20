import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('pets.db')


    with con:
        while True:
            person_id = input('Please enter the ID number of requested Person or -1 to exit:')
            if person_id == '-1':
                sys.exit()
            elif person_id != '-1':
                con.row_factory = lite.Row
                cur = con.cursor()
                cur.execute('SELECT * FROM person where id =?', (person_id))
                row = cur.fetchall()

                print(f"{row['first_name']} {row['last_name']} is {row['age']} year old.")

            # data = cur.fetchall()

            # for row in data:



except lite.Error as e:
    print(f"Error: {e.args[0]}")
    sys.exit(1)


if __name__ == "__main__":
    pass
