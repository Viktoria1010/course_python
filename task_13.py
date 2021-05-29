import xml.etree.ElementTree as etree


class Corpus:
    def __init__(self):
        self.__sentences = []

    def load_corpus(self, path_to_file):
        tree = etree.parse(path_to_file)
        root = tree.getroot()
        for sentence in root.iter('sentence'):
            sent_text = sentence.find('source').text
            words = []
            for token in sentence.find('tokens'):
                word_text = token.get('text')
                grammems = []
                for g in token[0][0][0].findall('g'):
                    if g.attrib.get('v') == "PNCT":
                        pass
                    else:
                        grammems.append(g.attrib.get('v'))
                if grammems == []:
                    pass
                else:
                    token = Wordform(word_text, grammems)
                    words.append(token)
            sentence = Sentence(sent_text, words)
            self.__sentences.append(sentence)

    def get_whatever(self, sent, word, gramm):  # определенная граммема определенного слова определенного предложения
        s = self.__sentences[sent]
        w = s.return_word(word)
        w_text = w.return_word_text()
        g = w.return_grammema(gramm)
        print(f'Предложение: {s.return_sentence()}, {w_text}, {g}')

    def get_sent_words(self, sent):
        sentence = self.__sentences[sent]
        print(sentence.return_sent_words())
        return sentence.return_sent_words()

    def get_word_gramms(self, sent, word):
        s = self.__sentences[sent]
        w = s.return_word(word)
        print(w.return_gramms_of_word())
        return w.return_gramms_of_word()

    def get_word(self, sent, word):
        s = self.__sentences[sent]
        w = s.return_word(word)
        print(w.return_word_text())
        return w.return_word_text()

    def get_grammema(self, sent, word, gramm):
        s = self.__sentences[sent]
        w = s.return_word(word)
        print(w.return_grammema(gramm))
        return w.return_grammema(gramm)

    def get_sentence(self, sent):
        sentence = self.__sentences[sent]
        print(f'Предложение: {sentence.return_sentence()}')


class Sentence:
    def __init__(self, sent_text, list_of_words):
        self._sent_text = sent_text
        self._words = list_of_words

    def return_sent_words(self):
        words_text = []
        for word in self._words:
            words_text.append(word.return_word_text())
        return f'Предложение: {self._sent_text}, слова: {words_text}'

    def return_sentence(self):
        return self._sent_text

    def return_word(self, word):
        return self._words[word]


class Wordform:
    def __init__(self, word, grammems):
        self._word = word
        self._grammems = grammems

    def return_word_text(self):
        return f'Слово: {self._word}'

    def return_gramms_of_word(self):
        return f'Cлово: {self._word}, грамеммы: {self._grammems}'

    def return_grammema(self, gramm):
        return f'Грамемма: {self._grammems[gramm]}'


corp = Corpus()
corp.load_corpus(r'C:\Users\Виктория\Downloads\annot.opcorpora.no_ambig.xml')
corp.get_whatever(0, 0, 0)
corp.get_sent_words(0)
corp.get_word_gramms(0, 0)
corp.get_word(0, 0)
corp.get_sentence(0)
corp.get_grammema(0, 0, 0)
