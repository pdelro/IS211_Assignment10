import sqlite3 as lite
import sys


def query_pets():
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
                person_data = cur.fetchone()

                first_name = person_data['first_name']
                last_name = person_data['last_name']
                age = person_data['age']

                print('{} {} is {} years old.'.format (first_name, last_name, age))

                cur.execute('''
                SELECT * 
                FROM pet
                INNER JOIN person_pet ON pet.id = person_pet.pet_id
                INNER JOIN person ON person_pet.person_id = person.id
                WHERE person_id =?
                ''', (person_id,))

                pet_data = cur.fetchall()

                for info in pet_data:
                    pet_name = info[1]
                    pet_breed = info[2]
                    pet_age = info[3]
                    dead = (info[4])
                    if dead == 1:
                        print('{} {} owned {}, a {}, who was {} years old.'.format(first_name, last_name, pet_name, pet_breed, pet_age))
                    else:
                        print('{} {} owns {}, a {}, who is {} years old.'.format(first_name, last_name, pet_name, pet_breed, pet_age))

    except lite.Error as e:
        print(f"Error: {e.args[0]}")
        sys.exit(1)


if __name__ == "__main__":
    query_pets()
