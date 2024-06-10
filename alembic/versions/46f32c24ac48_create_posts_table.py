"""create posts table

Revision ID: 46f32c24ac48
Revises: 
Create Date: 2024-06-06 06:17:21.920398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46f32c24ac48'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:


    op.create_table('posts',sa.Column('id', sa.Integer(),nullable= False, primary_key= True), 
                            sa.Column('title', sa.String(),nullable= False))

    
def downgrade() -> None:

    op.drop_table('posts')