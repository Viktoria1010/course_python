import json
import collections

with open('C:\\Users\\Виктория\\Downloads\\RomeoAndJuliet.json', 'r', encoding='utf-8') as rajfile:
    romeo = json.load(rajfile)
    set_of_words = []
    for act in romeo["acts"]:
        for scene in act["scenes"]:
            for actions in scene["action"]:
                for phrase in actions["says"]:
                    phrase = phrase.replace('.', '').replace('!', '').replace('?', '').replace(':', '').replace('?', '')
                    phrase = phrase.replace(',', '')
                    phrase = phrase.replace(';', '')
                    phrase = phrase.replace('--', '')
                sentence = phrase.split(' ')
                for word in sentence:
                    set_of_words.append(word.lower())
    cnt = collections.Counter(set_of_words)
    print(cnt.most_common(20))
    print(cnt.most_common()[:-21:-1])

