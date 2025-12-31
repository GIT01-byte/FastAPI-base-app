from pydantic import (
    BaseModel,
    ConfigDict,
    )


class UserSchema(BaseModel):
    useraname: str
    foo: int
    bar: int


class UserCreate(UserSchema):
    pass


class UserRead(UserSchema):
    model_config = ConfigDict(
        from_attributes=True,
    )
    
    id: int
