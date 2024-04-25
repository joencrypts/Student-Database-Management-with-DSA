# Student-Database-Management-with-DSA
The Student Database Management System (SDMS) is a Python program for managing student records. It offers functions to insert, search, edit, export, and print student data, providing a user-friendly solution for educational institutions.
This Python program allows users to manage a student database, including inserting new students, searching for students, editing student details, exporting student information, and printing the database in spreadsheet format.

edit the variables in fakke.py to create a fake list of db with random names,email and marks.

## Getting Started

### Prerequisites

- Python 3
- SQLite3
- pandas
- faker (for generating dummy data)
- memory-profiler (for measuring memory usage)

### Installing Dependencies

```bash
pip install pandas memory-profiler faker

```Database Setup

    Ensure you have SQLite3 installed.
    Run the following command to create the database file (StudentDatabase.db) and the students table:

sqlite3 StudentDatabase.db
CREATE TABLE students (
    Name TEXT,
    Email TEXT,
    Age INTEGER,
    Marks INTEGER
);

Usage

    Run the Student.py file to start the program.
    Follow the on-screen instructions to perform various operations on the student database.

Features

    Insert New Student: Add a new student to the database.
    Search and Edit Student Details: Find a student by name and edit their email, age, and marks.
    Search and Export Student Information: Find a student by name and export their details to a text file.
    Print the Database in Spreadsheet Format: Export the entire database to an Excel spreadsheet.
