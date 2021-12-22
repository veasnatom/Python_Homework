from xml.dom import UserDataHandler

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pony.orm import db_session, flush

from com.flexiblesolution.dbconnection.connection import user_class
from com.flexiblesolution.dto.tokendatadto import TokenDataDto
from com.flexiblesolution.dto.tokendto import TokenDto
from com.flexiblesolution.dto.userdto import UserDto
from com.flexiblesolution.token.oaut2 import get_current_user
from com.flexiblesolution.token.usertoken import create_access_token
from com.flexiblesolution.utils.validate_utils import ValidateUtils

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
def get_user_by_id(id:int, get_current_user:TokenDataDto=Depends(get_current_user)):
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
def update_user(id:int, request:UserDto, get_current_user:UserDto=Depends(get_current_user)):
    try:
        validate = ValidateUtils.validateInput(request)
        if validate[0] == True:
            with db_session:
                user = user_class.get(id=id)
                if user == None:
                    return 'Id not found.'
                else:
                    if user.email != request.email:
                        tmp = user_class.get(email=request.email)
                        if tmp != None:
                            return 'Email: '+request.email+' already exist'
                    request.password = pwd_context.hash(request.password)
                    request.id=id
                    user.set(**dict(request))
                    return 'Updated successfully'
        else:
            return validate[1]
    except BaseException as err:
        return "Error: {0}".format(err)
@user_router.delete('/delete_user')
def delete_user(id:int, get_current_user:TokenDataDto=Depends(get_current_user)):
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

@user_router.get('/get_all_user/')
def get_all_user(get_current_user:TokenDataDto=Depends(get_current_user)):
    try:
        with db_session:
            lst_user = user_class.select().order_by(user_class.name)
            users = []
            for u in lst_user:
                users.append(UserDto.from_orm(u))
        return users
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
    access_token = create_access_token(data={"sub":user.email})
    return TokenDto(access_token=access_token,token_type='bearer')

