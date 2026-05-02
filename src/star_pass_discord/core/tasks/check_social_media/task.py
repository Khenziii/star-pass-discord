from star_pass_discord.core.tasks.task import Task, TaskName


class CheckSocialMediaTask(Task):
    def __init__(self):
        super().__init__(TaskName.CHECK_SOCIAL_MEDIA)

    def run(self):
        print("yo")
