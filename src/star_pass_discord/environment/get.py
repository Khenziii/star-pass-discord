import os
from .model import Environment, Discord, Channels, Identifiable, RSSBridge
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

    return Environment(discord, rss_bridge)
