from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

SECRET_KEY = 'flexiblesolution'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 3

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt