import logging

import typer

from potoo.config import Config
from potoo.containers import Container

seed_cli = typer.Typer()

logger = logging.getLogger(__name__)


@seed_cli.command("add")
def add_seed_users(promo_user_id: str, seed_user_ids: list[str]) -> None:
    """
    Add seed users to generate candidate pool based on their followers
    """
    container = Container()
    container.config.from_pydantic(Config())

    seed_user_repository = container.seed_user_repository()

    seed_user_repository.add(promo_user_id, seed_user_ids)

    logger.info("Seed users have been added")