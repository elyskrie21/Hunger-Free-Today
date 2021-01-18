"""empty message

Revision ID: 6b8e50b787e6
Revises: 37cf883db607
Create Date: 2021-01-17 19:53:38.794637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b8e50b787e6'
down_revision = '37cf883db607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('bought_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('food_pantry', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('bought_item', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_bought_item_food_pantry'), ['food_pantry'], unique=False)
        batch_op.create_index(batch_op.f('ix_bought_item_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_bought_item_price'), ['price'], unique=False)
        batch_op.create_index(batch_op.f('ix_bought_item_quantity'), ['quantity'], unique=False)

    op.create_table('requested_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('requested_item', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_requested_item_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_requested_item_image'), ['image'], unique=False)
        batch_op.create_index(batch_op.f('ix_requested_item_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_requested_item_price'), ['price'], unique=False)
        batch_op.create_index(batch_op.f('ix_requested_item_quantity'), ['quantity'], unique=False)

    op.create_table('user_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('store_type', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('zip_code', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_data', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_data_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_data_phone'), ['phone'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_data_state'), ['state'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_data_store_type'), ['store_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_data_zip_code'), ['zip_code'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_data', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_data_zip_code'))
        batch_op.drop_index(batch_op.f('ix_user_data_store_type'))
        batch_op.drop_index(batch_op.f('ix_user_data_state'))
        batch_op.drop_index(batch_op.f('ix_user_data_phone'))
        batch_op.drop_index(batch_op.f('ix_user_data_name'))

    op.drop_table('user_data')
    with op.batch_alter_table('requested_item', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_requested_item_quantity'))
        batch_op.drop_index(batch_op.f('ix_requested_item_price'))
        batch_op.drop_index(batch_op.f('ix_requested_item_name'))
        batch_op.drop_index(batch_op.f('ix_requested_item_image'))
        batch_op.drop_index(batch_op.f('ix_requested_item_description'))

    op.drop_table('requested_item')
    with op.batch_alter_table('bought_item', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_bought_item_quantity'))
        batch_op.drop_index(batch_op.f('ix_bought_item_price'))
        batch_op.drop_index(batch_op.f('ix_bought_item_name'))
        batch_op.drop_index(batch_op.f('ix_bought_item_food_pantry'))

    op.drop_table('bought_item')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###