import logging


def init_logging() -> None:
    logging.basicConfig(
        format='[%(levelname)s] - %(asctime)s - %(name)s::%(funcName)s() - %(message)s',
        level=logging.DEBUG,
    )
