from urllib.parse import quote
from star_pass_discord.environment import get_environment
from star_pass_discord.socials.infrastructure import RSSBridgeGetter, RSSBridgeName
from star_pass_discord.socials import SocialMediaPlatform


class RSSBridgeYouTubeGetter(RSSBridgeGetter):
    def __init__(self):
        super().__init__(RSSBridgeName.YOUTUBE, SocialMediaPlatform.YOUTUBE)

    def get_additional_args(self):
        env = get_environment()
        name = quote(env.youtube.username)
        return f"context=By+custom+name&custom={name}&duration_min=&duration_max="
