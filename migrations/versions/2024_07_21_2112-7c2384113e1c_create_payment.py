"""create payment

Revision ID: 7c2384113e1c
Revises: 37c0ce24dca5
Create Date: 2024-07-21 21:12:29.920265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c2384113e1c'
down_revision: Union[str, None] = '37c0ce24dca5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('cart_id', sa.Integer(), nullable=False))
    op.add_column('payment', sa.Column('amount', sa.Float(), nullable=False))
    op.drop_constraint('payment_user_id_fkey', 'payment', type_='foreignkey')
    op.create_foreign_key(None, 'payment', 'user', ['cart_id'], ['id'])
    op.drop_column('payment', 'user_id')
    op.drop_column('payment', 'summ')
    op.drop_column('payment', 'currency')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('currency', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('payment', sa.Column('summ', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.add_column('payment', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'payment', type_='foreignkey')
    op.create_foreign_key('payment_user_id_fkey', 'payment', 'user', ['user_id'], ['id'])
    op.drop_column('payment', 'amount')
    op.drop_column('payment', 'cart_id')
    # ### end Alembic commands ###
