"""empty message

Revision ID: 24d86a6b9a4c
Revises: None
Create Date: 2015-02-18 16:43:44.823142

"""

# revision identifiers, used by Alembic.
revision = '24d86a6b9a4c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('first', sa.String(), nullable=False),
    sa.Column('last', sa.String(), nullable=False),
    sa.Column('organization', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('attempts', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('email_verification_token', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lon', sa.Float(), nullable=False),
    sa.Column('country', sa.Integer(), nullable=True),
    sa.Column('continent', sa.String(), nullable=True),
    sa.Column('field', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_edited', sa.DateTime(), nullable=True),
    sa.Column('use_verification', sa.Boolean(), nullable=True),
    sa.Column('use_valid', sa.Boolean(), nullable=True),
    sa.Column('use_deleted', sa.Boolean(), nullable=True),
    sa.CheckConstraint(u'lat Between -90 and 90', name='lat_bounds'),
    sa.CheckConstraint(u'lon Between -180 and 180', name='lon_bounds'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('lat', 'lon', name='one_location_at_each_lat_lon_pair')
    )
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('protected', sa.Boolean(), nullable=True),
    sa.Column('validation', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('land_use_type', sa.Integer(), nullable=True),
    sa.Column('intensity', sa.Integer(), nullable=True),
    sa.Column('water', sa.Integer(), nullable=True),
    sa.Column('crop_primary', sa.Integer(), nullable=True),
    sa.Column('crop_secondary', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('year', 'location_id', 'month', name='one_year_per_location')
    )
    op.create_index(op.f('ix_record_location_id'), 'record', ['location_id'], unique=False)
    op.create_index(op.f('ix_record_month'), 'record', ['month'], unique=False)
    op.create_index(op.f('ix_record_year'), 'record', ['year'], unique=False)
    op.create_table('timeseries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('series', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('date_acquired', sa.Date(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_timeseries_date_acquired'), 'timeseries', ['date_acquired'], unique=False)
    op.create_index(op.f('ix_timeseries_series'), 'timeseries', ['series'], unique=False)
    op.create_table('photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('date_taken', sa.DateTime(), nullable=False),
    sa.Column('comments', sa.String(), nullable=True),
    sa.Column('date_uploaded', sa.DateTime(), nullable=True),
    sa.Column('flagged', sa.Integer(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_photo_location_id'), 'photo', ['location_id'], unique=False)
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('last_read', sa.DateTime(), nullable=True),
    sa.Column('read', sa.Boolean(), nullable=True),
    sa.Column('subject', sa.String(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('record_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['record_id'], ['record.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_read'), 'notification', ['read'], unique=False)
    op.create_index(op.f('ix_notification_user_id'), 'notification', ['user_id'], unique=False)
    op.create_table('record_rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('record_id', sa.Integer(), nullable=False),
    sa.Column('date_rated', sa.DateTime(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('stale', sa.BOOLEAN(), nullable=True),
    sa.ForeignKeyConstraint(['record_id'], ['record.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'record_id', name='one_rating_per_record_per_user')
    )
    op.create_index(op.f('ix_record_rating_record_id'), 'record_rating', ['record_id'], unique=False)
    op.create_table('record_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('record_id', sa.Integer(), nullable=False),
    sa.Column('date_edited', sa.DateTime(), nullable=True),
    sa.Column('data', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['record_id'], ['record.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_record_history_record_id'), 'record_history', ['record_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_record_history_record_id'), table_name='record_history')
    op.drop_table('record_history')
    op.drop_index(op.f('ix_record_rating_record_id'), table_name='record_rating')
    op.drop_table('record_rating')
    op.drop_index(op.f('ix_notification_user_id'), table_name='notification')
    op.drop_index(op.f('ix_notification_read'), table_name='notification')
    op.drop_table('notification')
    op.drop_index(op.f('ix_photo_location_id'), table_name='photo')
    op.drop_table('photo')
    op.drop_index(op.f('ix_timeseries_series'), table_name='timeseries')
    op.drop_index(op.f('ix_timeseries_date_acquired'), table_name='timeseries')
    op.drop_table('timeseries')
    op.drop_index(op.f('ix_record_year'), table_name='record')
    op.drop_index(op.f('ix_record_month'), table_name='record')
    op.drop_index(op.f('ix_record_location_id'), table_name='record')
    op.drop_table('record')
    op.drop_table('location')
    op.drop_table('user')
    ### end Alembic commands ###