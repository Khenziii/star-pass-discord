import discord
from discord import app_commands
from discord.ext import tasks
from .tasks import TaskExecutor, CheckSocialMediaTask


class Client(discord.Client):
    task_executor: TaskExecutor

    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)
        self.task_executor = TaskExecutor()

    async def setup_hook(self):
        await self.tree.sync()

        self.check_social_media.start()

    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    @tasks.loop(seconds=10)
    async def check_social_media(self):
        task = CheckSocialMediaTask()
        self.task_executor.run(task)

    @check_social_media.before_loop
    async def before_check_social_media(self):
        await self.wait_until_ready()
