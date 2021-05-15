import json

with open('C:\\Users\\Виктория\\Downloads\\RomeoAndJuliet.json', 'r', encoding='utf-8') as f:
    romeo = json.load(f)
    characters_list = []
    max_character_number = 0
    max_character = ''
    for act in romeo['acts']:
        for scene in act['scenes']:
            for action in scene['action']:
                characters_list.append(action['character'])
    for character in characters_list:
        if characters_list.count(character) > max_character_number:
            max_character_number = characters_list.count(character)
            max_character = character

print(max_character)
