"""empty message

Revision ID: 07fe229dd548
Revises: c97aa9ccd33b
Create Date: 2017-10-01 14:53:12.382887

"""

# revision identifiers, used by Alembic.
revision = '07fe229dd548'
down_revision = 'c97aa9ccd33b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tname', sa.String(length=255), nullable=True),
    sa.Column('team_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'users', sa.Column('team_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'teams', ['team_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column(u'users', 'team_id')
    op.drop_table('teams')
    # ### end Alembic commands ###
