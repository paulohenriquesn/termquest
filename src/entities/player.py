from vos.attribute import Attribute
from entities.quest import Quest
from game import chat

class Player:
    name: str
    health = 100
    hungry = 0
    quest: Quest = None
    place: str = 'venore'
    attributes = {
        "level": Attribute(name="level"),
        "attack": Attribute(name="attack"),
        "shield": Attribute(name="shield"),
    }

    def __init__(self, name):
        self.name = name

    def go_to(self, place):
        chat(f'✈️ u travelled to {place}')
        self.place = place

    def set_quest(self, quest):
        chat(f'📝 u got a new quest {quest.name}')
        chat(f'tasks of quest:')
        quest.show_tasks()
        self.quest = quest