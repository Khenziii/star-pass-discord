from star_pass_discord.socials.infrastructure import RSSBridgeGetter, RSSBridgeName
from star_pass_discord.socials import SocialMediaPlatform


class RSSBridgeBlueskyGetter(RSSBridgeGetter):
    def __init__(self):
        super().__init__(RSSBridgeName.BLUESKY, SocialMediaPlatform.BLUESKY)

    def get_additional_args(self):
        username = "star-pass.bsky.social"
        return f"data_source=getAuthorFeed&user_id={username}&feed_filter=posts_and_author_threads&include_reposts=on"
