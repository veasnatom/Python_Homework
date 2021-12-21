from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException
from jose import jwt, JWTError

from com.flexiblesolution.dto.tokendatadto import TokenData

SECRET_KEY = 'flexiblesolution'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 3

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str,credential_exception:HTTPException):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        if email is None:
            raise credential_exception
        return TokenData(email=email)
    except JWTError as err:
        raise credential_exception