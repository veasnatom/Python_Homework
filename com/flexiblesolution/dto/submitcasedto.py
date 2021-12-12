from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel


class SubmitCaseDto(BaseModel):
    id:Optional[int]
    owner_id : Optional[int]
    street_no : Optional[str]
    house_no : Optional[str]
    address : Optional[str]
    land_width : Optional[float]
    land_length : Optional[float]
    land_area : Optional[float]
    description : Optional[str]
    record_type : Optional[str]
    type : Optional[str]
    created_by : Optional[int]
    updated_by : Optional[int]
    created_at : Optional[datetime]
    updated_at : Optional[datetime]
    deleted_at : Optional[datetime]
    current_use : Optional[str]
    case_status : Optional[str]
    instructor_date : Optional[datetime]
    due_date : Optional[datetime]
    indication_date : Optional[datetime]

    class Config:
        updated_by:Optional[int]
        orm_mode = True
        arbitrary_types_allowed = True


