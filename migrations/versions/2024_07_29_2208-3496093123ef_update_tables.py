"""update tables

Revision ID: 3496093123ef
Revises: 8f3ff504f6e5
Create Date: 2024-07-29 22:08:32.035235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3496093123ef'
down_revision: Union[str, None] = '8f3ff504f6e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('payment_id', sa.String(), nullable=True))
    op.drop_column('payment', 'descriptions')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('descriptions', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('payment', 'payment_id')
    # ### end Alembic commands ###