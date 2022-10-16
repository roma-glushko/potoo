import typer

from potoo.cli import db_cli, promo_cli, seed_cli

app = typer.Typer()

app.add_typer(db_cli, name="db")
app.add_typer(promo_cli, name="promo")
app.add_typer(seed_cli, name="seed")


__all__ = ("app",)
