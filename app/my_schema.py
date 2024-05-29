from pydantic import BaseModel, EmailStr
from typing import Optional

from datetime import datetime
from random import randint


from enum import Enum


class User(BaseModel):
    wallet_id: int = randint(0000000000, 9999999999)
    first_name: str
    last_name: str
    email: EmailStr
    phone: str


class CreateUser(User):
    password: str
    bvn: str
    bvn_dob: str
    created_at: datetime
    
    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    wallet_id: int


class TransferDetails(str, Enum):
    amount: int
    reference: str = f"ref-{randint(0000, 9999)}"
    narration: str
    destinationBankCode: str
    destinationAccountNumber: str
    currency: str = "NGN"
    sourceAccountNumber: str


class Transfer(BaseModel):
    amount: int
    reference: str = TransferDetails.reference
    narration: str
    destinationBankCode: str
    destinationAccountNumber: str
    currency: str = "NGN"
    sourceAccountNumber: str


class ValidateOTP(BaseModel):
    reference: str = TransferDetails.reference
    authorizationCode: str


# ********** RESPONSE MODELS ************
class UserResponseModel(BaseModel):
    wallet_id: int
    email: EmailStr
    phone: str


class WalletResponseModel(BaseModel):
    wallet_ref: int
    wallet_name: str
    account_number: int
    account_name: str
    bank_name: str
    balance: int
    
    class Config:
        orm_mode = True


class TransferResponseModel(BaseModel):
    amount: int
    reference: str
    status: str
    dateCreated: str
    totalFee: float
    destinationBankName: str
    destinationAccountNumber: int
    
    class Config:
        orm_mode = True



# class Permission(BaseModel):
#     name: str
#     read: bool
#     write: bool
#     description: str


# class Role(BaseModel):
#     name: str
#     description: str
#     permission: List[Permission]

