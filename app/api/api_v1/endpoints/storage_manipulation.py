from fastapi import APIRouter, Depends
from app.core.config import Settings
from app.api.api_v1.deps import ApiDependencies
from sqlalchemy.orm import Session
import pandas as pd
import numpy as np
import math
import numpy.linalg as LA
from app.crud.components import CRUDComponents
from app.models.hdd import HDDData
from app.models.ssd import SSDData
from app.models.cpu import CPUData
from app.schemas.hdd import HDDDataBase
from app.schemas.hdd import HDDDataCreate
from app.schemas.ssd import SSDDataCreate, SSDDataBase
from app.schemas.cpu import CPUDataCreate, CPUDataBase
from http import HTTPStatus
from app.models.resources.storage.hdd import HDD
from app.models.resources.storage.ssd import SSD
from app.models.resources.cpu import CPU
from typing import Union, Any
import enum
from app.crud.hdd import STORAGES, StorageModels


class AvailableProcesses(enum.Enum):
    claim = "claim"
    freeup = "freeup"
    died = "died"
    purchased = "purchased"


class StorageRoutes:
    def __init__(self, api_dependencies: ApiDependencies):
        self.router = APIRouter()
        self.settings = Settings()
        self.crud_components = CRUDComponents()

        @self.router.put("/")
        async def initial_store():
            return {"starting ": "starting"}

        @self.router.put("/create", status_code=HTTPStatus.CREATED,
                         response_model=Union[HDDDataBase, CPUDataBase, SSDDataBase])
        async def add_hdd(*, obj_in: Union[HDDDataCreate, SSDDataCreate, CPUDataCreate],
                          db: Session = Depends(api_dependencies.get_db)) -> dict:
            """
            Create a new storage record in the database.
            """

            obj_create, flag_storage_type= _check_initial_creation(obj_in=obj_in)

            return self.crud_components.storage_data.create_or_update(db=db, obj_in=obj_create,
                                                                  storage_type=flag_storage_type)

        @self.router.put("/{process_type}/{number_of_items}")
        async def process_storage(*, process_type, number_of_items: int,
                                  obj_in: Union[HDDDataCreate, SSDDataCreate, CPUDataCreate],
                                  db: Session = Depends(api_dependencies.get_db)):

            obj_create, flag_storage_type = _check_initial_creation(obj_in=obj_in)
            try:
                AvailableProcesses[process_type]
            except:
                raise KeyError("Only available methods")

            model = StorageModels[flag_storage_type].value
            obj_in_db = self.crud_components.storage_data.get_by_name(db, name=obj_create.name,
                                                                  storage_model=model)

            if not obj_in_db:
                return {"Cannot perform action"}


            db_model = _create_object_from_db_parameters(flag_storage_type, obj_in_db)

            method_to_process = db_model.__getattribute__(process_type)
            method_to_process(number_of_items)

            schema_object_for_db = _get_updated_schema_obj(db_model, flag_storage_type)
            print(schema_object_for_db)

            return self.crud_components.storage_data.update(db, db_obj=obj_in_db, obj_in=schema_object_for_db)



        def _get_updated_schema_obj(db_model, flag_storage_type):
            if flag_storage_type == "hdd":
                created_obj = HDDDataCreate(
                    name=db_model.name,
                    manufacturer=db_model.manufacturer,
                    total=db_model.total,
                    allocated=db_model.allocated,
                    capacity_gb=db_model.capacity_gb,
                    size=db_model.size,
                    rpm=db_model.rpm
                )
                return created_obj

            elif flag_storage_type == "cpu":
                created_obj = CPUDataCreate(
                    name=db_model.name,
                    manufacturer=db_model.manufacturer,
                    total=db_model.total,
                    allocated=db_model.allocated,
                    cores=db_model.cores,
                    socket=db_model.socket,
                    power_watts=db_model.power_watts
                )
                return created_obj
            else:
                created_obj = SSDDataCreate(
                    name=db_model.name,
                    manufacturer=db_model.manufacturer,
                    total=db_model.total,
                    allocated=db_model.allocated,
                    capacity_gb=db_model.capacity_gb,
                    interface=db_model.interface
                )
                return created_obj

        def _create_object_from_db_parameters(storage_type, db_model_parameters):
            if storage_type == "cpu":
                cpu = CPU(name=db_model_parameters.name,
                          manufacturer=db_model_parameters.manufacturer,
                          total=db_model_parameters.total,
                          allocated=db_model_parameters.allocated,
                          cores=db_model_parameters.cores,
                          socket=db_model_parameters.socket,
                          power_watts=db_model_parameters.power_watts)
                return cpu

            elif storage_type == "hdd":
                hdd = HDD(name=db_model_parameters.name,
                          manufacturer=db_model_parameters.manufacturer,
                          total=db_model_parameters.total,
                          allocated=db_model_parameters.allocated,
                          capacity_gb=db_model_parameters.capacity_gb,
                          size=db_model_parameters.size,
                          rpm=db_model_parameters.rpm)
                return hdd

            else:
                ssd = SSD(name=db_model_parameters.name,
                          manufacturer=db_model_parameters.manufacturer,
                          total=db_model_parameters.total,
                          allocated=db_model_parameters.allocated,
                          capacity_gb=db_model_parameters.capacity_gb,
                          interface=db_model_parameters.interface)
                return ssd

        def _check_initial_creation(obj_in):

            if isinstance(obj_in, HDDDataCreate):
                flag_storage_type = "hdd"
                keys = Settings().HDD_KEYS
                hdd_in = obj_in.dict()
                hdd_in_check = {key: hdd_in[key] for key in keys}
                hdd_in_db = HDD(**hdd_in_check)

                if not hdd_in_db:
                    raise ValueError("Check up the types of the parameters")
                obj_create = HDDDataCreate(**hdd_in)
                return obj_create, flag_storage_type


            elif isinstance(obj_in, SSDDataCreate):
                flag_storage_type = "ssd"
                keys = Settings().SSD_KEYS
                ssd_in = obj_in.dict()
                ssd_in_check = {key: ssd_in[key] for key in keys}
                ssd_in_db = SSD(**ssd_in_check)

                if not ssd_in_db:
                    raise ValueError("Check up the types of the parameters")
                obj_create = SSDDataCreate(**ssd_in)
                return obj_create, flag_storage_type

            elif isinstance(obj_in, CPUDataCreate):
                flag_storage_type = "cpu"
                keys = Settings().CPU_KEYS
                cpu_in = obj_in.dict()
                cpu_in_check = {key: cpu_in[key] for key in keys}
                cpu_in_db = CPU(**cpu_in_check)

                if not cpu_in_db:
                    raise ValueError("Check up the types of the parameters")
                obj_create = CPUDataCreate(**cpu_in)
                return obj_create, flag_storage_type

            else:
                return {"NON-VALID TYPE": "CHECK THE AVAILABLE MODELS"}
