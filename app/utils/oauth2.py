from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException

from app.config import setting


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')



SECRET_KEY = setting.secret_key
ALGORITHM = setting.algorithm
ACCESS_TOKEN_EXPIRATION_MINUTES = int(setting.access_token_expiration_time)


def create_access_token(data: dict):
    
    try:
        data_to_encode = data.copy()
    
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_MINUTES)
        data_to_encode.update({"exp": expire})
        
        encode_jwt = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
        return encode_jwt

    except Exception as e:
        raise e



def verify_access_token(token: str, credentials_exceptions):
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        wallet_id: int = payload.get('wallet_id')
        
        if wallet_id == None:
            raise credentials_exceptions        
        # token_data = my_schema.TokenData(wallet_id=wallet_id)        
        return wallet_id
        
    except Exception as e:
        raise e


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exceptions = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Couldn't validate credentials", headers={"WWW-Authenticate": "Bearer"})
    
    return verify_access_token(token, credentials_exceptions)



