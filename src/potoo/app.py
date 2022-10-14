import typer
from potoo.containers import Container

app = typer.Typer()


@app.command()
def init_database() -> None:
    container = Container()
    container.db().create_database()


__all__ = ("app",)
