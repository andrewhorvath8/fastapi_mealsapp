"""empty message

Revision ID: 95049117e202
Revises: 
Create Date: 2022-08-25 10:43:35.793656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95049117e202'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('ingredients', sa.Text(), nullable=True),
    sa.Column('spicy', sa.Boolean(), nullable=True),
    sa.Column('vegan', sa.Boolean(), nullable=True),
    sa.Column('gluten_free', sa.Boolean(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('kcal', sa.Numeric(), nullable=True),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('meals')
    # ### end Alembic commands ###