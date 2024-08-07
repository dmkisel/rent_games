"""create orders

Revision ID: 4f994c27f9da
Revises: be33c343f416
Create Date: 2024-07-24 15:59:24.194288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4f994c27f9da'
down_revision: Union[str, None] = 'be33c343f416'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('contain', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('type_orders', sa.Integer(), nullable=True),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['type_orders'], ['type_price.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.add_column('payment', sa.Column('order_id', sa.Integer(), nullable=False))
    op.drop_constraint('payment_cart_id_fkey', 'payment', type_='foreignkey')
    op.create_foreign_key(None, 'payment', 'order', ['order_id'], ['id'])
    op.drop_column('payment', 'cart_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('cart_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'payment', type_='foreignkey')
    op.create_foreign_key('payment_cart_id_fkey', 'payment', 'user', ['cart_id'], ['id'])
    op.drop_column('payment', 'order_id')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_table('order')
    # ### end Alembic commands ###
