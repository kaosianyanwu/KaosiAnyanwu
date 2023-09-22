# News Article Recommender System
NOTE: I am using a MAC, so all instructions are based on macOS operating system. Other operating systems may have different instructions.

## Setting up Virtual Environment

- cd to the directory where you want to create your project
- `python -m venv venv`
- `source venv/bin/activate` Your virtual environment is active if it appears on the far left of your path
- `pip install beautifulsoup4`. Install this library for web scrapping
- Alternatively, you can utilize APIs from your favourite news website. 
    * I am using new york times and utilizing their API. For reference: [NYT APIs](https://developer.nytimes.com/get-started)

## Setting up Database 
- `pip install mysql-connector-python`. You'll need the MySQL Connector/Python library to connect to MySQL from your Python script.