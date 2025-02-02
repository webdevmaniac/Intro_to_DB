import mysql.connector

def create_database(host_name, db_user, db_password, db_name):
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host_name,
            user=db_user,
            password=db_password
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

        # Print a success message
        print(f"Database '{db_name}' created successfully!")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        # Print an error message if the connection fails
        print(f"Failed to connect to MySQL Server: {error}")

# Call the function to create the database
create_database("localhost", "your_username", "your_password", "alx_book_store")
