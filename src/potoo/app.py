from potoo.containers import Container


def create_app() -> None:
    container = Container()

    container.db().create_database()
