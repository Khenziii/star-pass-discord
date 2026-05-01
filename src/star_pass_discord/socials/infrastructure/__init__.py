from .model import RSSBridgeQueryResponseDTO, RSSBridgeItemDTO, RSSBridgeName, build_bridge_item_dto
from .get import RSSBridgeGetter

from .youtube import RSSBridgeYouTubeGetter
from .bluesky import RSSBridgeBlueskyGetter
from .mastodon import RSSBridgeMastodonGetter


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
]
