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
            else:
                try:
                    person_id = int(person_id)
                except:
                    print('Invalid input. Please enter valid ID."')
                    continue

            con.row_factory = lite.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM person WHERE person.id =?',(person_id,))
            person_data = cur.fetchall()

            print(f"{person_data['first_name']} {person_data['last_name']} is {person_data['age']} year old.")

            # data = cur.fetchall()

            # for row in data:



except lite.Error as e:
    print(f"Error: {e.args[0]}")
    sys.exit(1)


if __name__ == "__main__":
    pass
