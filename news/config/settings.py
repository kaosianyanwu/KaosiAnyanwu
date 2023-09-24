from decouple import config

# ================== Database Configuration ==================
DB_HOST = config('DB_HOST', default='localhost')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

# ================== NYT API Configuration ==================
NYT_API_BASE_URL = config('NYT_API_BASE_URL')
NYT_API_KEY = config('NYT_API_KEY')


DB_CONFIG = {
    "host": DB_HOST,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "database": DB_NAME,
}

NYT_API_CONFIG = {
    "base_url": NYT_API_BASE_URL,
    "api_key": NYT_API_KEY,
}