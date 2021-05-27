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
            if word in range(len(self.__sentences[sent]._words)):
                if gramm in range(len(self.__sentences[sent]._words[word]._grammems)):
                    print(f'Предложение: {self.__sentences[sent]._sent_text}, слово: {self.__sentences[sent]._words[word]._word}, граммема: {self.__sentences[sent]._words[word]._grammems[gramm]}')
                    return f'Предложение: {self.__sentences[sent]._sent_text}, слово: {self.__sentences[sent]._words[word]._word}, граммема: {self.__sentences[sent]._words[word]._grammems[gramm]}'
                else:
                    print('Sorry :(, i need another grammema')
            else:
                print("Another word, please")
        else:
            print('Smth is wrong here')

    def get_sentence(self, i):
        if i in range(len(self.__sentences)):
            print(f"Предложение: {self.__sentences[i]._sent_text}")
            return f"Предложение: {self.__sentences[i]._sent_text}"
        else:
            print("Предложения с таким номером не существует.")

    def get_sent_words(self, sent):
        sentence = self.__sentences[sent]
        print(Sentence.get_sent_words(sentence))
        return Sentence.get_sent_words(sentence)

    def get_word_gramms(self, sent, word):
        w = self.__sentences[sent]._words[word]
        print(Wordform.get_word_gramms(w))
        return Wordform.get_word_gramms(w)

    def get_word(self, sent, word):
        w = self.__sentences[sent]._words[word]
        print(Wordform.get_word(w))
        return Wordform.get_word(w)

    def get_grammema(self, sent, word, gramm):
        w = self.__sentences[sent]._words[word]
        print(Wordform.get_gramm(w, gramm))
        return Wordform.get_gramm(w, gramm)

class Sentence:
    def __init__(self, sent_text, list_of_words):
        self._sent_text = sent_text
        self._words = list_of_words

    def get_sent_words(self):
        text = []
        for word in range(len(self._words)):
            word = self._words[word]._word
            text.append(word)
        return f'Предложение: {self._sent_text}, слова: {text}'


class Wordform:
    def __init__(self, word, grammems):
        self._word = word
        self._grammems = grammems

    def get_word_gramms(self):
        return f'Слово: {self._word}, граммемы: {self._grammems}'

    def get_word(self):
        return f"Слово: {self._word}"

    def get_gramm(self, i):
        return f'Граммема: {self._grammems[i]}'


corp = Corpus()
corp.load_corpus(r'C:\Users\Виктория\Downloads\annot.opcorpora.no_ambig.xml')
corp.get_whatever(0, 0, 0)
corp.get_sent_words(0)
corp.get_word_gramms(0, 0)
corp.get_word(0, 0)
corp.get_sentence(0)
corp.get_grammema(0, 0, 0)
