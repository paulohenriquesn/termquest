from events.sail import event_sail

default_options = {
    "SAIL TO ANOTHER PLACE": lambda player: event_sail(player),
    "VIEW PLAYER": lambda player: view_player(player),
    "MY CURRENT QUEST": lambda player: view_current_quest(player)
}

def show_interface(player):
    while True:
        
        print("\nChoose an option:")
        for idx, option in enumerate(default_options.keys(), start=1):
            print(f'{idx} - {option}')
        
        try:
            opt = int(input('-> '))
            if 1 <= opt <= len(default_options):
                selected_option = list(default_options.keys())[opt - 1]
                
                default_options[selected_option](player)
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def view_player(player):
    print("\nPlayer Information:")
    print(f"Name: {player.name}")
    print(f"Health: {player.health}")
    print(f"Hungry: {player.hungry}")
    print(f"Place: {player.place}")
    print("\nAttributes:")
    for attribute_name, attribute in player.attributes.items():
        print(f"{attribute_name.capitalize()}: Level {attribute.level}, EXP {attribute.exp}/{attribute.next_level_exp}")

def view_current_quest(player):
    if player.quest:
        print("\nCurrent Quest:")
        print(f"Quest Name: {player.quest.name}")
        print("Tasks:")
        player.quest.show_tasks()
    else:
        print("\nNo current quest.")