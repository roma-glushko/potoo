import typer

from potoo.config import Config
from potoo.containers import Container

app = typer.Typer()

db_cli = typer.Typer()
app.add_typer(db_cli, name="db")


@db_cli.command("init")
def init_database() -> None:
    container = Container()
    container.config.from_pydantic(Config())

    container.db().init_database()


__all__ = ("app",)
