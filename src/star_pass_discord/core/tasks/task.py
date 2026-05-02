import discord
from abc import ABC, abstractmethod
from enum import StrEnum


class TaskName(StrEnum):
    CHECK_SOCIAL_MEDIA = "CHECK-SOCIAL-MEDIA"


class Task(ABC):
    name: TaskName
    client: discord.Client

    def __init__(self, client: discord.Client, name: TaskName):
        self.name = name
        self.client = client

    @abstractmethod
    async def run(self):
        pass
