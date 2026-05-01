from star_pass_discord.socials.infrastructure import RSSBridgeGetter, RSSBridgeName
from star_pass_discord.socials import SocialMediaPlatform


class RSSBridgeInstagramGetter(RSSBridgeGetter):
    def __init__(self):
        super().__init__(RSSBridgeName.INSTAGRAM, SocialMediaPlatform.INSTAGRAM)

    def get_additional_args(self):
        # TODO: replace with an environment variable
        username = "starpass_eu"
        return f"context=Username&u={username}&media_type=all"
