from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from potoo.database.engine import BaseModel


class PromoUser(BaseModel):
    """
    Users that we need to promote via the follow rate optimization
    """

    __tablename__ = "promo_users"

    id = Column(Integer, primary_key=True, index=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(String, unique=True, index=True)

    seeds = relationship("SeedUser")

    def __repr__(self):
        return f"<PromoUser(id='{self.id}', user='{self.user_id}')>"


class SeedUser(BaseModel):
    """
    Users that we assume to have content similar to promoting users.
    Hence, we use their followers to build a candidate list to follow
    """

    __tablename__ = "seed_users"

    id = Column(Integer, primary_key=True, unique=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    promo_user_id = Column(Integer, ForeignKey("promo_users.user_id"), index=True)
    user_id = Column(String, unique=True)

    def __repr__(self):
        return f"<SeedUser(id='{self.id}', promo_user='{self.promo_user_id}', user='{self.user_id}')>"
