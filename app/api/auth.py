from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app import database, models, my_schema
from app.utils import utils
from app.utils.oauth2 import create_access_token



router = APIRouter(
    prefix='/auth',
    tags=["Authentication"]
)


@router.post('/login')
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    try:
        user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()
            
        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials!")
        
        if not utils.verify_password(user_credentials.password, user.password):
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail='Invalid credentials!')
        
        access_token = create_access_token(data={"wallet_id": user.wallet_id})
        
        return {"access_token": access_token, "token_type": "bearer"}

        
    except Exception as e:
        raise e
    
    