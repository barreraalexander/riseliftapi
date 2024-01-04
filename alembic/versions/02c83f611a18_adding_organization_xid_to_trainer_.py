"""adding organization_xid to trainer_profile

Revision ID: 02c83f611a18
Revises: 7a7666660192
Create Date: 2024-01-03 12:46:20.692315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02c83f611a18'
down_revision: Union[str, None] = '7a7666660192'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trainer_profile', sa.Column('organization_xid', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'trainer_profile', 'organization', ['organization_xid'], ['xid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'trainer_profile', type_='foreignkey')
    op.drop_column('trainer_profile', 'organization_xid')
    # ### end Alembic commands ###