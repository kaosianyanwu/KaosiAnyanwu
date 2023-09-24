import pytest

# Define a list of environment variables and their values for testing
ENVIRONMENT_VARIABLES = {
    "DB_HOST": "test_host",
    "DB_USER": "test_user",
    "DB_PASSWORD": "test_password",
    "DB_NAME": "test_db",
    "NYT_API_BASE_URL": "http://test.url",
    "NYT_API_KEY": "test_api_key"
}

@pytest.fixture(scope='function', params=ENVIRONMENT_VARIABLES.items())
def environment_variable(monkeypatch, request):
    key, value = request.param
    monkeypatch.setenv(key, value)
    return key, value
