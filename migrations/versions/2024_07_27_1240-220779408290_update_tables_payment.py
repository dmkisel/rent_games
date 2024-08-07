"""update tables payment

Revision ID: 220779408290
Revises: e566289ce4d1
Create Date: 2024-07-27 12:40:02.036078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '220779408290'
down_revision: Union[str, None] = 'e566289ce4d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payment', 'payment_id')
    op.drop_column('payment', 'amount')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.add_column('payment', sa.Column('payment_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
