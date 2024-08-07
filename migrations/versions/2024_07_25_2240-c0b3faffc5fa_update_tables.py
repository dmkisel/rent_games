"""update tables

Revision ID: c0b3faffc5fa
Revises: 4d1db2c069c7
Create Date: 2024-07-25 22:40:22.978368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0b3faffc5fa'
down_revision: Union[str, None] = '4d1db2c069c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('confirmation_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payment', 'confirmation_url')
    # ### end Alembic commands ###
