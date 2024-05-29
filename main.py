import time
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os

from app.database import engine
from app import models
from app.api import users, wallets, auth, transactions


models.Base.metadata.create_all(bind=engine)
app = FastAPI()




while True:    
    try:
        conn = psycopg2.connect(host="localhost", database='wallet', user='postgres', password='Bs79SK-=bj', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as e:
        time.sleep(3)
        print(f"Connection to the database is failed!")
        raise e
        
    
    
    
    
@app.get('/')
def root():
    return {"status": "chill bro, server is up and running"}


app.include_router(users.router)
app.include_router(wallets.router)
app.include_router(auth.router)
app.include_router(transactions.router)

