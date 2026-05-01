from urllib.parse import quote
from star_pass_discord.socials.infrastructure import RSSBridgeGetter, RSSBridgeName
from star_pass_discord.socials import SocialMediaPlatform


class RSSBridgeYouTubeGetter(RSSBridgeGetter):
    def __init__(self):
        super().__init__(RSSBridgeName.YOUTUBE, SocialMediaPlatform.YOUTUBE)

    def get_additional_args(self):
        name = quote("@STAR-PASS")
        return f"context=By+custom+name&custom={name}&duration_min=&duration_max="
