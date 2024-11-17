from entities.quest import Quest
from vos.task import Task

quest = Quest(name="🎂 Cake's recipient", exp=10)
tasks = [
    Task(message="🥚 collect an egg outside"),
    Task(message="🥛 collect some milk on the cows"),
    Task(message="🧑🏻‍🍳 send recipients to bob")
]

quest.add_tasks(tasks)