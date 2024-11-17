from init import PLACES
from game import chat

def event_sail(player):
    chat(f'Where you want to go?')
    for place in PLACES:
        chat(f'-> {place}')
    
    place_selected = input('> ')
    
    player.go_to(place_selected)
    
