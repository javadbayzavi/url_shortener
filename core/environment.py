from os import getenv
from dotenv import load_dotenv
load_dotenv()

ALLOWED_ORIGINS= getenv("ALLOW  ED_ORIGINS", "*").split(",")
ALLOWED_METHODS= getenv("ALLOWED_METHODS", "*").split(",")
SERVER_HOST= getenv("SERVER_HOST", None)
SERVER_PORT= int(getenv("SERVER_PORT", None))
CACHE_HOST= getenv("CACHE_HOST", None)
CACHE_PORT= int(getenv("CACHE_PORT", None))
CACHE_DB= getenv("CACHE_DB", None)
DB_HOST= getenv("DB_HOST", None)
DB_PORT= int(getenv("DB_PORT", None))
DB_NAME= getenv("DB_NAME", None)
DB_PASS= getenv("DB_PASS", None)
DB_USER= getenv("DB_USER", None)

