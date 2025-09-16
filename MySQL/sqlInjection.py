import mysql.connector


def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rolls@mysql",
            database = 'schoolProject'
        )
        if conn.is_connected():
            print("Connected ✅")
            return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    

connection = get_connection()
cur = connection.cursor()

name = input('Enter the name >>>> ')
sql = f"SELECT * FROM students WHERE name = '{name}'"
cur.execute(sql)
for row in cur.fetchall():
    print(row)

cur.close()
connection.close()