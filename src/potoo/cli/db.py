import typer

from potoo.config import Config
from potoo.containers import Container

db_cli = typer.Typer()


@db_cli.command("init")
def init_database() -> None:
    container = Container()
    container.config.from_pydantic(Config())

    container.db().init_database()
