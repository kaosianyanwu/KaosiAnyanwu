from importlib import reload
from news.config import settings

class TestSettings:

    def test_environment_variables_loaded(self, environment_variable):
        key, value = environment_variable
        reload(settings)
        config_mapping = {
            "DB_HOST": settings.DB_CONFIG["host"],
            "DB_USER": settings.DB_CONFIG["user"],
            "DB_PASSWORD": settings.DB_CONFIG["password"],
            "DB_NAME": settings.DB_CONFIG["database"],
            "NYT_API_BASE_URL": settings.NYT_API_CONFIG["base_url"],
            "NYT_API_KEY": settings.NYT_API_CONFIG["api_key"],
        }
        
        assert config_mapping[key] == value