from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    user_name: str = Field(default="UserName", min_length=1, max_length=15)
    user_mail: str = Field(default="UserMail", min_length=1, max_length=15)
    password: str = Field(default="Pass", min_length=1)
