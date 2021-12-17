from typing import Any, cast

import phonenumbers

from com.flexiblesolution.dto.userdto import UserDto





class ValidateUtils:

    @staticmethod
    def validateInput(obj:object):
        if isinstance(obj,UserDto):
            return ValidateUtils.validateUser(cast(UserDto,obj))

    @staticmethod
    def validateUser(user:UserDto):
        phone_number = phonenumbers.parse(user.phone)
        if phonenumbers.is_possible_number(phone_number):
            return True,None
        else:
            return False,None