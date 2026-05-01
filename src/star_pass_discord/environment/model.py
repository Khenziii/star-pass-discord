from dataclasses import dataclass


@dataclass
class Identifiable:
    id: str


@dataclass
class Channels:
    social_media: Identifiable


@dataclass
class Discord:
    token: str
    channels: Channels


@dataclass
class RSSBridge:
    url: str


@dataclass
class GenericSocialMedia:
    username: str


@dataclass
class Environment:
    discord: Discord
    rss_bridge: RSSBridge
    youtube: GenericSocialMedia
    bluesky: GenericSocialMedia
    mastodon: GenericSocialMedia
    instagram: GenericSocialMedia
    threads: GenericSocialMedia
