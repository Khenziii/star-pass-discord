from star_pass_discord.core import Client
from star_pass_discord.environment import get_environment


def main():
    print("Starting up...")

    env = get_environment()

    client = Client()
    client.run(env.discord.token)
