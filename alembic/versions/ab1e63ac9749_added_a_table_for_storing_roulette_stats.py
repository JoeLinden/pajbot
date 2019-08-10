"""Added a table for storing roulette stats

Revision ID: ab1e63ac9749
Revises: 00f5c41335a5
Create Date: 2016-03-13 20:11:43.089025

"""

# revision identifiers, used by Alembic.
revision = "ab1e63ac9749"
down_revision = "00f5c41335a5"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tb_roulette",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("points", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_tb_roulette_user_id"), "tb_roulette", ["user_id"], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tb_roulette_user_id"), table_name="tb_roulette")
    op.drop_table("tb_roulette")
    ### end Alembic commands ###
