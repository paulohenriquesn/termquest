from vos.task import Task

class Quest:
    name: str
    messages: [str]
    tasks: [Task]
    exp: int

    def __init__(self,name, exp):
        self.name = name
        self.exp = exp

    def add_tasks(self,tasks):
        self.tasks = tasks
    
    def show_tasks(self):
        for task in self.tasks:
            if (task.done == True):
                print(f'✅ {task.message}')
            else:
                print(f'🚫 {task.message}')
