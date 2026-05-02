from .task import Task


class TaskExecutor:
    async def run(self, task: Task):
        print(f"Running task \"{task.name}\"...")
        await task.run()
