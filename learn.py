import re
from pickle import dump


parse_dict = {}

text = open('text.txt', 'r').read()
text = re.sub(r'\n', ' ', text)
text = re.sub(r'\.',' ', text)
text = re.sub(r'[^А-я,  ]', ' ', text)

text = re.sub(r',', ' ', text)
r_text = ''
for i in range(len(text) - 1):
    if not (text[i] == ' ' and not text[i + 1].isalpha()):
        r_text += text[i]
r_text = r_text.lower()

r_text = re.split(' ', r_text)

for i in range(len(r_text) - 1):
    if r_text[i] in parse_dict.keys():
        parse_dict[r_text[i]].append(r_text[i + 1])
    else:
        parse_dict.update({r_text[i]: [r_text[i + 1]]})


with open('a.pickle', 'wb') as f :
    dump(parse_dict, f)
