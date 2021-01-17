from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ImageModel(BaseModel):
    filename: str = Field(...)
    description: Optional[EmailStr] = Field(...)
    user_id: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "filename": "My Image",
                "description": "this is my image",
                "user_id": "ghyteu35jdsvh34jnn3j"
            }
        }


class UserModel(BaseModel):
    user_id: str
    fullname: Optional[str]
    email: EmailStr
   
    class Config:
        schema_extra = {
            "example": {
                "user_id": "dfhru3y4u3nu3jj4",
                "fullname": "John Doe",
                "email": "user@mail.com",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}