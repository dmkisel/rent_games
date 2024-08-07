"""fix cat model

Revision ID: be33c343f416
Revises: 6735928cd4e6
Create Date: 2024-07-22 22:50:57.548897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be33c343f416'
down_revision: Union[str, None] = '6735928cd4e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'is_active')
    # ### end Alembic commands ###
