import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="vscode",
    password="",
    database="mydatabase"
)

cursor = conn.cursor()
cursor.execute("INSERT INTO test_table (name) VALUES ('Alice');")
conn.commit()

cursor.execute("SELECT * FROM test_table;")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
