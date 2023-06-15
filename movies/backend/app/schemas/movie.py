from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str | None = None


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True







"""


from typing import Optional

from pydantic import BaseModel


# Shared properties
class MovieBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class MovieCreate(MovieBase):
    title: str
    description: str


# Properties to receive on item update
class MovieUpdate(MovieBase):
    pass


# Properties shared by models stored in DB
class MovieInDBBase(MovieBase):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


# Properties to return to client
class Movie(MovieInDBBase):
    pass


# Properties properties stored in DB
class MovieInDB(MovieInDBBase):
    pass


"""