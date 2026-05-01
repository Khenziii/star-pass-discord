from star_pass_discord.socials import (
    YouTubeGetter,
    BlueskyGetter,
    MastodonGetter,
)


def main():
    youtube = YouTubeGetter()
    posts = youtube.query()

    print(posts)

    bluesky = BlueskyGetter()
    posts = bluesky.query()

    print(posts)

    mastodon = MastodonGetter()
    posts = mastodon.query()

    print(posts)
