import logging

import typer

from potoo.config import Config
from potoo.containers import Runtime
from potoo.logger import init_logger

seed_cli = typer.Typer()

logger = logging.getLogger(__name__)


@seed_cli.command("add")
def add_seed_users(promo_username: str, seed_usernames: list[str]) -> None:
    """
    Add seed users to generate candidate pool based on their followers
    """
    runtime = Runtime()
    runtime.config.from_pydantic(Config())
    init_logger(log_level=runtime.config.log_level())

    candidate_service = runtime.candidate_service()
    candidate_service.add_seed_users(promo_username, seed_usernames)

    logger.info("Seed users have been added ✅")
