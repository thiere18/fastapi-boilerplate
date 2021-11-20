"""adding usrname column

Revision ID: 175f5441bd46
Revises: 186abcf43cae
Create Date: 2021-11-20 22:54:04.157131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '175f5441bd46'
down_revision = '186abcf43cae'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('username', sa.String(255),nullable=False)
    )
    pass


def downgrade():
    pass
