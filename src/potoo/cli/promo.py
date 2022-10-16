import logging

import typer

from potoo.config import Config
from potoo.containers import Container

promo_cli = typer.Typer()

logger = logging.getLogger(__name__)


@promo_cli.command("add")
def add_promo_user(user_id: str) -> None:
    """
    Add a new user to promote
    """
    container = Container()
    container.config.from_pydantic(Config())

    promo_user = container.promo_user_repository().add(user_id)

    if promo_user:
        logger.info(f"Promo user {user_id} has been added", extra={"id": promo_user.id})