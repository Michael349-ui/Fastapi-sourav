"""add last columns to posts

Revision ID: 1b86a37accce
Revises: a6b8433afd89
Create Date: 2024-06-06 06:57:28.578102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b86a37accce'
down_revision: Union[str, None] = 'a6b8433afd89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column('posts',sa.Column('published', sa.Boolean(),nullable= False, server_default= 'True'))
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True),nullable= False, server_default= sa.text('NOW()')))



def downgrade() -> None:

    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
