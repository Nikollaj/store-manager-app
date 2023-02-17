import logging
import datetime
from typing import Optional, Union, Dict, Any
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.hdd import HDDData
from app.models.ssd import SSDData
from app.models.cpu import CPUData
from app.schemas.hdd import HDDDataCreate, HDDDataUpdate
from app.schemas.ssd import SSDDataCreate, SSDDataUpdate
from app.schemas.cpu import CPUDataCreate, CPUDataUpdate
from pydantic import BaseModel
import enum


class STORAGES(str, enum.Enum):
    cpu = "cpu",
    hdd = "hdd",
    ssd = "ssd"


class StorageModels(enum.Enum):
    cpu = CPUData
    hdd = HDDData
    ssd = SSDData


class CRUDStorageData(CRUDBase[Union[HDDData, SSDData, CPUData],
                           Union[HDDDataCreate, SSDDataCreate, CPUDataCreate],
                           Union[HDDDataUpdate, SSDDataUpdate, CPUDataUpdate]]):
    def get_by_name(self, db, name, storage_model):
        return db.query(storage_model).filter(storage_model.name == name).first()

    def create_or_update(self, db: Session, *, obj_in=BaseModel, should_commit=True, storage_type: str):
        storage_model = StorageModels[storage_type].value
        campaign_in_db = self.get_by_name(db, name=obj_in.name, storage_model=storage_model)
        if campaign_in_db:
            return self.update(db, db_obj=campaign_in_db, obj_in=obj_in, should_commit=should_commit)

        return self.create(db=db, obj_in=obj_in, should_commit=should_commit, storage_type=storage_type)

    def create(self, db: Session, *, obj_in=BaseModel, should_commit=True, storage_type: str) -> \
            Union[HDDData, SSDData, CPUData]:

        if storage_type == STORAGES.hdd:
            create_data = obj_in.dict()
            db_obj = HDDData(**create_data)
            db.add(db_obj)
            if should_commit:
                db.commit()
            db.flush()
            return db_obj
        elif storage_type == STORAGES.ssd:
            create_data = obj_in.dict()
            db_obj = SSDData(**create_data)
            db.add(db_obj)
            if should_commit:
                db.commit()
            db.flush()
            return db_obj
        else:
            create_data = obj_in.dict()
            db_obj = CPUData(**create_data)
            db.add(db_obj)
            if should_commit:
                db.commit()
            db.flush()
            return db_obj

    def update(self, db: Session, *, db_obj: Union[HDDData, CPUData, SSDData],
               obj_in: Union[HDDDataCreate, CPUDataCreate, SSDDataCreate],
               should_commit=True):
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data, should_commit=should_commit)

    def get_all_in_db(self, db: Session, db_obj=Union[HDDData, CPUData, SSDData]) \
            -> Union[HDDData, SSDData, CPUData]:
        return db.query(db_obj).all()
