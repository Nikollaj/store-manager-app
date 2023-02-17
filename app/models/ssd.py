import sqlalchemy
from app.db.base_class import Base


class SSDData(Base):
    __tablename__ = "ssd_storage"

    id = sqlalchemy.Column('id', sqlalchemy.BigInteger(), primary_key=True, autoincrement=True, nullable=False)
    name = sqlalchemy.Column('name', sqlalchemy.String(), nullable=False)
    manufacturer = sqlalchemy.Column('manufacturer', sqlalchemy.String(), nullable=False)
    total = sqlalchemy.Column('total', sqlalchemy.Integer(), nullable=False)
    allocated = sqlalchemy.Column('allocated', sqlalchemy.Integer(), nullable=False)
    capacity_gb = sqlalchemy.Column('capacity_gb', sqlalchemy.Integer(), nullable=False)
    interface = sqlalchemy.Column('interface', sqlalchemy.String(), nullable=False)

    def __repr__(self):
        return f"id = {self.id}," \
               f" name = {self.name}," \
               f" manufacturer = {self.manufacturer}," \
               f" total = {self.total}," \
               f" allocated = {self.allocated}," \
               f" capacity_gb = {self.capacity_gb}," \
               f" interface = {self.interface}"