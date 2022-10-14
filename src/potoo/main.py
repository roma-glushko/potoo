from dotenv import load_dotenv
load_dotenv()

from potoo.app import create_app

if __name__ == "__main__":
    create_app()
