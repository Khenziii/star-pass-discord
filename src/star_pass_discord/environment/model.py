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
class Environment:
    discord: Discord
