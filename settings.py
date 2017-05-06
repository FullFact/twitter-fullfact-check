import os
from os.path import join, dirname
from dotenv import load_dotenv


API_KEY = ''
API_SECRET = ''


# Load environment variables from the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Load any extra environment variables overriding these settings
for var, value in os.environ.items():
    if var in globals():
        globals()[var] = value

