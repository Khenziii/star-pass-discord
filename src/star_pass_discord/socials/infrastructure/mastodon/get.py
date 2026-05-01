from urllib.parse import quote
from star_pass_discord.socials.infrastructure import RSSBridgeGetter, RSSBridgeName
from star_pass_discord.socials import SocialMediaPlatform


class RSSBridgeMastodonGetter(RSSBridgeGetter):
    def __init__(self):
        super().__init__(RSSBridgeName.MASTODON, SocialMediaPlatform.MASTODON)

    def get_additional_args(self):
        # TODO: replace with an environment variable
        username = quote("@starpass_eu@mastodon.social")
        return f"canusername={username}&norep=on&noboost=on&signaturetype=noquery"
