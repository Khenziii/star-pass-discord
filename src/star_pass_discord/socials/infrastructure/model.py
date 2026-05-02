from dataclasses import dataclass
from enum import StrEnum


class RSSBridgeName(StrEnum):
    YOUTUBE = "YoutubeBridge"
    BLUESKY = "BlueskyBridge"
    MASTODON = "MastodonBridge"
    INSTAGRAM = "InstagramBridge"
    THREADS = "ThreadsBridge"


@dataclass
class RSSBridgeItemDTO:
    url: str
    title: str
    date_modified: str


def build_bridge_item_dto(data) -> RSSBridgeItemDTO | None:
    try:
        return RSSBridgeItemDTO(data["url"], data["title"], data["date_modified"])
    except KeyError:
        return None


@dataclass
class RSSBridgeQueryResponseDTO:
    items: list[RSSBridgeItemDTO]
