import xml.etree.ElementTree as etree

with open(r'C:\Users\Виктория\Downloads\annot.opcorpora.no_ambig.xml', 'r', encoding='utf-8') as corpus:
    with open('4_1 задача.txt', 'w', encoding='utf-8') as to_write:
        tree = etree.parse(corpus)
        root = tree.getroot()
        for source in root.iter('source'):
            to_write.write(source.text)
            to_write.write('\n')
