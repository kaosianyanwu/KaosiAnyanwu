import json
import logging
import requests

from typing import Optional, List, Dict

OK = 200
logging.basicConfig(level=logging.INFO)

class ArticleAPI:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.articles = []

    def fetch_articles(self, query: List[str], begin_date: Optional[str], end_date: Optional[str], sort: Optional[str], page: int) -> List[Dict[str, any]]:
        "Feth articles based on user search criteria"
        optional_params = {
            "begin_date": begin_date,
            "end_date": end_date,
            "sort": sort,
            "page": page
        }
        
        optional_params = {k: v for k, v in optional_params.items() if v is not None}
    
        params = {
            "api-key": self.api_key,
            **optional_params
        }

        articles = []
        for keyword in query:
            params["query"] = keyword
            response = requests.get(self.base_url, params=params)
    
            if response.status_code != OK:
                logging.error(f"Error {response.status_code}: {response.text}. There was an error while fetching articles")
                continue

            data = response.json()
            if "response" in data and "docs" in data["response"]:
                articles.extend(data["response"]["docs"])
            if not articles:
                logging.info(f"No articles found using {keyword} and the provided search criterias")
                return self.articles
        self.articles = articles
        return self.articles

    def refine_input(self, prompt: str, current_value: Optional[str] = None) -> str:
        """Prompt user for input and refine the search criteria"""
        logging.info(f"Current {prompt}: {current_value if current_value else 'None'}")
        new_value = input(f"Enter a new {prompt} or press Enter to keep the current value: ")
        return new_value if new_value else current_value

    def get_user_input(self, query: str, begin_date: Optional[str], end_date: Optional[str], sort: Optional[str], page: str) -> (str, Optional[str], Optional[str], Optional[str], int):
        """"Get user input for search criteria"""
        query = self.refine_input("List of keywords separated by commas (e.g., technology, science, politics): ", query).split(',') or None
        query = [q.split() for q in query]if query else None
        begin_date = self.refine_input("Begin date (YYYYMMDD) ", begin_date) or None
        end_date = self.refine_input("End date (YYYYMMDD) ", end_date) or None
        sort = self.refine_input("Sort type (newest, oldest, relevance) ", sort) or None
        try:
            page = int(self.refine_input("Page number ", page)) or 0
        except ValueError:
            page = 0
        return query, begin_date, end_date, sort, page

    def display_article(self) -> None:
        """Display articles based on search criteria"""
        for article in self.articles:
            print(article["headline"]["main"])
            print(article["pub_date"])
            print(article["web_url"])
            print("-"*70)

    def run(self) -> None:
        """Run the program"""
        query, begin_date, end_date, sort, page = None, None, None, None, 0
        while True:
            query, begin_date, end_date, sort, page = self.get_user_input(query, begin_date, end_date, sort, page)
            self.articles = self.fetch_articles(query, begin_date, end_date, sort, page)
            if self.articles:
                self.display_article()
                refine = input("Do you want to refine your search? (y/n): ")
                if refine.lower() in ["y", "yes"]:
                    continue
                else:
                    break
            else:
                logging.info("No articles found for the provided search criteria")
                continue


if __name__ == "__main__":
    BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    API_KEY = "Aclu4xRFlSVpVKAVcUAEUcAZp0I3mPDz"
    articleapi = ArticleAPI(API_KEY, BASE_URL)
    articleapi.run()