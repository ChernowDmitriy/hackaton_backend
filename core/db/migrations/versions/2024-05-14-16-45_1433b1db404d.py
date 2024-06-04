"""empty message

Revision ID: 1433b1db404d
Revises: c453fe1473fc
Create Date: 2024-05-14 16:45:59.428551

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "1433b1db404d"
down_revision = "c453fe1473fc"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "databoolean",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("param_id", sa.BIGINT(), nullable=False),
        sa.Column("borehole_id", sa.BIGINT(), nullable=False),
        sa.Column("source_time", sa.DateTime(), nullable=False),
        sa.Column("server_time", sa.DateTime(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("source_id", sa.BIGINT(), nullable=True),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.Column(
            "modify_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="main",
    )
    op.create_table(
        "datainteger",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("param_id", sa.BIGINT(), nullable=False),
        sa.Column("borehole_id", sa.BIGINT(), nullable=False),
        sa.Column("source_time", sa.DateTime(), nullable=False),
        sa.Column("server_time", sa.DateTime(), nullable=False),
        sa.Column("value", sa.BIGINT(), nullable=False),
        sa.Column("source_id", sa.BIGINT(), nullable=True),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.Column(
            "modify_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="main",
    )
    op.create_table(
        "datatext",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("param_id", sa.BIGINT(), nullable=False),
        sa.Column("borehole_id", sa.BIGINT(), nullable=False),
        sa.Column("source_time", sa.DateTime(), nullable=False),
        sa.Column("server_time", sa.DateTime(), nullable=False),
        sa.Column("value", sa.String(), nullable=False),
        sa.Column("source_id", sa.BIGINT(), nullable=True),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.Column(
            "modify_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="main",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("datatext", schema="main")
    op.drop_table("datainteger", schema="main")
    op.drop_table("databoolean", schema="main")
    # ### end Alembic commands ###
