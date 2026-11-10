from pydantic import (
    BaseModel,
    ConfigDict,
)


class UserSchema(BaseModel):
    username: str
    foo: int
    bar: int


class UserCreate(UserSchema):
    pass


class UserRead(UserSchema):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
