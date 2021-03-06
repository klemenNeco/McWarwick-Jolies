"""empty message

Revision ID: fd143339f58a
Revises: e82be3c52211
Create Date: 2021-02-12 18:19:32.179792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd143339f58a'
down_revision = 'e82be3c52211'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vrednosti', schema=None) as batch_op:
        batch_op.alter_column('naziv',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('vrednost',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vrednosti', schema=None) as batch_op:
        batch_op.alter_column('vrednost',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('naziv',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)

    # ### end Alembic commands ###
