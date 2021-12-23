from datetime import datetime

from pony.orm import PrimaryKey, Required, Optional, Set


def getUser(db):
    class UserModel(db.Entity):
        _table_ = 'user'
        id = PrimaryKey(int, auto=True)
        name = Required(str)
        email = Required(str)
        phone = Required(str)
        password = Required(str)
        created_at = Required(datetime)
        updated_at = Required(datetime)
        owner_id = Set('SubmitCaseModel')
        created_by = Set('SubmitCaseModel')
        updated_by = Set('SubmitCaseModel')
    return UserModel
