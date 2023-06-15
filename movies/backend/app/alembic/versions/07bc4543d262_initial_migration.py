"""Initial migration

Revision ID: 07bc4543d262
Revises: 
Create Date: 2023-06-13 20:36:37.047924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07bc4543d262'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_description'), 'movie', ['description'], unique=False)
    op.create_index(op.f('ix_movie_id'), 'movie', ['id'], unique=False)
    op.create_index(op.f('ix_movie_title'), 'movie', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_movie_title'), table_name='movie')
    op.drop_index(op.f('ix_movie_id'), table_name='movie')
    op.drop_index(op.f('ix_movie_description'), table_name='movie')
    op.drop_table('movie')
    # ### end Alembic commands ###