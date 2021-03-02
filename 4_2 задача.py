import xml.etree.ElementTree as etree

tree = etree.parse(r'C:\Users\Виктория\Downloads\annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open('4_2 задача.txt', 'w', encoding='utf-8') as to_write:
    for token in root.iter('token'):
        data = []
        for g in token.iter('g'):
            data.append(g.get('v'))
        if 'NOUN' in data:
            if 'plur' in data:
                to_write.write(token.get('text'))
                to_write.write('\n')
