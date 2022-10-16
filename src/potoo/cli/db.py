import logging

import typer

from potoo.config import Config
from potoo.containers import Runtime
from potoo.logger import init_logger

db_cli = typer.Typer()

logger = logging.getLogger(__name__)


@db_cli.command("init")
def init_database() -> None:
    """
    Init Potoo database
    """
    runtime = Runtime()
    runtime.config.from_pydantic(Config())
    init_logger(log_level=runtime.config.log_level())

    runtime.db().init_database()
    logger.info("Database has been initialized ✅")