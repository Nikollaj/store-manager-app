import app.models.hdd
from app.crud.hdd import CRUDStorageData
from app.models.hdd import HDDData


class CRUDComponents:
    def __init__(self):
        self.storage_data = CRUDStorageData(HDDData)
