import sqlalchemy
from app.db.base_class import Base


class HDDData(Base):
    __tablename__ = "hdd_storage"

    id = sqlalchemy.Column('id', sqlalchemy.BigInteger(), primary_key=True, autoincrement=True, nullable=False)
    name = sqlalchemy.Column('name', sqlalchemy.String(), nullable=False)
    manufacturer = sqlalchemy.Column('manufacturer', sqlalchemy.String(), nullable=False)
    total = sqlalchemy.Column('total', sqlalchemy.Integer(), nullable=False)
    allocated = sqlalchemy.Column('allocated', sqlalchemy.Integer(), nullable=False)
    capacity_gb = sqlalchemy.Column('capacity_gb', sqlalchemy.Integer(), nullable=False)
    size = sqlalchemy.Column('size', sqlalchemy.String(), nullable=False)
    rpm = sqlalchemy.Column('rpm', sqlalchemy.Integer(), nullable=False)

    def __repr__(self):
        return (f"name = {self.name}, manufacturer = {self.manufacturer}, total = {self.total}, allocated = {self.allocated},"
              f" capacity_gb = {self.capacity_gb}, size = {self.size}, rpm = {self.rpm}")

