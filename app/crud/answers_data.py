import logging
import datetime
from typing import Optional, Union, Dict, Any

from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.hdd import HDDData
from app.schemas.hdd import HDDDataCreate, HDDDataUpdate


class CRUDHDDData(CRUDBase[HDDData,
                           HDDDataCreate,
                           HDDDataUpdate]):

    def create(self, db: Session, *, obj_in=HDDDataCreate, should_commit=True) -> HDDData:
        create_data = obj_in.dict()
        db_obj = HDDData(**create_data)
        db.add(db_obj)
        if should_commit:
            db.commit()
        db.flush()
        return db_obj
