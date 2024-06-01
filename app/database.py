from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import time
import psycopg2
from psycopg2.extras import RealDictCursor

from app.config import setting


# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:Bs79SK-=bj@localhost/wallet'

SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_host}:{setting.database_port}/{setting.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# while True:    
#     try:
#         conn = psycopg2.connect(host="localhost", database='wallet', user='postgres', password='Bs79SK-=bj', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as e:
#         time.sleep(3)
#         print(f"Connection to the database is failed!")
#         raise e
        
    
