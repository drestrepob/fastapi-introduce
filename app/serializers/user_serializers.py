from pydantic import BaseModel


class UserSerializer(BaseModel):
    id: int
    full_name: str

    class Config:
        from_attributes = True
