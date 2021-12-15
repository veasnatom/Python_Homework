from typing import Any, cast

from com.flexiblesolution.dto.userdto import UserDto





class ValidateUtils:

    @staticmethod
    def validateInput(obj:object):
        if isinstance(obj,UserDto):
            ValidateUtils.validateUser(cast(UserDto,obj))

    @staticmethod
    def validateUser(user:UserDto):
        pass