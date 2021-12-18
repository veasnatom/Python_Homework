from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from starlette.status import HTTP_401_UNAUTHORIZED

from com.flexiblesolution.token.usertoken import SECRET_KEY, ALGORITHM, verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
def get_current_user(token:str=Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    return verify_token(token,credential_exception)
