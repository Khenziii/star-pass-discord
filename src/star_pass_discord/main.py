from star_pass_discord.socials import (
    YouTubeGetter,
    BlueskyGetter,
    MastodonGetter,
    InstagramGetter,
)


def label(text: str):
    print()
    print(text)
    print()

def main():
    label("YOUTUBE")

    youtube = YouTubeGetter()
    posts = youtube.query()

    print(posts)

    label("BLUESKY")

    bluesky = BlueskyGetter()
    posts = bluesky.query()

    print(posts)

    label("MASTODON")

    mastodon = MastodonGetter()
    posts = mastodon.query()

    print(posts)

    label("INSTAGRAM")

    instagram = InstagramGetter()
    posts = instagram.query()

    print(posts)
