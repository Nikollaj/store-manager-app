"""create hdd table

Revision ID: 02a17b1b2105
Revises: 
Create Date: 2023-02-13 11:36:00.325317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02a17b1b2105'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('hdd_storage',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False, primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('manufacturer', sa.String(), nullable=False),
                    sa.Column('total', sa.Integer(), nullable=False),
                    sa.Column('allocated', sa.Integer(), nullable=False),
                    sa.Column('capacity_db', sa.Integer(), nullable=False),
                    sa.Column('size', sa.String(), nullable=False),
                    sa.Column('rpm', sa.Integer(), nullable=False)
                    )


def downgrade():
    op.drop_table('hdd_storage')
