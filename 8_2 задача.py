import json
import collections

with open('C:\\Users\\Виктория\\Downloads\\RomeoAndJuliet.json', 'r', encoding='utf-8') as rajfile:
    with open('RaJ.txt', 'w') as to_write:
        romeo = json.load(rajfile)
        dictionary = collections.defaultdict(list)
        for act in romeo["acts"]:
            for scene in act["scenes"]:
                for actions in scene["action"]:
                    dictionary[actions["character"]].append(actions["says"])
        to_write.write(str(dictionary))



