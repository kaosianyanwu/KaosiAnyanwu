import mysql.connector
import logging

logging.basicConfig(level=logging.INFO)

# Define your MySQL connection parameters
db_config = {
    "host": "localhost",
    "user": "kaosi",  # Replace with your MySQL username
    "password": "Thisisus@20",  # Replace with your MySQL password
    "database": "news_articles",  # Replace with your database name
}

# Connect to MySQL
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        logging.info("Connected to MySQL")
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print("Test query result:", result)

    else:
        logging.info("Failed to connect to MySQL")
except mysql.connector.Error as err:
    logging.info(f"Error: {err}")

finally:
   if "connection" in locals() and connection.is_connected():
        connection.close()
        logging.info("MySQL connection closed")
