"""create phone in users

Revision ID: 93d004dc2fcc
Revises: 9c13a30e9ba4
Create Date: 2025-07-20 14:30:50.415167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93d004dc2fcc'
down_revision: Union[str, Sequence[str], None] = '9c13a30e9ba4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
    pass
