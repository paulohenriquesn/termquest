
from init import NPCS
from quests.bob_cake import quest

bob = NPCS['bob']

def raise_quest_cake(player):
    bob.say('uuh, hey friend 👋')
    bob.say('notice u new here, I need your help 🛟')
    bob.say('I got some problems I need to cook a cake 🎂 for my cousin but...')
    bob.say('I have many problems to resolve today 😖 so I dont have time to buy the recipients 📜')
    bob.say('you can not look these recipients at me? i pay you something... 🪙')
    
    question = input('[yes or no]: ')

    if (question == 'yes'):
        bob.say('thanks hurry up the party is tonight...')
        player.set_quest(quest)
    else:
        bob.say('huh, ok if you change your decision talk to me')