import sqlite3
from faker import Faker
import random

def connect_db():
    return sqlite3.connect('StudentDatabase.db')

def create_students_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            Name TEXT,
            Email TEXT,
            Age INTEGER,
            Marks INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def generate_student_data(num_students=158725):
    fake = Faker()
    students = []
    for _ in range(num_students):
        name = fake.name()
        email = fake.email()
        age = random.randint(18, 22)  # Assuming age range for college students
        marks = random.randint(40, 100)
        students.append((name, email, age, marks))
    return students

def insert_dummy_data():
    students = generate_student_data()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO students (Name, Email, Age, Marks) VALUES (?, ?, ?, ?)", students)
    conn.commit()
    conn.close()
    print(f"{len(students)} students added to the database successfully.")

def main():
    create_students_table()  # Ensure the table exists
    insert_dummy_data()      # Insert dummy data into the table

if __name__ == "__main__":
    main()
