"""change column

Revision ID: e699526355b2
Revises: c3ab9b3fc016
Create Date: 2024-05-27 01:34:26.742227

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e699526355b2'
down_revision: Union[str, None] = 'c3ab9b3fc016'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'email')
    op.drop_column('students', 'birthday')
    op.drop_column('students', 'enrolled_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('enrolled_date', sa.DATETIME(), nullable=True))
    op.add_column('students', sa.Column('birthday', sa.DATETIME(), nullable=True))
    op.add_column('students', sa.Column('email', sa.VARCHAR(length=55), nullable=True))
    # ### end Alembic commands ###
