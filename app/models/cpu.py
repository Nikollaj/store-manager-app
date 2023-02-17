import sqlalchemy
from app.db.base_class import Base


class CPUData(Base):
    __tablename__ = "cpu_storage"

    id = sqlalchemy.Column('id', sqlalchemy.BigInteger(), primary_key=True, autoincrement=True, nullable=False)
    name = sqlalchemy.Column('name', sqlalchemy.String(), nullable=False)
    manufacturer = sqlalchemy.Column('manufacturer', sqlalchemy.String(), nullable=False)
    total = sqlalchemy.Column('total', sqlalchemy.Integer(), nullable=False)
    allocated = sqlalchemy.Column('allocated', sqlalchemy.Integer(), nullable=False)
    cores = sqlalchemy.Column('cores', sqlalchemy.Integer(), nullable=False)
    socket = sqlalchemy.Column('socket', sqlalchemy.String(), nullable=False)
    power_watts = sqlalchemy.Column('power_watts', sqlalchemy.Integer(), nullable=False)

