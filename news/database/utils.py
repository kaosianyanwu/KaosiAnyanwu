import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def create_articles_table_sql():
    """SQL query to create the articles table"""
    create_articles_table_sql = """
    CREATE TABLE IF NOT EXISTS articles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT,
        author_id INT DEFAULT 0,
        author_name VARCHAR(255),
        published_date DATETIME,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        URL VARCHAR(255)
    )
    """
    return create_articles_table_sql
    
def insert_articles_sql():
    """SQL query to insert articles into the articles table"""
    insert_articles_sql = """
    INSERT INTO articles (title, content, author_id, author_name, published_date, URL)
    VALUES (%s, %s, NULL, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    title = VALUES(title),
    content = VALUES(content),
    author_id = VALUES(author_id),
    author_name = VALUES(author_name),
    published_date = VALUES(published_date),
    URL = VALUES(URL);
    """
    return insert_articles_sql

from datetime import datetime

def convert_date(date_str: str) -> datetime:
    """Convert a date string to a datetime object."""
    try:
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')

        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')

        return formatted_date
    except ValueError:
        logging.error(f"Invalid date format: {date_str}")
        return None
