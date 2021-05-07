import collections
import csv
from collections import OrderedDict

with open('C:\\Users\\Виктория\\Downloads\\stage3_test.csv', 'r', encoding='utf-8') as testfile:
    with open('to_write.txt', 'w') as to_write:
        reader = csv.DictReader(testfile)
        dictionary = collections.defaultdict(int)
        for row in reader:
            dictionary[row['Id']] = row['Price']
        dictionary_ordered = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1]))
        dictionary_reversed = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1], reverse=True))
        to_write.write(str(dictionary_ordered) + '\n')
        to_write.write(str(dictionary_reversed))






