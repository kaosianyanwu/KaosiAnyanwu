import logging
import mysql.connector
from decouple import config

logging.basicConfig(level=logging.INFO)

class DatabaseManager:
    """Manages SQL database connection and table creation"""
    def __init__(self):
        self.db_config = {
            "host": config('DB_HOST'),
            "user": config('DB_USER'),
            "password": config('DB_PASSWORD'),
            "database": config('DB_NAME'),
        }
        self.connection = None

    def initialize_connection(self):
        """Initialize mysql database connection"""
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            if self.connection.is_connected():
                logging.info("Connected to MySQL")
            else:
                logging.info("Failed to connect to MySQL")
        except mysql.connector.Error as err:
            logging.info(f"Error: {err}")

    def _execute_query(self, query: str, params=None):
        """Execute a SQL query with optional parameters."""
        try:
            if self.connection and self.connection.is_connected():
                cursor = self.connection.cursor()
               
                if params is not None:
                    if isinstance(params, tuple):
                        cursor.execute(query, params)
                    elif isinstance(params, list):
                        print(params)
                        lengths = [len(tup) for tup in params]
                        print(lengths)
                        cursor.executemany(query, params)
                        print("we got here")
                    else:
                        logging.error("Invalid parameters provided.")
                        return
                else:
                    cursor.execute(query)
                    
                self.connection.commit()
                logging.info(f"Query executed successfully.")
        except mysql.connector.Error as err:
            logging.error(f"Error in executing query: {err}")
            raise err

    def create_table(self, table_name: str, sql_query: str):
        """Create a table in the database."""
        try:
            self._execute_query(sql_query)
            logging.info(f"Table '{table_name}' created successfully.")
        except mysql.connector.Error as err:
            logging.error(f"Table not created: {err}")
            raise err
    
    def insert_data(self, table_name: str, sql_query: str, params: tuple):
        """Insert data into a table."""
        try:
            self._execute_query(sql_query, params)
            logging.info(f"Data inserted into table '{table_name}' with params: {params}")
        except mysql.connector.Error as err:
            logging.error(f"Data not inserted: {err}")
            raise err
    
    def close_connection(self):
        """Close the database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logging.info("MySQL connection closed")

    def print_articles_table(self):
        """Print the contents of the articles table."""
        try:
            if self.connection and self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM articles;")
                articles = cursor.fetchall()
                for article in articles:
                    print(article)
        except mysql.connector.Error as err:
            logging.error(f"Error in executing query: {err}")
