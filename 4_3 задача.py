import xml.etree.ElementTree as etree

tree = etree.parse(r'C:\Users\Виктория\Downloads\annot.opcorpora.no_ambig.xml')
root = tree.getroot()
conj = 0
verb = 0
for token in root.iter('token'):
    if token.get('text').lower() == 'может':
        data = []
        for g in token.iter('g'):
            data.append(g.get('v'))
        if "VERB" in data:
            verb += 1
        elif "CONJ" in data:
            conj += 1

print(verb, conj)
