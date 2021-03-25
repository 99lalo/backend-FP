"""empty message

Revision ID: 5e804a2597db
Revises: e6739be72fa2
Create Date: 2021-03-24 22:09:51.762705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e804a2597db'
down_revision = 'e6739be72fa2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite_list', sa.Column('game_image', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('favorite_list', 'game_image')
    # ### end Alembic commands ###
