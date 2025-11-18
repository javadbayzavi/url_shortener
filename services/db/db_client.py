from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from core.environment import DB_PORT, DB_HOST, DB_NAME, DB_PASS, DB_USER
__db_url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(url=__db_url, echo=True)
session = Session(bind=engine)