import nltk
import json
import string
import re

di = open("dec_independence.txt")

di_text = di.read()

di_token = nltk.word_tokenize(di_text)


essays = json.loads(open('one_topic_essays.json').read())
one_string = "".join([e['text'] for e in essays])
one_string_lower = one_string.lower()


essays_token = nltk.word_tokenize(one_string, 'portuguese')
essays_token_lower = nltk.word_tokenize(one_string_lower, 'portuguese')

len(set(essays_token))
len(set(essays_token_lower))


text_fd = nltk.FreqDist(essays_token_lower)
var = text_fd['com']

total_caracters_before = 0
total_caracters_after = 0
for e in essays:
    total_caracters_before += len(e['text'])

palavras = 0
lista = []
regex = re.compile('[%s]' % re.escape(string.punctuation))
for e in essays:
    s = regex.sub('', e['text'])
    total_caracters_after += len(s)
    palavras += len(s.split())
    for w in e['text'].split():
        lista.append(w)

print(palavras)
print(len(lista))
print(len(set(lista)))
print("total caracteres antes: " + str(total_caracters_before))
print("total caracteres depois: " + str(total_caracters_after))
