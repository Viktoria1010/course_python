import json

file = open('3_1 задача.json', 'w')
with open('C:\\Users\\Виктория\\Downloads\\wikidata_1000.json', 'r', encoding='utf-8') as f:
    characters_list = []
    for line in f.readlines():
        characters_list.append(json.loads(line))
    dictionary = dict()
    for a in range(len(characters_list)):
        try:
            dictionary[characters_list[a]["label"]["value"]] = characters_list[a]["description"]["value"]
        except KeyError:
            dictionary[characters_list[a]["label"]["value"]] = "None"

file.write(json.dumps(dictionary, ensure_ascii=False, indent=4))
