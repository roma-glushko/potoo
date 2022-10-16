import logging

import typer

from potoo.config import Config
from potoo.containers import Runtime
from potoo.logger import init_logger

promo_cli = typer.Typer()

logger = logging.getLogger(__name__)


@promo_cli.command("add")
def add_promo_user(username: str) -> None:
    """
    Add a new user to promote
    """
    runtime = Runtime()
    runtime.config.from_pydantic(Config())
    init_logger(log_level=runtime.config.log_level())

    promo_user = runtime.promo_user_service().add_promo_user(username)

    logger.info(
        f"Promo user {username} has been added ✅",
        extra={"id": promo_user.id, "user_id": promo_user.user_id},
    )
