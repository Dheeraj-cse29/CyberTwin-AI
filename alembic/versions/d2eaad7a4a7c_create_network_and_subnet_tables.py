"""create network and subnet tables

Revision ID: d2eaad7a4a7c
Revises: 61fbac3100e0
Create Date: 2026-07-27 13:53:13.499087

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd2eaad7a4a7c'
down_revision: Union[str, Sequence[str], None] = '61fbac3100e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "networks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("description", sa.String(255), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["owner_id"], ["users.id"]),
    )

    op.create_index(
        op.f("ix_networks_id"),
        "networks",
        ["id"],
        unique=False,
    )

    op.create_table(
        "subnets",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("cidr_block", sa.String(50), nullable=False),
        sa.Column("network_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["network_id"], ["networks.id"]),
    )

    op.create_index(
        op.f("ix_subnets_id"),
        "subnets",
        ["id"],
        unique=False,
    )

def downgrade() -> None:
    op.drop_index(op.f("ix_subnets_id"), table_name="subnets")
    op.drop_table("subnets")

    op.drop_index(op.f("ix_networks_id"), table_name="networks")
    op.drop_table("networks")
