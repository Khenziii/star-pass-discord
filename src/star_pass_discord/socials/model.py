from dataclasses import dataclass
from enum import StrEnum


class SocialMediaPlatform(StrEnum):
    YOUTUBE = "YouTube"
    BLUESKY = "Bluesky"
    MASTODON = "Mastodon"
    INSTAGRAM = "Instagram"
    THREADS = "Threads"


@dataclass
class SocialMediaPost:
    title: str
    url: str
    posted_at: str
    platform: SocialMediaPlatform
