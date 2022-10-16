from dotenv import load_dotenv

from potoo.app import app
from potoo.logger import init_logger

init_logger()
load_dotenv()

if __name__ == "__main__":
    app()
