"""add content column

Revision ID: 2ba87b76b598
Revises: 46f32c24ac48
Create Date: 2024-06-06 06:26:31.909890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ba87b76b598'
down_revision: Union[str, None] = '46f32c24ac48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column('posts',sa.Column('content', sa.String(),nullable= False))


def downgrade() -> None:
    
    op.drop_column('content')
