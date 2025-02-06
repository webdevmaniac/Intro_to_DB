import mysql.connector

def create_database(host_name, db_user, db_password, db_name):
try:
connection = mysql.connector.connect(
host=host_name,
user=db_user,
password=db_password
)
cursor = connection.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
connection.commit()
print(f"Database '{db_name}' created successfully!")
cursor.close()
connection.close()
except mysql.connector.Error as error:
print(f"Failed to connect to MySQL Server: {error}")

create_database("localhost", "your_username", "your_password", "alx_book_store")

