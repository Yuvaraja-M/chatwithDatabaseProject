import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
connection = sqlite3.connect("student.db")

cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    class TEXT,
    section TEXT,
    marks INTEGER
)
""")

# Insert 5 random students
students = [
    ("Arjun", "10", "A", 88),
    ("Sneha", "9", "B", 92),
    ("Rahul", "10", "C", 75),
    ("Meera", "8", "A", 81),
    ("Vikram", "9", "C", 95)
]

cursor.executemany("INSERT INTO students (name, class, section, marks) VALUES (?, ?, ?, ?)", students)

# Commit and close connection
connection.commit()
connection.close()

print("student.db created successfully with 5 students!")
