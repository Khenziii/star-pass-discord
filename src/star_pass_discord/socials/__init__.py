from .model import SocialMediaPlatform, SocialMediaPost
from .infrastructure import (
    RSSBridgeYouTubeGetter as YouTubeGetter,
    RSSBridgeBlueskyGetter as BlueskyGetter,
    RSSBridgeMastodonGetter as MastodonGetter,
    RSSBridgeInstagramGetter as InstagramGetter,
)


__all__ = [
    "SocialMediaPost",
    "SocialMediaPlatform",
] + [
    "YouTubeGetter",
    "BlueskyGetter",
    "MastodonGetter",
    "InstagramGetter",
]
