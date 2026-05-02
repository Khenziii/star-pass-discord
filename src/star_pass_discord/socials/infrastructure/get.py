from dataclasses import dataclass
from requests import get
from abc import ABC, abstractmethod
from star_pass_discord.socials.infrastructure import (
    RSSBridgeName, build_bridge_item_dto
)
from star_pass_discord.socials import SocialMediaPost, SocialMediaPlatform
from star_pass_discord.environment import get_environment


@dataclass
class SharedRSSBridgeGetterConfig:
    url: str


class RSSBridgeGetter(ABC):
    bridge_name: RSSBridgeName
    platform: SocialMediaPlatform
    shared_config: SharedRSSBridgeGetterConfig

    def __init__(self, bridge_name: RSSBridgeName, platform: SocialMediaPlatform):
        env = get_environment()

        self.bridge_name = bridge_name
        self.platform = platform
        self.shared_config = SharedRSSBridgeGetterConfig(env.rss_bridge.url)

    @abstractmethod
    def get_additional_args(self) -> str | None:
        pass

    def query(self) -> list[SocialMediaPost]:
        additional_args = self.get_additional_args()
        if additional_args is None:
            additional_args = ""
        else:
            additional_args = f"&{additional_args}"

        url = f"{self.shared_config.url}/?action=display&bridge={
            self.bridge_name}{additional_args}&format=Json"

        try:
            response = get(url)
            json = response.json()
            posts = []

            for item in json["items"]:
                dto = build_bridge_item_dto(item)

                if dto is None:
                    continue

                post = SocialMediaPost(dto.title, dto.url, self.platform)
                posts.append(post)

            return posts
        except Exception as e:
            print(f"Failed to fetch most recent posts for {
                  self.platform} platform!")
            print("Requested URL:")
            print(url)
            raise e
