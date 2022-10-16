import logging


def init_logger() -> None:
    logging.basicConfig(
        format='[%(levelname)s] - %(asctime)s - %(name)s::%(funcName)s() - %(message)s',
        level=logging.DEBUG,
    )
