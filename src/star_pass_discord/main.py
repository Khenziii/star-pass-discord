from star_pass_discord.socials import YouTubeGetter, BlueskyGetter


def main():
    youtube = YouTubeGetter()
    posts = youtube.query()

    print(posts)

    bluesky = BlueskyGetter()
    posts = bluesky.query()

    print(posts)
