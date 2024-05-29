from fastapi import APIRouter, Depends, status, HTTPException

from app import my_schema
from app.utils import utils, oauth2


router = APIRouter(
    prefix= "/transfer",
    tags= ["Transactions"]
)


@router.post('/initiate_transfer', response_model=my_schema.TransferResponseModel)
async def initiate_transfer(transfer_info: my_schema.Transfer, wallet_id: int = Depends(oauth2.get_current_user)):
    try:
        transfer_details = await utils.initiate_transfer(transfer_info)
        
        if not transfer_details:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="something went wrong with while initiating transfer!")
        
        return transfer_details

    except Exception as e:
        raise e


@router.post('/verify_otp', response_model=my_schema.TransferResponseModel)
async def verify_otp(transfer_info: my_schema.ValidateOTP, wallet_id: int = Depends(oauth2.get_current_user)):
    try:
        res = await utils.verify_OTP(transfer_info)
        
        if not res:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="something went wrong while validating transfer!")

        return res
    except Exception as e:
        raise e
