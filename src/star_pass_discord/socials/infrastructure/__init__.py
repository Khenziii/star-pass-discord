from .model import RSSBridgeQueryResponseDTO, RSSBridgeItemDTO, RSSBridgeName, build_bridge_item_dto
from .get import RSSBridgeGetter

from .youtube import RSSBridgeYouTubeGetter
from .bluesky import RSSBridgeBlueskyGetter
from .mastodon import RSSBridgeMastodonGetter
from .instagram import RSSBridgeInstagramGetter


__all__ = [
    "RSSBridgeQueryResponseDTO",
    "RSSBridgeItemDTO",
    "RSSBridgeGetter",
    "RSSBridgeName",
    "build_bridge_item_dto",
] + [
    "RSSBridgeYouTubeGetter",
    "RSSBridgeBlueskyGetter",
    "RSSBridgeMastodonGetter",
    "RSSBridgeInstagramGetter",
]
