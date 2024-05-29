from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import models, my_schema
from app.utils import oauth2

router = APIRouter(
    prefix='/wallets',
    tags= ['Wallets']
)



@router.get('/get_all_wallets')
async def get_all_wallets(db: Session = Depends(get_db), wallet_id: int = Depends(oauth2.get_current_user)):
    
    try:
        wallets = db.query(models.UserWallet).all()  
        if not wallets:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No wallet was found!")
                
        return wallets
    
    except Exception as e:
        raise e


@router.get('/get_wallet_by_id/{wallet_id}', response_model=my_schema.WalletResponseModel)
async def get_wallet_by_id(db: Session = Depends(get_db), wallet_id: int = Depends(oauth2.get_current_user)):
    
    try:
        current_wallet = db.query(models.UserWallet).filter(models.UserWallet.wallet_ref == wallet_id).first()
                
        if not current_wallet:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'wallet with {wallet_id} was not found!')
        
        
        return current_wallet

    except Exception as e:
        raise e




    
