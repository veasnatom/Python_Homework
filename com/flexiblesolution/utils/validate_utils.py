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

        return True,None


    @staticmethod
    def __validatePhone(phone:str):
        try:
            phone_number = phonenumbers.parse(phone)
        except BaseException as err:
            return False,'Invalid Phone (+85512345678)'
        if phonenumbers.is_possible_number(phone_number):
            return True,None
        else:
            return False,'Invalid Phone (+85512345678)'
    @staticmethod
    def __validateEmail(email:str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)):
            return True,None
        else:
            return False,'Invalid Email (example@mail.com)'


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
