
import datetime
from typing import Optional

from pydantic import BaseModel


class SSDDataBase(BaseModel):
    name: str
    manufacturer: str
    total: int
    allocated: int
    capacity_gb: int
    interface: str

    class Config:
        orm_mode = True


class SSDDataCreate(SSDDataBase):
    pass

class SSDDataUpdate(SSDDataBase):
    id: Optional[int] = None
