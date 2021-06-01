import unittest
from task_13 import Corpus


class Tests(unittest.TestCase):
    def setUp(self):
        self.coprus = Corpus()
        self.coprus.load_corpus(r'C:\Users\Виктория\Downloads\annot.opcorpora.no_ambig.xml')

    def test_word(self):
        word = self.coprus.get_word(1, 1)
        self.assertEqual(word, 'Слово: ли')

    def test_gramm(self):
        gramm = self.coprus.get_grammema(1, 2, 2)
        self.assertEqual(gramm, "Граммема: masc")

    def test_sentence(self):
        sent = self.coprus.get_sentence(5)
        self.assertEqual(sent, "Предложение: В остальном «Школа злословия» представляла собой интервью ведущих с героем выпуска.")

    def test_word_gramms(self):
        word = self.coprus.get_word_gramms(2, 4)
        self.assertEqual(word, "Слово: в, граммемы: ['PREP']")

    def test_sent_words(self):
        sent = self.coprus.get_sent_words(3)
        self.assertEqual(sent, "Предложение: В истории программы это уже не первый «ребрендинг»., слова: ['В', 'истории', 'программы', 'это', 'уже', 'не', 'первый', 'ребрендинг']")

    def test_everything(self):
        sent = self.coprus.get_whatever(2, 3, 4)
        self.assertEqual(sent, 'Предложение: Великолепная «Школа злословия» вернулась в эфир после летних каникул в новом формате., слово: вернулась, граммема: sing')



if __name__ == '__main__':
    unittest.main()
