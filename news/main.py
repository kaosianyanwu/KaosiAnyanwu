from database.database_manager import DatabaseManager
from articles import ArticlesOperations
from config import settings

if __name__ == "__main__":
    BASE_URL = settings.NYT_API_CONFIG["base_url"]
    API_KEY = settings.NYT_API_CONFIG["api_key"]

    # Initialize the Database
    dbmanager = DatabaseManager()
    articleops = ArticlesOperations(dbmanager)
    dbmanager.initialize_connection()
    articleops.create_articles_table()
    articleops.insert_articles_into_db()
    dbmanager.print_articles_table()
    dbmanager.close_connection()
