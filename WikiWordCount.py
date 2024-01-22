import json
import re

import xmltodict

with open("fawiki-20240120-pages-articles-multistream.xml") as xml_file:
    wiki_dict = xmltodict.parse(xml_file.read())
wiki_data = json.dumps(wiki_dict)
keys = ['title', 'text']
articles = {x: wiki_data[x] for x in keys}
words = []
for x, y in articles:
    words.append(x)
    words.append(y)

alphabet = "\u0621-\u0628\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC"
zwnj = "\u200C+\u202F"  # zero_width_none_joiner
numbers = "\u0660-\u0669\u06F0-\u06F9"
used_arabic_characters = "\u0629\u0643\u0649-\u064B\u064D\u06D5"
punctuation = "\u060C\u061B\u061F\u0640\u066A\u066B\u066C"
pesian_word = alphabet + zwnj + numbers

for x in words:
    x = re.sub(' ' + punctuation + ' ', '', x)

word_counter = 0
total_word_count = 0
for word in words:
    word_counter = 0
    word_counter = word.split(' ').length
    total_word_count = total_word_count + word_counter

print(total_word_count)
