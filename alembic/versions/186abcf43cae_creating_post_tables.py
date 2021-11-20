"""creating post tables

Revision ID: 186abcf43cae
Revises: 3942226444c6
Create Date: 2021-11-20 22:44:44.618303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '186abcf43cae'
down_revision = '3942226444c6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
                        sa.Column('id', sa.Integer(), nullable=False),
                        sa.Column('title', sa.String(), nullable=False),
                        sa.Column('content', sa.String(), nullable=False),
                        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),                        
                        sa.Column('user_id',sa.Integer(), nullable=False),
                        sa.PrimaryKeyConstraint('id'),
                    )

    op.create_foreign_key('post_user_fk',source_table='posts',referent_table="users",local_cols=[
        'user_id'],remote_cols=['id'], ondelete="CASCADE")

                        
            
    pass


def downgrade():
    pass
