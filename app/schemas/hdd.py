import datetime
from typing import Optional

from pydantic import BaseModel


class HDDDataBase(BaseModel):
    name: str
    manufacturer: str
    total: int
    allocated: int
    capacity_gb: int
    size: str
    rpm: int

    class Config:
        orm_mode = True


class HDDDataCreate(HDDDataBase):
    pass

    class Config:
        orm_mode = True




class HDDDataUpdate(HDDDataBase):
    id: Optional[int] = None
