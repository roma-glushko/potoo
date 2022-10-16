from dotenv import load_dotenv

from potoo.app import app
from potoo.logging import init_logging

init_logging()
load_dotenv()

if __name__ == "__main__":
    app()
