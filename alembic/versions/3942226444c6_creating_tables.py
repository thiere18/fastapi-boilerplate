"""creating tables

Revision ID: 3942226444c6
Revises: 
Create Date: 2021-11-20 22:34:33.378654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3942226444c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    )
  
  
    
    pass


def downgrade():
    pass
