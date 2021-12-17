import re
from datetime import datetime
from typing import Any, cast

import phonenumbers
from click import exceptions

from com.flexiblesolution.dto.submitcasedto import SubmitCaseDto
from com.flexiblesolution.dto.userdto import UserDto





class ValidateUtils:

    @staticmethod
    def validateInput(obj:object):
        if isinstance(obj,UserDto):
            return ValidateUtils.__validate_user(cast(UserDto, obj))
        elif isinstance(obj,SubmitCaseDto):
            return ValidateUtils.__validate_submit_case(cast(SubmitCaseDto, obj))

#Use validate section
    @staticmethod
    def __validate_user(user:UserDto):
        #validate phone
        validate_phone = ValidateUtils.__validatePhone(user.phone)
        if validate_phone[0]==False:
            return validate_phone
        #validate email
        validate_email = ValidateUtils.__validateEmail(user.email)
        if validate_email[0] == False:
            return validate_email
        #validate_datetime
        validate_created_at = ValidateUtils.__validate_date_time(user.created_at)
        if validate_created_at[0] == False:
            return validate_created_at
        validate_updated_at = ValidateUtils.__validate_date_time(user.updated_at)
        if validate_updated_at[0] == False:
            return validate_updated_at
        return True,None


    @staticmethod
    def __validatePhone(phone:str):
        try:
            phone_number = phonenumbers.parse(phone)
        except BaseException as err:
            return False,'Invalid Phone'
        if phonenumbers.is_possible_number(phone_number):
            return True,None
        else:
            return False,'Invalid Phone'
    @staticmethod
    def __validateEmail(email:str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)):
            return True,None
        else:
            return False,'Invalid Email'

    @staticmethod
    def __validate_date_time(date_string:datetime):
        format = "%Y-%m-%dT%H:%M:%S"
        try:
            datetime.strptime(date_string, format)
            return True,None
        except BaseException as err:
            return False,'Invalid format YYYY-MM-DDTHH:mm:ss'
#end user validate section
#Submit_Case validate section
    @staticmethod
    def __validate_submit_case(submit_case:SubmitCaseDto):
        owner_id = ValidateUtils.__validate_int(submit_case.owner_id)
        if owner_id[0] == False:
            return owner_id

        return True,None
    @staticmethod
    def __validate_int(value:str):
        try:
            int(value)
            return True,None
        except BaseException as err:
            return False,'Invalid Integer'
    @staticmethod
    def __validate_number(value:str):
        try:
            float(value)
            return True,None
        except BaseException as err:
            return False,'Invalid Number'
#end Submit_Case validate section
