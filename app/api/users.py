from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app import models, my_schema
from app.utils import hashing_password, utils, oauth2
from app.utils.serializers import users_serializer, wallet_serializer

from random import randint


router = APIRouter(
    prefix='/users',
    tags= ['Users']
)


@router.get('/all_users')
async def get_all_users(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    print(id)
    try:    
        users = db.query(models.Users).filter(models.Users.first_name.contains(search)).limit(limit).offset(skip).all()
        
        if not users:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found!")
        return users
    except Exception as e:
        raise e


@router.post('/create_user', response_model=my_schema.UserResponseModel)
async def create_user(user: my_schema.CreateUser, db: Session = Depends(get_db)):
    try:
        
        if user.wallet_id:
            user.wallet_id = randint(0000000000,9999999999)
            
        res = await utils.create_user_wallet(users_serializer(user))      
        
        if not res:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong with user_wallet response")
        
        # hashing user's password
        hashed_password = hashing_password.hashing(user.password)
        user.password = hashed_password
        
        new_user = models.Users(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        new_wallet = models.UserWallet(**wallet_serializer(res))
        db.add(new_wallet)
        db.commit()
        
        return new_user
    except Exception as e:
        raise e


@router.get('/get_user_by_id/{wallet_id}', response_model=my_schema.User)
async def get_user_by_id(db: Session = Depends(get_db), wallet_id: int = Depends(oauth2.get_current_user)):
    
    try:
        current_user = db.query(models.Users).filter(models.Users.wallet_id == wallet_id).first()
        
        if not current_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {wallet_id} not found!")
        
        return current_user

    except Exception as e:
        raise e


@router.delete('/delete_user_by_id/{wallet_id}')
async def delete_user(db: Session = Depends(get_db), wallet_id: int = Depends(oauth2.get_current_user)):
    
    try:
        user = db.query(models.Users).filter(models.Users.wallet_id == wallet_id).first()
    
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with {wallet_id} was not found!') 
        
        db.delete(user)
        db.commit()
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Deleted successfully")
    except Exception as e:
        raise e


@router.put('/update_user/{wallet_id}', response_model=my_schema.UserResponseModel)
async def update_user(user: my_schema.UpdateUser, db: Session = Depends(get_db), wallet_id: int = Depends(oauth2.get_current_user)):
    
    try:
        user_query = db.query(models.Users).filter(models.Users.wallet_id == wallet_id)
        
        current_user = user_query.first()
        
        # hashing password before updating
        hashed_password = hashing_password.hashing(current_user.password)
        current_user.password = hashed_password
        
        if current_user == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with {wallet_id} was not found!')
        
        user_query.update(user.model_dump(),synchronize_session=False)
        db.commit()
        db.refresh(current_user)
        
        return current_user

    except Exception as e:
        raise e

