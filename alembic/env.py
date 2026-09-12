from dotenv import load_dotenv
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.database.base import Base
from app import models


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# Alembic Config
# --------------------------------------------------

config = context.config


# --------------------------------------------------
# Database URL
# --------------------------------------------------

database_url = os.getenv("DATABASE_URL")

if database_url:
    config.set_main_option(
        "sqlalchemy.url",
        database_url
    )


# --------------------------------------------------
# Logging configuration
# --------------------------------------------------

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# --------------------------------------------------
# SQLAlchemy metadata
# --------------------------------------------------

# Importing app.models loads all SQLAlchemy models:
#
# User
# Asset
# Network
# Subnet
# Attack
# Detection
# Risk
# Incident
#
# This allows Alembic to detect changes to all models.

target_metadata = Base.metadata


# --------------------------------------------------
# Offline migrations
# --------------------------------------------------

def run_migrations_offline() -> None:
    """
    Run migrations in offline mode.

    Offline mode generates SQL without creating
    a live database connection.
    """

    url = config.get_main_option(
        "sqlalchemy.url"
    )

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named"
        },
    )

    with context.begin_transaction():
        context.run_migrations()


# --------------------------------------------------
# Online migrations
# --------------------------------------------------

def run_migrations_online() -> None:
    """
    Run migrations in online mode.

    This creates a database connection and applies
    migrations directly to the database.
    """

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL environment variable is not set."
        )

    config.set_main_option(
        "sqlalchemy.url",
        database_url
    )

    connectable = engine_from_config(
        config.get_section(
            config.config_ini_section,
            {}
        ),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# --------------------------------------------------
# Run migration
# --------------------------------------------------

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()