"""initial

Revision ID: b8294209135a
Revises:
Create Date: 2024-02-01 15:30:58.222865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8294209135a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('rating', sa.Integer(), nullable=True),
                    sa.Column('registered', sa.Date(), nullable=True),
                    sa.PrimaryKeyConstraint('user_id'),
                    sa.UniqueConstraint('user_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
