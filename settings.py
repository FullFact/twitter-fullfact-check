import os
from os.path import join, dirname
from dotenv import load_dotenv


API_KEY = ''
API_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

FACTCHECK_API_URL = ''
FACTCHECK_API_KEY = ''


# Load environment variables from the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Load any extra environment variables overriding these settings
for var, value in os.environ.items():
    if var in globals():
        globals()[var] = value
