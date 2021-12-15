from fastapi import APIRouter
from pony.orm import db_session, flush

from com.flexiblesolution.dbconnection.connection import user_class
from com.flexiblesolution.dto.userdto import UserDto
from com.flexiblesolution.utils.validate_utils import ValidateUtils

user_router = APIRouter(
    prefix='/user',
    tags=['User']
)

@user_router.post('/create_user')
def create_user(request:UserDto):
    try:
        ValidateUtils.validateInput(request)
        with db_session:
            user = user_class(name=request.name, email=request.email, phone=request.phone, password=request.password, created_at=request.created_at,
                  updated_at=request.updated_at)
            flush()
        return {"id":user.id}
    except BaseException as err:
        return "Error: {0}".format(err)

@user_router.get('/{id}')
def get_user_by_id(id:int):
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
def update_user(id:int,request:UserDto):
    try:
        with db_session:
            user = user_class.get(id=id)
            if user == None:
                return 'Id not found.'
            else:
                user.set(**dict(request))
                return 'Updated successfully'
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

