from pydantic import BaseModel
from typing import List, Union

class SQLDocumentBase(BaseModel):
    title:str
    body:str

class SQLDocumentCreate(SQLDocumentBase):
    id: int

    class Config:
        orm_mode = True