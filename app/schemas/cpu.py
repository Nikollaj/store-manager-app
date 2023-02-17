import datetime
from typing import Optional

from pydantic import BaseModel


class CPUDataBase(BaseModel):
    name: str
    manufacturer: str
    total: int
    allocated: int
    cores: int
    socket: str
    power_watts: int

    class Config:
        orm_mode = True


class CPUDataCreate(CPUDataBase):
    pass


class CPUDataUpdate(CPUDataBase):
    id: Optional[int] = None
