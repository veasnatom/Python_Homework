from datetime import datetime

from pony.orm import PrimaryKey, Required, Optional


def getSubmitCase(db,userModel):
    class SubmitCaseModel(db.Entity):
        _table_ = 'submit_case'
        id = PrimaryKey(int,auto=True)
        owner_id = Required(userModel,reverse='owner_id')
        street_no = Optional(str)
        house_no = Optional(str)
        address = Optional(str)
        land_width = Required(float)
        land_length = Required(float)
        land_area = Required(float)
        description = Optional(str)
        record_type = Required(str)
        type = Required(str)
        created_by = Required(userModel,reverse='created_by')
        updated_by = Required(userModel,reverse='updated_by')
        created_at = Required(datetime)
        updated_at = Required(datetime)
        deleted_at = Optional(datetime)
        current_use = Required(str)
        case_status = Required(str)
        instructor_date = Required(datetime)
        due_date = Optional(datetime)
        indication_date = Optional(datetime)
    return SubmitCaseModel
