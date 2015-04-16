"""empty message

Revision ID: 3788c538b024
Revises: 362e3617dccf
Create Date: 2015-04-15 22:54:30.946459

"""

# revision identifiers, used by Alembic.
revision = '3788c538b024'
down_revision = '362e3617dccf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tile_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_captured', sa.DateTime(), nullable=True),
    sa.Column('session_id', sa.String(), nullable=False),
    sa.Column('level', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tile_classification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification', sa.Integer(), nullable=False),
    sa.Column('date_classified', sa.DateTime(), nullable=True),
    sa.Column('tile', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['tile'], ['tile.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tile', 'session_id', name='one_classification_per_tile')
    )
    op.add_column(u'tile', sa.Column('classifications_count', sa.Integer(), nullable=True))
    op.add_column(u'tile', sa.Column('classifications_majority_agreement', sa.Integer(), nullable=True))
    op.add_column(u'tile', sa.Column('classifications_majority_class', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'tile', 'classifications_majority_class')
    op.drop_column(u'tile', 'classifications_majority_agreement')
    op.drop_column(u'tile', 'classifications_count')
    op.drop_table('tile_classification')
    op.drop_table('tile_user')
    ### end Alembic commands ###