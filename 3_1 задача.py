import json

dict_new = dict()
with open('3_1 задача.json', 'w') as to_write:
    with open('C:\\Users\\Виктория\\Downloads\\wikidata_1000.json', 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            try:
                dict_new[data["label"]["value"]] = data["description"]["value"]
            except KeyError:
                dict_new[data["label"]["value"]] = None
        to_write.write(json.dumps(dict_new, ensure_ascii=False, indent=4))
