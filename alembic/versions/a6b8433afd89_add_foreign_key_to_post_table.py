"""add foreign key to post table

Revision ID: a6b8433afd89
Revises: 31fde4802012
Create Date: 2024-06-06 06:53:08.669353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6b8433afd89'
down_revision: Union[str, None] = '31fde4802012'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column('posts',sa.Column('owner_id', sa.Integer(),nullable= False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')



def downgrade() -> None:
    
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts',"owner_id")
