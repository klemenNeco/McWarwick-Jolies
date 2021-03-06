"""empty message

Revision ID: e82be3c52211
Revises: f75e3abcc139
Create Date: 2021-02-12 18:03:21.262235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e82be3c52211'
down_revision = 'f75e3abcc139'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('kategorije', schema=None) as batch_op:
        batch_op.alter_column('ime_kategorije',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('kategorije', schema=None) as batch_op:
        batch_op.alter_column('ime_kategorije',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)

    # ### end Alembic commands ###
