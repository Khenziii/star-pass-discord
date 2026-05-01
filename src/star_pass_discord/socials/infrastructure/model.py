from dataclasses import dataclass
from enum import StrEnum


class RSSBridgeName(StrEnum):
    YOUTUBE = "YoutubeBridge"
    BLUESKY = "BlueskyBridge"
    MASTODON = "MastodonBridge"


@dataclass
class RSSBridgeItemDTO:
    url: str
    title: str


def build_bridge_item_dto(data) -> RSSBridgeItemDTO:
    return RSSBridgeItemDTO(data["url"], data["title"])


@dataclass
class RSSBridgeQueryResponseDTO:
    items: list[RSSBridgeItemDTO]
