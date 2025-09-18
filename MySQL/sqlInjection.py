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

# name = input('Enter the name >>>> ')
# sql = f"SELECT * FROM students WHERE name = '{name}'"
# cur.execute(sql)
# for row in cur.fetchall():
#     print(row)

cur.execute("SELECT * FROM students WHERE name = %s",('Siran Kaur',))
# rows = cur.fetchone()
# print("Result:", rows)
# # print("Result:", rows[0]) # error
# print(cur.rowcount)
cur.close()
connection.close()