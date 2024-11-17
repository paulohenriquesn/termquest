from entities.player import Player
from npcs.bob import raise_quest_cake
from interface import show_interface

player = Player(name="Alvard Kimor")

while True:
    show_interface(player)