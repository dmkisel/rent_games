"""create payments

Revision ID: 6735928cd4e6
Revises: 435e88c61022
Create Date: 2024-07-22 19:34:44.357432

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6735928cd4e6'
down_revision: Union[str, None] = '435e88c61022'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment',
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('payment_id', sa.String(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('descriptions', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('confirmation', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payment_id'), 'payment', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_payment_id'), table_name='payment')
    op.drop_table('payment')
    # ### end Alembic commands ###
