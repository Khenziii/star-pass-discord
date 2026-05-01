from star_pass_discord.socials import YouTubeGetter


def main():
    youtube = YouTubeGetter()
    posts = youtube.query()

    print(posts)
