import mysql.connector
import time

print("⏳ Waiting for MariaDB to be ready...")
time.sleep(3)

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="vscode",
        password="",  # empty password
        database="mydatabase"
    )
    cursor = conn.cursor()

    # Example table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50)
        );
    """)
    conn.commit()

    print("Database 'mydatabase' is ready and table 'test_table' created.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close(
