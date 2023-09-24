# articles_operations.py
import logging
import mysql.connector
from typing import List, Dict, Any

from config import settings
from news_api import ArticleAPI
from database.database_manager import DatabaseManager
from database.utils import create_articles_table_sql, insert_articles_sql, convert_date  

logging.basicConfig(level=logging.INFO)

BASE_URL = settings.NYT_API_CONFIG["base_url"]
API_KEY = settings.NYT_API_CONFIG["api_key"]

class ArticlesOperations:
    """Hands articles operations."""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def prepare_articles(self, articles: List[Dict[str, Any]]) -> List[tuple]:
        """Prepare articles for insertion into the database."""
        prepared_articles = []
        if articles is None:
            logging.info("No articles to prepare.")
            return prepared_articles
        for article in articles:
            # Extract relevant data from the article dictionary
            title = article.get("headline", {}).get("main", "")
            content = article.get("snippet", "")
        
            # Extract author name from the byline field
            persons = article.get("byline", {}).get("person", [])
            author_name = ""
            if persons:
                first_name = persons[0].get("firstname", "")
                last_name = persons[0].get("lastname", "")
                if first_name and last_name:
                    author_name = f"{first_name} {last_name}"
            
            published_date = convert_date(article.get("pub_date", ""))
            url = article.get("web_url", "")
            # Prepare a tuple with article data
            article_data = (title, content, author_name, published_date, url)
            prepared_articles.append(article_data)

        return prepared_articles

    def insert_articles_into_db(self):
        """Insert articles into the database."""
        # Initialize the ArticleAPI to get articles
        article_api = ArticleAPI(API_KEY, BASE_URL)
        articles = article_api.run()

        # Prepare articles for insertion
        prepared_articles = self.prepare_articles(articles)


        if articles:
            try:
                self.db_manager.insert_data('articles', insert_articles_sql(), prepared_articles)
                logging.info(f"{len(articles)} articles inserted into the database.")
            except mysql.connector.Error as err:
                logging.error(f"Error inserting articles into the database: {err}")
        else:
            logging.info("No articles to insert into the database.")

    def create_articles_table(self):
        """Create the articles table in the database."""
        try:
            self.db_manager.create_table('articles', create_articles_table_sql())
        except mysql.connector.Error as err:
            logging.error(f"Error creating articles table: {err}")