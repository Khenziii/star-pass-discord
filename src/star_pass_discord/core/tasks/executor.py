from .task import Task


class TaskExecutor:
    def run(self, task: Task):
        print(f"Running task \"{task.name}\"...")
        task.run()
