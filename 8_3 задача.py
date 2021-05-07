import json
import collections

with open('C:\\Users\\Виктория\\Downloads\\RomeoAndJuliet.json', 'r', encoding='utf-8') as rajfile:
    romeo = json.load(rajfile)
    dictionary = collections.defaultdict(int)
    for act in romeo["acts"]:
        for scene in act["scenes"]:
            for actions in scene["action"]:
                dictionary[actions["character"]] += 1
    cnt = collections.Counter(dictionary)
    print(cnt)


