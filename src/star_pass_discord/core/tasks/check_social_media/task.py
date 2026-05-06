import discord
import asyncio
from datetime import datetime, timedelta, timezone
from star_pass_discord.environment import get_environment
from star_pass_discord.core.tasks.task import Task, TaskName
from star_pass_discord.socials import (
    YouTubeGetter,
    BlueskyGetter,
    MastodonGetter,
    InstagramGetter,
    ThreadsGetter,
)
from star_pass_discord.socials.infrastructure import RSSBridgeGetter


# Getter fetches most recent posts.
async def check_platform(getter: RSSBridgeGetter, ctx: discord.Client):
    print(f"Fetching most recent posts from {getter.platform}...")
    posts = await asyncio.to_thread(getter.query)

    env = get_environment()
    fresh_post_seconds = env.internal.social_media_check_interval_seconds

    fresh_posts = []
    for post in posts:
        posted_at_date = datetime.fromisoformat(post.posted_at)
        now = datetime.now(timezone.utc)

        diference = now - posted_at_date
        is_fresh = diference < timedelta(seconds=fresh_post_seconds)

        if is_fresh:
            fresh_posts.append(post)

    if len(fresh_posts) == 0:
        print(f"No fresh posts (posted in last ~{fresh_post_seconds // 60} minutes) on {getter.platform}!")
        return

    # TODO: check if we've already sent a notification about this post.

    env = get_environment()
    channel = ctx.get_channel(int(env.discord.channels.social_media.id))

    for post in fresh_posts:
        await channel.send(f"{getter.platform}: {post.title} \n\n {post.url}")


class CheckSocialMediaTask(Task):
    def __init__(self, client: discord.Client):
        super().__init__(client, TaskName.CHECK_SOCIAL_MEDIA)

    async def run(self):
        platforms = [
            YouTubeGetter(), BlueskyGetter(), MastodonGetter(),
            InstagramGetter(), ThreadsGetter(),
        ]
        for platform in platforms:
            await check_platform(platform, self.client)
