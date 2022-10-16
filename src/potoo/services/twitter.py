import tweepy
from tweepy.models import User as TwitterUser


def get_twitter_client(
    api_key: str, api_secret: str, access_token: str, access_token_secret: str
) -> tweepy.API:
    auth = tweepy.OAuth1UserHandler(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return tweepy.API(auth)


# def handleRateLimits(self, cursor):
#
#     while True:
#         try:
#             yield cursor.next()
#         except tweepy.RateLimitError:
#             self.logger.warn('RateLimit Timeout is reached. Needs to wait for 15 mins...')
#             time.sleep(15 * MINS)
#         except tweepy.TweepError as tweepyError:
#             if tweepyError.response.status_code == 429:
#                 self.logger.warn('RateLimit Timeout is reached. Needs to wait for 15 mins...')
#                 time.sleep(15 * MINS)
#             else:
#                 raise tweepyError
#         except StopIteration:
#             return


class TwitterUserService:
    """ """

    def __init__(self, twitter_client: tweepy.API) -> None:
        self._twitter_client: tweepy.API = twitter_client

    def fetch_profile_by_username(self, username: str) -> TwitterUser:
        profile = self._twitter_client.get_user(screen_name=username)

        return profile

    def fetch_profiles_by_usernames(self, usernames: list[str]) -> list[TwitterUser]:
        profiles = self._twitter_client.lookup_users(screen_name=",".join(usernames))

        return profiles
