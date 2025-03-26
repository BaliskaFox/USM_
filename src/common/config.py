from os import getenv
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
DATABASE_URL = getenv('DATABASE_USRL')
ALGORITM = getenv("ALGORITM")
