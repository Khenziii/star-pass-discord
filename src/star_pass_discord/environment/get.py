import os
from .model import (Environment, Discord, Channels, Identifiable,
                    RSSBridge, GenericSocialMedia, Internal)
from dotenv import load_dotenv


def load_variables() -> None:
    load_dotenv(".env")


def get_variable(key: str) -> str:
    return os.getenv(key)


def get_environment() -> Environment:
    load_variables()

    social_media = Identifiable(
        get_variable("DISCORD_CHANNELS_SOCIAL_MEDIA_ID")
    )
    channels = Channels(social_media)
    discord = Discord(
        get_variable("DISCORD_TOKEN"),
        channels,
    )

    rss_bridge = RSSBridge(get_variable("RSS_BRIDGE_URL"))

    youtube = GenericSocialMedia(get_variable("YOUTUBE_USERNAME"))
    bluesky = GenericSocialMedia(get_variable("BLUESKY_USERNAME"))
    mastodon = GenericSocialMedia(get_variable("MASTODON_USERNAME"))
    instagram = GenericSocialMedia(get_variable("INSTAGRAM_USERNAME"))
    threads = GenericSocialMedia(get_variable("THREADS_USERNAME"))

    internal = Internal(int(get_variable("SOCIAL_MEDIA_CHECK_INTERVAL_SECONDS")))

    return Environment(
        discord,
        rss_bridge,
        youtube,
        bluesky,
        mastodon,
        instagram,
        threads,
        internal,
    )
