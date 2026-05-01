from dataclasses import dataclass


@dataclass
class Discord:
    token: str


@dataclass
class Environment:
    discord: Discord
