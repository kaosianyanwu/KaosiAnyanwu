import mysql.connector
import logging
from decouple import config

logging.basicConfig(level=logging.INFO)

db_config = {
    "host": config('DB_HOST'),
    "user": config('DB_USER'),
    "password": config('DB_PASSWORD'),
    "database": config('DB_NAME'),
}

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