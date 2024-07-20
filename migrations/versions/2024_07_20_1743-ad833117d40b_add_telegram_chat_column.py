"""add telegram chat column

Revision ID: ad833117d40b
Revises: 1945fcec8978
Create Date: 2024-07-20 17:43:53.481225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad833117d40b'
down_revision: Union[str, None] = '1945fcec8978'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('chat_telegram', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'user', ['chat_telegram'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'chat_telegram')
    # ### end Alembic commands ###
