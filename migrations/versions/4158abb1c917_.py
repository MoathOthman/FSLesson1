"""empty message

Revision ID: 4158abb1c917
Revises: 6a815f4e98c2
Create Date: 2020-02-05 00:09:37.097560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4158abb1c917'
down_revision = '6a815f4e98c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###
