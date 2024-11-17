from game import chat

class Npc:
    name: str
    char: str

    def __init__(self, name, char):
        self.name = name
        self.char = char
    
    def say(self, msg):
        chat(f"[{self.char} {self.name}]: {msg}")