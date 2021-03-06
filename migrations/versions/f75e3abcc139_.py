"""empty message

Revision ID: f75e3abcc139
Revises: 
Create Date: 2021-01-09 15:32:46.834434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f75e3abcc139'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uporabniki',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('uporabnisko_ime', sa.String(length=50), nullable=False),
    sa.Column('e_naslov', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('uporabniki', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_uporabniki_e_naslov'), ['e_naslov'], unique=False)
        batch_op.create_index(batch_op.f('ix_uporabniki_uporabnisko_ime'), ['uporabnisko_ime'], unique=False)

    op.create_table('kategorije',
    sa.Column('id_kategorije', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('ime_kategorije', sa.String(length=50), nullable=False),
    sa.Column('id_uporabnika', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['id_uporabnika'], ['uporabniki.id'], ),
    sa.PrimaryKeyConstraint('id_kategorije')
    )
    with op.batch_alter_table('kategorije', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_kategorije_ime_kategorije'), ['ime_kategorije'], unique=False)

    op.create_table('vrednosti',
    sa.Column('id_vrednosti', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('naziv', sa.String(length=50), nullable=False),
    sa.Column('vrednost', sa.String(length=50), nullable=False),
    sa.Column('id_kategorije', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['id_kategorije'], ['kategorije.id_kategorije'], ),
    sa.PrimaryKeyConstraint('id_vrednosti')
    )
    with op.batch_alter_table('vrednosti', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_vrednosti_naziv'), ['naziv'], unique=False)
        batch_op.create_index(batch_op.f('ix_vrednosti_vrednost'), ['vrednost'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vrednosti', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_vrednosti_vrednost'))
        batch_op.drop_index(batch_op.f('ix_vrednosti_naziv'))

    op.drop_table('vrednosti')
    with op.batch_alter_table('kategorije', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_kategorije_ime_kategorije'))

    op.drop_table('kategorije')
    with op.batch_alter_table('uporabniki', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_uporabniki_uporabnisko_ime'))
        batch_op.drop_index(batch_op.f('ix_uporabniki_e_naslov'))

    op.drop_table('uporabniki')
    # ### end Alembic commands ###
