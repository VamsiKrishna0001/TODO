"""added owner id in todos

Revision ID: 9c13a30e9ba4
Revises: 
Create Date: 2025-07-20 14:15:52.825723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c13a30e9ba4'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('todos', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'fk_todos_owner_id_users',
        source_table='todos',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_todos_owner_id_users', 'todos', type_='foreignkey')
    op.drop_column('todos', 'owner_id')
    pass
