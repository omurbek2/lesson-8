
import sqlite3

db = sqlite3.connect('omke.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    hobby TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    birth_year INTEGER,
                    homework_score INTEGER
                )''')

students_name = [
    ('Reading', 'Luffi', 'Smithsonian', 1998, 15),
    ('Gaming', 'Sanji', 'Henderson', 1997, 8),
    ('Music', 'Sasuke', 'Pattersons', 1999, 12),
    ('football', 'Naruto', 'Kanekison', 2006, 14)
]

cursor.executemany('INSERT INTO students (hobby, first_name, last_name, birth_year, homework_score) VALUES (?, ?, ?, ?, ?)', students_name)

cursor.execute("SELECT * FROM students WHERE (last_name) > 10")
long_last_name_students = cursor.fetchall()
print("Студенты фамилией больше 10 символов:", long_last_name_students)

cursor.execute("UPDATE students SET first_name = 'genius' WHERE homework_score > 10")

cursor.execute("SELECT * FROM students WHERE first_name = 'genius'")
genius_students = cursor.fetchall()
print("Студенты с именем 'genius':", genius_students)

cursor.execute("DELETE FROM students WHERE id % 2 = 0")

a = cursor.fetchall()
for i in a:
    print(i)

db.commit()
db.close()

