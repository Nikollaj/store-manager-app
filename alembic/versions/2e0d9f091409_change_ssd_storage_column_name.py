"""change ssd_storage column name

Revision ID: 2e0d9f091409
Revises: 54a6e577cb48
Create Date: 2023-02-14 15:54:25.950684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e0d9f091409'
down_revision = '54a6e577cb48'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('ssd_storage', 'capacity_db', nullable=False, new_column_name='capacity_gb')


def downgrade():
    pass
