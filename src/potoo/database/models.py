from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from potoo.database.engine import BaseModel


class PromoUser(BaseModel):
    """
    Users that we need to promote via the follow rate optimization
    """

    __tablename__ = "promo_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

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
    username = Column(String, unique=True)

    promo_user_id = Column(Integer, ForeignKey("promo_users.id"), index=True)

    def __repr__(self):
        return f"<SeedUser(id='{self.id}', username='{self.username}', promo_user='{self.promo_user_id}')>"
