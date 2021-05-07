import json
import collections

with open('C:\\Users\\Виктория\\Downloads\\RomeoAndJuliet.json', 'r', encoding='utf-8') as rajfile:
    romeo = json.load(rajfile)
    cnt = collections.Counter()
    for act in romeo["acts"]:
        for scene in act["scenes"]:
            for actions in scene["action"]:
                cnt[actions["character"]] += 1
    print(cnt)


