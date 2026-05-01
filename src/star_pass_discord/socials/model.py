from dataclasses import dataclass
from enum import StrEnum


class SocialMediaPlatform(StrEnum):
    YOUTUBE = "YouTube"


@dataclass
class SocialMediaPost:
    title: str
    url: str
    platform: SocialMediaPlatform
