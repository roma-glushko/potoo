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

    seed_users = relationship("SeedUser")

    followers = relationship("FollowersUpdateCampaign")
    follow_requests = relationship("FollowCampaign")

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

    promo_username = Column(String, ForeignKey("promo_users.username"), index=True)
    username = Column(String, unique=True)
    user_id = Column(String, unique=True)

    def __repr__(self):
        return f"<SeedUser(id='{self.id}', promo_user='{self.promo_username}', username='{self.username}')>"


class FollowCandidate(BaseModel):
    """
    A candidate that we can try to follow. Collected based on the seed account's followers
    """

    __tablename__ = "follow_candidates"

    id = Column(Integer, primary_key=True, unique=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<FollowCandidate(id='{self.id}')>"


class Follower(BaseModel):
    """ """

    __tablename__ = "followers"

    id = Column(Integer, primary_key=True, unique=True)
    added_at = Column(DateTime, default=datetime.utcnow)
    campaign_id = Column(
        Integer, ForeignKey("followers_update_campaigns.id"), index=True
    )

    promo_username = Column(String, ForeignKey("promo_users.username"), index=True)

    username = Column(String, unique=True)
    user_id = Column(String, unique=True)

    def __repr__(self):
        return f"<Follower(id='{self.id}', promo_user='{self.promo_username}', username='{self.username})>"


class FollowersUpdateCampaign(BaseModel):
    """ """

    __tablename__ = "followers_update_campaigns"

    id = Column(Integer, primary_key=True, unique=True)

    promo_username = Column(String, ForeignKey("promo_users.username"), index=True)

    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, default=None)

    followers = relationship("Follower")

    def __repr__(self):
        return f"<FollowersUpdateCampaign(id='{self.id}')>"


class FollowRequest(BaseModel):
    """ """

    __tablename__ = "follow_requests"

    id = Column(Integer, primary_key=True, unique=True)
    requested_at = Column(DateTime, default=datetime.utcnow)

    campaign_id = Column(Integer, ForeignKey("follow_campaigns.id"), index=True)

    promo_username = Column(String, ForeignKey("promo_users.username"), index=True)

    username = Column(String, unique=True)
    user_id = Column(String, unique=True)

    def __repr__(self):
        return f"<FollowRequest(id='{self.id}')>"


class FollowCampaign(BaseModel):
    """ """

    __tablename__ = "follow_campaigns"

    id = Column(Integer, primary_key=True, unique=True)

    promo_username = Column(String, ForeignKey("promo_users.username"), index=True)

    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, default=None)

    requests = relationship("FollowRequest")

    def __repr__(self):
        return f"<FollowCampaign(id='{self.id}')>"


class ProfilesUpdateCampaign(BaseModel):
    """ """

    __tablename__ = "profiles_update_campaigns"

    id = Column(Integer, primary_key=True, unique=True)

    updated_profiles = relationship("Profile")

    def __repr__(self):
        return f"<ProfilesUpdateCampaign(id='{self.id}')>"


class Profile(BaseModel):
    """ """

    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, unique=True)
    added_at = Column(DateTime, default=datetime.utcnow)
    campaign_id = Column(
        Integer, ForeignKey("profiles_update_campaigns.id"), index=True
    )

    username = Column(String)
    user_id = Column(String)

    # TODO: Add more fields

    recent_tweets = relationship("Tweet")


class Tweet(BaseModel):
    """ """

    __tablename__ = "tweets"

    id = Column(String, primary_key=True, unique=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    created_at = Column(DateTime)

    # TODO: Add more fields
