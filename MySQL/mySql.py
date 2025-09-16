import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rolls@mysql"
        )
        if conn.is_connected():
            print("Connected ✅")
            return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

connection = get_connection()
cur = connection.cursor()
cur.execute('USE schoolProject')
cur.execute('CREATE DATABASE IF NOT EXISTS schoolProject')
print('Created successfully')


cur.execute('''
CREATE TABLE IF NOT EXISTS students(
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    class VARCHAR(10),
    marks INT
)
''')
students_data = [
    (1, "Amit Kumar", "12A", 87),
    (2, "Priya Sharma", "12B", 92),
    (3, "Rohit Verma", "11A", 76),
    (4, "Sneha Gupta", "10C", 81),
    (5, "", "12A", 95),
    (6, "Anjali Mehta", "11B", 68),
    (7, "Rahul Yadav", "10A", 73),
    (8, "Neha Chauhan", "12C", 89),
    (9, "Arjun Kapoor", "11A", 54),
    (10, "Simran Kaur", "12B", 99)
]

cur.executemany(
    "INSERT INTO students (roll_no, name, class, marks) VALUES (%s, %s, %s, %s)",
    students_data
)

connection.commit()
name = input("Enter student name: ")  
cur.execute(f"SELECT * FROM students WHERE name =%s ",(name,))
for row in cur.fetchall():
    print(row)

print("✅ Dummy data inserted successfully!")
connection.close()
