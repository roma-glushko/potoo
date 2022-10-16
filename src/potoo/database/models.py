from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from potoo.database.engine import BaseModel


class PromoUser(BaseModel):
    """
    Users that we need to promote via the follow rate optimization
    """

    __tablename__ = "promo_users"

    id = Column(Integer, primary_key=True, index=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    username = Column(String, unique=True, index=True)
    user_id = Column(String, unique=True, index=True)

    seeds = relationship("SeedUser")

    def __repr__(self):
        return f"<PromoUser(id='{self.id}', username='{self.username}')>"


class SeedUser(BaseModel):
    """
    Users that we assume to have content similar to promoting users.
    Hence, we use their followers to build a candidate list to follow
    """

    __tablename__ = "seed_users"

    id = Column(Integer, primary_key=True, unique=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    promo_username = Column(Integer, ForeignKey("promo_users.username"), index=True)
    username = Column(String, unique=True)
    user_id = Column(String, unique=True)

    def __repr__(self):
        return f"<SeedUser(id='{self.id}', promo_user='{self.promo_username}', username='{self.username}')>"
