from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from passlib.context import CryptContext
from pony.orm import db_session, flush

from com.flexiblesolution.dbconnection.connection import user_class
from com.flexiblesolution.dto.userdto import UserDto
from com.flexiblesolution.utils.validate_utils import ValidateUtils
from com.flexiblesolution.token.oaut2 import get_current_user
from com.flexiblesolution.token.usertoken import ACCESS_TOKEN_EXPIRE_MINUTE, create_access_token

user_router = APIRouter(
    prefix='/user',
    tags=['User']
)

pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

@user_router.post('/create_user')
def create_user(request:UserDto):
    try:
        validate = ValidateUtils.validateInput(request)
        if(validate[0] == True):
            with db_session:
                user = user_class.get(email=request.email)
                if user != None:
                    return 'Email: '+request.email+' already exist'
                user = user_class(name=request.name, email=request.email, phone=request.phone, password=pwd_context.hash(request.password), created_at=request.created_at,
                      updated_at=request.updated_at)
                flush()
            return {"id":user.id}
        else:
            return validate[1]

    except BaseException as err:
        return "Error: {0}".format(err)

@user_router.get('/{id}')
def get_user_by_id(id:int,get_current_user:UserDto=Depends(get_current_user)):
    try:
        with db_session:
            user = user_class.get(id=id)
        if user == None:
            return 'Id not found.'
        else:
            result = UserDto.from_orm(user)
            return result
    except BaseException as err:
        return "Error: {0}".format(err)
@user_router.put('/update_user')
def update_user(request:UserDto):
    try:
        if request.id == None:
            return 'id is required.'
        validate = ValidateUtils.validateInput(request)
        if validate[0] == True:
            with db_session:
                user = user_class.get(id=request.id)
                if user == None:
                    return 'Id not found.'
                else:
                    if user.email != request.email:
                        tmp = user_class.get(email=request.email)
                        if tmp != None:
                            return 'Email: '+request.email+' already exist'
                    request.password = pwd_context.hash(request.password)
                    user.set(**dict(request))
                    return 'Updated successfully'
        else:
            return validate[1]
    except BaseException as err:
        return "Error: {0}".format(err)
@user_router.delete('/delete_user')
def delete_user(id:int):
    try:
        with db_session:
            user = user_class.get(id=id)
            if user == None:
                return 'Id not found'
            else:
                user.delete()
                return 'Deleted successfully.'
    except BaseException as err:
        return "Error: {0}".format(err)

@user_router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends()):
    with db_session:
        user = user_class.get(email=request.username)
    if user == None:
        return 'Invlaid Username'

    if not pwd_context.verify(request.password,user.password):
        return 'Invaid Password'
    #general access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    access_token = create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}

