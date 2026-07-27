"""Add Asset Enums

Revision ID: 61fbac3100e0
Revises: 9d7304ddefc3
Create Date: 2026-07-24 15:36:04.799427
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers
revision: str = "61fbac3100e0"
down_revision: Union[str, Sequence[str], None] = "9d7304ddefc3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


asset_type_enum = postgresql.ENUM(
    "Server",
    "Workstation",
    "Router",
    "Switch",
    "Firewall",
    "Database",
    "Cloud",
    name="assettype",
)

asset_status_enum = postgresql.ENUM(
    "Active",
    "Inactive",
    "Maintenance",
    "Compromised",
    name="assetstatus",
)


def upgrade():

    # Create ENUM types first
    asset_type_enum.create(op.get_bind(), checkfirst=True)
    asset_status_enum.create(op.get_bind(), checkfirst=True)

    # Convert asset_type
    op.execute("""
        ALTER TABLE assets
        ALTER COLUMN asset_type
        TYPE assettype
        USING asset_type::assettype
    """)

    # Convert status
    op.execute("""
        ALTER TABLE assets
        ALTER COLUMN status
        TYPE assetstatus
        USING status::assetstatus
    """)


def downgrade():

    # Convert back to VARCHAR
    op.execute("""
        ALTER TABLE assets
        ALTER COLUMN asset_type
        TYPE VARCHAR
        USING asset_type::text
    """)

    op.execute("""
        ALTER TABLE assets
        ALTER COLUMN status
        TYPE VARCHAR
        USING status::text
    """)

    # Drop ENUM types
    asset_type_enum.drop(op.get_bind(), checkfirst=True)
    asset_status_enum.drop(op.get_bind(), checkfirst=True)