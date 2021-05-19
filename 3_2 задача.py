import json

with open('3_2 задача.json', 'w') as to_write:
    with open('C:\\Users\\Виктория\\Downloads\\RomeoAndJuliet.json', 'r', encoding='utf-8') as f:
        romeo = json.load(f)
        for act in range(len(romeo['acts'])):
            for scene in range(len(romeo['acts'][act]['scenes'])):
                set_char = set()
                for characters in range(len(romeo['acts'][act]['scenes'][scene]['action'])):
                    set_char.add(romeo['acts'][act]['scenes'][scene]['action'][characters]['character'])
        for act in romeo['acts']:
            for scene in act['scenes']:
                set_char = set()
                for characters in scene['action']:
                    set_char.add(characters['character'])
                to_write.write(json.dumps(list(set_char), ensure_ascii=False))
                to_write.write('\n')
