"""add ssd and cpu tables

Revision ID: 1769b7e29898
Revises: 02a17b1b2105
Create Date: 2023-02-13 12:52:17.452418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1769b7e29898'
down_revision = '02a17b1b2105'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('ssd_storage',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False, primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('manufacturer', sa.String(), nullable=False),
                    sa.Column('total', sa.Integer(), nullable=False),
                    sa.Column('allocated', sa.Integer(), nullable=False),
                    sa.Column('capacity_db', sa.Integer(), nullable=False),
                    sa.Column('interface', sa.String(), nullable=False),
                    )
    op.create_table('cpu_storage',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False, primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('manufacturer', sa.String(), nullable=False),
                    sa.Column('total', sa.Integer(), nullable=False),
                    sa.Column('allocated', sa.Integer(), nullable=False),
                    sa.Column('cores', sa.Integer(), nullable=False),
                    sa.Column('socket', sa.String(), nullable=False),
                    sa.Column('power_watts', sa.Integer(), nullable=False)
                    )


def downgrade():
    op.drop_table('ssd_storage')
    op.drop_table('cpu_storage')


