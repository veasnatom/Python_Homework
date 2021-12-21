from typing import Optional

from pydantic import BaseModel


class TokenDataDto(BaseModel):
    email:Optional[str]=None