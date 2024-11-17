class Task:
    message: str
    done: bool = False
    
    def __init__(self, message):
        self.message = message
    
    def complete(self):
        self.done = true