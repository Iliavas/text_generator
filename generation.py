from pickle import load
from random import choice

l = 100
with open('a.pickle', 'rb') as f:
    data = load(f)

text = ''
print(type(data.keys()))
start_pos = choice(list(data.keys()))
for _ in range(l):
    text += start_pos + ' '
    start_pos = choice(data[start_pos])
print(text)
