"""create users table

Revision ID: 31fde4802012
Revises: 2ba87b76b598
Create Date: 2024-06-06 06:45:15.593491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31fde4802012'
down_revision: Union[str, None] = '2ba87b76b598'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table('users',
                    sa.Column('id', sa.Integer(),nullable= False), 
                    sa.Column('email', sa.String(),nullable= False),
                    sa.Column('password', sa.String(),nullable= False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable= False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))



def downgrade() -> None:
    
    op.drop_table('users')
