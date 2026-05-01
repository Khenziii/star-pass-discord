from star_pass_discord.environment import get_environment
from star_pass_discord.socials.infrastructure import RSSBridgeGetter, RSSBridgeName
from star_pass_discord.socials import SocialMediaPlatform


class RSSBridgeThreadsGetter(RSSBridgeGetter):
    def __init__(self):
        super().__init__(RSSBridgeName.THREADS, SocialMediaPlatform.THREADS)

    def get_additional_args(self):
        env = get_environment()
        username = env.threads.username
        return f"context=By+username&u={username}&limit=5"
