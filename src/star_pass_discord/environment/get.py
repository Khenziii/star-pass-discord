import os
from .model import Environment, Discord
from dotenv import load_dotenv


def load_variables() -> None:
    load_dotenv(".env")


def get_variable(key: str) -> str:
    return os.getenv(key)


def get_environment() -> Environment:
    load_variables()

    discord = Discord(
        get_variable("DISCORD_TOKEN")
    )

    return Environment(discord)
