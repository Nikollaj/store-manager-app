"""change hdd_storage column name

Revision ID: 54a6e577cb48
Revises: 1769b7e29898
Create Date: 2023-02-13 15:17:31.196153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54a6e577cb48'
down_revision = '1769b7e29898'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('hdd_storage', 'capacity_db', nullable=False, new_column_name='capacity_gb')


def downgrade():
    pass
