import xml.etree.ElementTree as etree


class Corpus:
    def __init__(self):
        self._sentences = []

    def load_corpus(self, path_to_file):
        tree = etree.parse(path_to_file)
        root = tree.getroot()
        for sentence in root.iter('sentence'):

            for source in sentence.iter('source'):
                self._sentences.append(source.text)
                Sentence.sent = source.text
                for word in root.iter('token'):
                    for g in word.iter('g'):
                        if g.get('v') == 'PNKT':
                            pass
                        else:
                            word = Wordform()
                            word.text = Wordform().word
                            Sentence(source.text).words.append(word.text)
                        for gramm in root.iter('g'):
                            Wordform().grammems.append(str(gramm.get('v')))

    def get_sentence(self):
        i = int(input('Введите номер предложения: '))
        if i in range(len(self._sentences)):
            print(self._sentences[i])
        else:
            print("Предложения с таким номером не существует.")


class Sentence:
    def __init__(self, sent):
        self.sent = sent
        self.words = []


class Wordform:
    def __init__(self):
        self.word = ''
        self.grammems = []


corp = Corpus()
corp.load_corpus('C:\\Users\\Виктория\\Downloads\\annot.opcorpora.no_ambig.xml')
corp.get_sentence()
