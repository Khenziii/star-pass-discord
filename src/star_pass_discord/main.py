from star_pass_discord.environment import get_environment


def main():
    env = get_environment()
    print(env.discord.channels.social_media.id)
