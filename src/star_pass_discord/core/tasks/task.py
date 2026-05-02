from abc import ABC, abstractmethod
from enum import StrEnum


class TaskName(StrEnum):
    CHECK_SOCIAL_MEDIA = "CHECK-SOCIAL-MEDIA"


class Task(ABC):
    name: TaskName

    def __init__(self, name: TaskName):
        self.name = name

    @abstractmethod
    def run(self):
        pass
