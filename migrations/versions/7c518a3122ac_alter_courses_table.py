"""Alter courses table

Revision ID: 7c518a3122ac
Revises: e9a00cabad0c
Create Date: 2023-12-17 01:56:50.538853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c518a3122ac'
down_revision: Union[str, None] = 'e9a00cabad0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('image', sa.VARCHAR(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('courses', 'image')
    # ### end Alembic commands ###
