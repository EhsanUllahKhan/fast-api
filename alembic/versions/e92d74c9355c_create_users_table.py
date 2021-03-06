"""create users table

Revision ID: e92d74c9355c
Revises: 
Create Date: 2021-03-21 17:40:17.665025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e92d74c9355c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=20), nullable=True),
                    sa.Column('password', sa.String(length=20), nullable=True),
                    sa.PrimaryKeyConstraint('user_id')
                    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_user_id'), 'users',
                    ['user_id'], unique=False)
    op.create_table('lost_items',
                    sa.Column('lost_item_id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=20), nullable=True),
                    sa.Column('description', sa.String(
                        length=50), nullable=True),
                    sa.Column('lost_lattitude', sa.Float(), nullable=True),
                    sa.Column('lost_longitude', sa.Float(), nullable=True),
                    sa.Column('lost_date', sa.Date(), nullable=True),
                    sa.Column('is_found', sa.Boolean(), nullable=True),
                    sa.Column('picture', sa.String(length=200), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
                    sa.PrimaryKeyConstraint('lost_item_id')
                    )
    op.create_index(op.f('ix_lost_items_lost_item_id'),
                    'lost_items', ['lost_item_id'], unique=False)
    op.create_table('found_items',
                    sa.Column('foundItem_id', sa.Integer(), nullable=False),
                    sa.Column('found_lattitude', sa.Float(), nullable=True),
                    sa.Column('found_longitude', sa.Float(), nullable=True),
                    sa.Column('found_date', sa.Date(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('lost_item_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['lost_item_id'], ['lost_items.lost_item_id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
                    sa.PrimaryKeyConstraint('foundItem_id')
                    )
    op.create_index(op.f('ix_found_items_foundItem_id'),
                    'found_items', ['foundItem_id'], unique=False)
    op.create_table('item_pictures',
                    sa.Column('pictures_id', sa.Integer(), nullable=False),
                    sa.Column('lost_item_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['lost_item_id'], ['lost_items.lost_item_id'], ),
                    sa.PrimaryKeyConstraint('pictures_id')
                    )
    op.create_index(op.f('ix_item_pictures_pictures_id'),
                    'item_pictures', ['pictures_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_pictures_pictures_id'),
                  table_name='item_pictures')
    op.drop_table('item_pictures')
    op.drop_index(op.f('ix_found_items_foundItem_id'),
                  table_name='found_items')
    op.drop_table('found_items')
    op.drop_index(op.f('ix_lost_items_lost_item_id'), table_name='lost_items')
    op.drop_table('lost_items')
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
