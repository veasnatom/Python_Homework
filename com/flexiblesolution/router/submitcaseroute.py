
from fastapi import APIRouter
from fastapi.params import Depends
from pony.orm import db_session, flush

from com.flexiblesolution.dbconnection.connection import user_class, submit_case_class
from com.flexiblesolution.dto.submitcasedto import SubmitCaseDto
from com.flexiblesolution.dto.tokendatadto import TokenDataDto
from com.flexiblesolution.dto.userdto import UserDto
from com.flexiblesolution.token.oaut2 import get_current_user
from com.flexiblesolution.utils.validate_utils import ValidateUtils

submit_case_router = APIRouter(
    prefix='/submit_case',
    tags=['Submit_Case']
)

@submit_case_router.post('/create_submit_case')
def create_submit_case(request:SubmitCaseDto, get_current_user:TokenDataDto=Depends(get_current_user)):
    try:
        validate = ValidateUtils.validateInput(request);
        if validate[0] == True:
            with db_session:
                submit_case = submit_case_class(owner_id=user_class.get(id=request.owner_id),
                                                street_no=request.street_no,
                                                house_no=request.house_no,
                                                address=request.address,
                                                land_width=request.land_width,
                                                land_length=request.land_length,
                                                land_area=request.land_area,
                                                description=request.description,
                                                record_type=request.record_type,
                                                type=request.type,
                                                created_by=user_class.get(id=request.created_by),
                                                updated_by=user_class.get(id=request.updated_by),
                                                created_at=request.created_at,
                                                updated_at=request.updated_at,
                                                deleted_at=request.deleted_at,
                                                current_use=request.current_use,
                                                case_status=request.case_status,
                                                instructor_date=request.instructor_date,
                                                due_date=request.due_date,
                                                indication_date=request.indication_date)

                flush()
                return {"id:",submit_case.id}
        else:
            return validate[1]
    except BaseException as err:
        return 'Error: {0}'.format(err)

@submit_case_router.get('/{id}')
def get_user_by_id(id:int, get_current_user:TokenDataDto=Depends(get_current_user)):
    try:
        with db_session:
            submit_case = submit_case_class.get(id=id)
        if submit_case == None:
            return 'Id not found.'
        else:

            result = SubmitCaseDto(id=submit_case.id,
                                   owner_id=submit_case.owner_id.id,
                                   street_no=submit_case.street_no,
                                   house_no=submit_case.house_no,
                                   address=submit_case.address,
                                   land_width=submit_case.land_width,
                                   land_length=submit_case.land_length,
                                   land_area=submit_case.land_area,
                                   description=submit_case.description,
                                   record_type=submit_case.record_type,
                                   type=submit_case.type,
                                   created_by=submit_case.created_by.id,
                                   updated_by=submit_case.updated_by.id,
                                   created_at=submit_case.created_at,
                                   updated_at=submit_case.updated_at,
                                   deleted_at=submit_case.deleted_at,
                                   current_use=submit_case.current_use,
                                   case_status=submit_case.case_status,
                                   instructor_date=submit_case.instructor_date,
                                   due_date=submit_case.due_date,
                                   indication_date=submit_case.indication_date
                                   )
            return result
    except BaseException as err:
        return "Error: {0}".format(err)

@submit_case_router.put('/update_submit_case')
def update_submit_case(id:int, request: SubmitCaseDto, get_current_user:TokenDataDto=Depends(get_current_user)):
    try:
        validate = ValidateUtils.validateInput(request);
        if validate[0] == True:
            with db_session:
                submit_case = submit_case_class.get(id=id)
                if submit_case == None:
                    return 'Id not found.'
                else:
                    submit_case.set(**dict(request))
                    return 'Updated successfully'
        else:
            return validate[1]
    except BaseException as err:
        return "Error: {0}".format(err)

@submit_case_router.get('/get_all_submit_case/')
def get_all_submit_case(get_current_user:TokenDataDto=Depends(get_current_user)):
    try:
        with db_session:
            lst_submit_case = submit_case_class.select().order_by(submit_case_class.id)
            submit_cases = []
            for s in lst_submit_case:
                submit_cases.append(SubmitCaseDto(
                    id=s.id,
                    owner_id=s.owner_id.id,
                    street_no=s.street_no,
                    house_no=s.house_no,
                    address=s.address,
                    land_width=s.land_width,
                    land_length=s.land_length,
                    land_area=s.land_area,
                    description=s.description,
                    record_type=s.record_type,
                    type=s.type,
                    created_by=s.created_by.id,
                    updated_by=s.updated_by.id,
                    created_at=s.created_at,
                    updated_at=s.updated_at,
                    deleted_at=s.deleted_at,
                    current_use=s.current_use,
                    case_status=s.case_status,
                    instructor_date=s.instructor_date,
                    due_date=s.due_date,
                    indication_date=s.indication_date
                ))
        return submit_cases
    except BaseException as err:
        return 'Error: {0}'.format(err)

@submit_case_router.delete('/delete_submit_case')
def delete_submit_case(id:int, get_current_user:TokenDataDto=Depends(get_current_user)):
    try:
        with db_session:
            delete_submit_case = submit_case_class.get(id=id)
            if delete_submit_case == None:
                return 'Id not found'
            else:
                delete_submit_case.delete()
                return 'Deleted successfully.'
    except BaseException as err:
        return "Error: {0}".format(err)

