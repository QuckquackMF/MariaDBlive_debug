import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS testdb;")
print("Database created (if it didn't exist).")
cursor.close()
conn.close()
