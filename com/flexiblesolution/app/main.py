import uvicorn
from fastapi import FastAPI

from com.flexiblesolution.router.submitcaseroute import submit_case_router
from com.flexiblesolution.router.userroute import user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(submit_case_router)


'''
@app.post('/create_user')
def create_user(request:UserDto):
    try:
        with db_session:
            user = user_class(name=request.name, email=request.email, phone=request.phone, password=request.password, created_at=request.created_at,
                  updated_at=request.updated_at)
            flush()
        return {"id":user.id}
    except BaseException as err:
        return "Error: {0}".format(err)

@app.get('/user/{id}')
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
@app.post('/update_user')
def update_user(request:UserDto):
    try:
        with db_session:
            user = user_class.get(id=request.id)
            if user == None:
                return 'Id not found.'
            else:
                user.set(**dict(request))
                return 'Updated successfully'
    except BaseException as err:
        return "Error: {0}".format(err)
@app.post('/delete_user')
def delete_user(id:int):
    try:
        with db_session:
            user = user_class.get(id=id)
            if user.id == None:
                return 'Id not found'
            else:
                user.delete()
                return 'Deleted successfully.'
    except BaseException as err:
        return "Error: {0}".format(err)


'''
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)