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
        if sent in range(len(self.__sentences)):
            if word in range(len(self.__sentences[sent].words)):
                if gramm in range(len(self.__sentences[sent].words[word].grammems)):
                    print(f'Предложение: {self.__sentences[sent].sent_text}, ' 
                          f'слово: {self.__sentences[sent].words[word].word}, '
                          f'граммема: {self.__sentences[sent].words[word].grammems[gramm]}')
                    return f'Предложение: {self.__sentences[sent].sent_text}, ' \
                           f'слово: {self.__sentences[sent].words[word].word}, ' \
                           f'граммема: {self.__sentences[sent].words[word].grammems[gramm]}'
                else:
                    print('Sorry :(, i need another grammema')
            else:
                print("Another word, please")
        else:
            print('Smth is wrong here')

    def get_sentence(self, i):
        if i in range(len(self.__sentences)):
            print(f"Предложение: {self.__sentences[i].sent_text}")
            return f"Предложение: {self.__sentences[i].sent_text}"
        else:
            print("Предложения с таким номером не существует.")

    def get_sent_words(self, sent):
        sentence = self.__sentences[sent]
        words = []
        for word in range(len(sentence.words)):
            words.append(sentence.words[word].word)
        print(f'Предложение: {sentence.sent_text}, слова: {words}')
        return f'Предложение: {sentence.sent_text}, слова: {words}'

    def get_word_gramms(self, sent, word):
        w = self.__sentences[sent].words[word]
        print(f'Слово: {w.word}, граммемы: {w.grammems}')
        return f'Слово: {w.word}, граммемы: {w.grammems}'

    def get_word(self, sent, word):
        w = self.__sentences[sent].words[word]
        print(f'Слово: {w.word}')
        return f'Слово: {w.word}'

    def get_grammema(self, sent, word, gramm):
        g = self.__sentences[sent].words[word].grammems[gramm]
        print(f'Граммема: {g}')
        return f'Граммема: {g}'


class Sentence:
    def __init__(self, sent_text, list_of_words):
        self.sent_text = sent_text
        self.words = list_of_words


class Wordform:
    def __init__(self, word, grammems):
        self.word = word
        self.grammems = grammems


corp = Corpus()
corp.load_corpus(r'C:\Users\Виктория\Downloads\annot.opcorpora.no_ambig.xml')
corp.get_whatever(0, 0, 0)
corp.get_sent_words(0)
corp.get_word_gramms(0, 0)
corp.get_word(0, 0)
corp.get_sentence(0)
corp.get_grammema(0, 0, 0)
