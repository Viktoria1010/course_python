import os
import math
import json
import re


class TFIDF:
    def __init__(self, path_to_file, texts):
        if os.path.exists(path_to_file):
            with open('idf.json', 'r') as idf_file:
                self._idf = json.load(idf_file)
        else:
            self._idf = self._count_idf(texts)

    def _count_tf(self, texts):
        tf_output = {}
        list_of_words = re.findall('[a-zа-яё]+', texts, flags=re.IGNORECASE)
        for word in list_of_words:
            amount = list_of_words.count(word)
            tf = amount/len(list_of_words)
            tf_output[word] = tf
        return tf_output

    def get_tf(self, texts):
        return self._count_tf(texts)

    def _count_idf(self, texts):
        with open(texts, 'r', encoding='utf-8') as file_for_tfidf:
            text = []
            for line in file_for_tfidf:
                text.append(line)
            idf_output = {}
            big_list = []
            for t in text:
                list_of_words = re.findall('[a-zа-яё]+', t, flags=re.IGNORECASE)
                big_list.append(list_of_words)
            if len(big_list) == 1:
                for wo in list_of_words:
                    idf = math.log10(len(list_of_words) / sum([1.0 for i in list_of_words if wo in i]))
                    idf_output[wo] = idf
            else:
                for w in big_list:
                    for word in w:
                        idf = math.log10(len(big_list)/sum([1.0 for i in big_list if word in i]))
                        idf_output[word] = idf
            with open('idf.json', 'w') as idf_file:
                json.dump(idf_output, idf_file, indent=4, ensure_ascii=False)
            return idf_output

    def get_idf(self, texts):
        return self._count_idf(texts)

    def tfidf(self, texts):
        tf_idf_output = {}
        for key in self.get_tf(texts):
            tfidf = self.get_idf(texts)[key] * self._idf[key]
            tf_idf_output[key] = tfidf
        return tf_idf_output


tf_idf = TFIDF(r'C:\Users\Виктория\OneDrive\Рабочий стол\Для Универа\Второй курс\Четвертый семестр\Прога\course_python\idf.json', 'text.txt')
tf_idf.tfidf('Великолепная «Школа злословия» вернулась в эфир после летних каникул в новом формате.')



