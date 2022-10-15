from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session


SessionFactory = Callable[..., AbstractContextManager[Session]]