import sqlite3
import pandas as pd
import time
import sys
from memory_profiler import memory_usage

def connect_db():
    return sqlite3.connect('StudentDatabase.db')

def insert_student():
    start_time = time.time()
    name = input("Enter student's name: ")
    email = input("Enter student's email: ")
    age = int(input("Enter student's age: "))
    marks = int(input("Enter student's marks: "))
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (Name, Email, Age, Marks) VALUES (?, ?, ?, ?)", (name, email, age, marks))
    conn.commit()
    conn.close()
    
    end_time = time.time()
    print("Student added successfully.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Approximate memory usage: {memory_usage()[-1]:.2f} MB")

def search_edit_student():
    name = input("Enter the name of the student to search and edit: ")
    start_time = time.time()
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM students WHERE Name LIKE ?", (f'%{name}%',))
    student = cursor.fetchone()
    
    if student:
        student = list(student)
        print("Student found: ", student)
        
        new_email = input("Enter new email (leave blank to keep current): ")
        new_age = input("Enter new age (leave blank to keep current): ")
        new_marks = input("Enter new marks (leave blank to keep current): ")
        
        student[2] = new_email if new_email else student[2]
        student[3] = int(new_age) if new_age else student[3]
        student[4] = int(new_marks) if new_marks else student[4]
        
        cursor.execute("UPDATE students SET Email = ?, Age = ?, Marks = ? WHERE rowid = ?", (student[2], student[3], student[4], student[0]))
        conn.commit()
        print("Student details updated successfully.")
    else:
        print("No student found with that name.")
    conn.close()
    
    end_time = time.time()
    print(f"Time taken to find the student name: {(end_time - start_time) * 1000:.2f} milliseconds")
    print(f"Approximate memory usage: {memory_usage()[-1]:.2f} MB")

def search_export_student():
    name = input("Enter the name of the student to search and export: ")
    start_time = time.time()
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE Name LIKE ?", (f'%{name}%',))
    student = cursor.fetchone()
    conn.close()
    
    if student:
        with open(f"{student[0]}_info.txt", "w") as file:
            file.write(f"Name: {student[0]}\nEmail: {student[1]}\nAge: {student[2]}\nMarks: {student[3]}\n")
        print(f"Student info exported to {student[0]}_info.txt")
    else:
        print("No student found with that name.")
    
    end_time = time.time()
    print(f"Time taken to find the student name: {(end_time - start_time) * 1000:.2f} milliseconds")
    print(f"Approximate memory usage: {memory_usage()[-1]:.2f} MB")

def print_all_students():
    start_time = time.time()
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()
    print(df)
    df.to_excel('AllStudents.xlsx', index=False)
    print("Data exported to AllStudents.xlsx")
    
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Approximate memory usage: {memory_usage()[-1]:.2f} MB")

def main_menu():
    while True:
        print("\n1. Insert new student")
        print("2. Search and edit student details")
        print("3. Search and print the student info as .txt file")
        print("4. Print the complete file in spreadsheet format")
        print("5. EXIT")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            insert_student()
        elif choice == '2':
            search_edit_student()
        elif choice == '3':
            search_export_student()
        elif choice == '4':
            print_all_students()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
