from fastapi import FastAPI

from app.database import engine
from app import models
from app.api import users, wallets, auth, transactions


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users.router)
app.include_router(wallets.router)
app.include_router(auth.router)
app.include_router(transactions.router)



@app.get('/')
def root():
    return {"status": "chill bro, server is up and running..."}

