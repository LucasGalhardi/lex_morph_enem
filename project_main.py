import json
import nltk
import pickle
from pt_tagger import pt_tagger
from polyglot.text import Text
from lemmatizer import lemmatizer


class DWord(object):

    def __init__(self):
        self.id = 0
        self.word = ''
        self.freq = 0
        self.occur_list = []
        self.pos_tag = set()
        self.morphemes = []
        self.meaning = ''
        self.root = ''
        self.suffix = ''
        self.numero = ''
        self.genero = ''
        self.pessoa = ''
        self.grau = ''
        self.modo = ''
        self.tempo = ''
        self.lemmas = set()


dword_list = []

# abre o arquivo json e coloca o conteúdo em uma variavel tipo dicionario
essays_dict = json.loads(open('datasets/one_topic_essays.json', encoding='utf-8').read())

# transforma as redacoes em uma unica string tudo junta
essays_in_one_string = ""
# essays_in_one_string_normalized = ""
for e in essays_dict:
    essays_in_one_string += e['text']

# lista de tokens a partir da string
initial_tokens = nltk.word_tokenize(essays_in_one_string)

# normaliza a lista de tokens
tokens = [word.lower() for word in initial_tokens]
tokens_without_punc = [word.lower() for word in initial_tokens if word.isalpha()]

# lista de tokens únicos no texto
unique_tokens = list(set(tokens_without_punc))

# distribuição de frequência
frequency_dist = nltk.FreqDist(tokens_without_punc)

# stemmer para o português
stemmer = nltk.stem.RSLPStemmer()

# gerando as setenças do texto com as classes gramaticiais associadas às palavras
tagged_sentences = pt_tagger.tag_sentences(essays_in_one_string)
tagged_words = []
for s in tagged_sentences:
    for w in s:
        tagged_words.append(w)

# lemmatizando as palavras
lemmatized_words = lemmatizer.atalho()
lemmatized_words_n = [word.lower() for word in lemmatized_words]

# pegando o significado das palavras
with open('dic_api/meanings.txt', 'r', encoding='utf-8') as f:
    meanings_list = f.read().splitlines()
with open('dic_api/words_to_search_for_meaning.txt', 'r', encoding='utf-8') as f:
    words_to_search_for_meaning = f.read().splitlines()

words_and_meanings = dict(zip(words_to_search_for_meaning, meanings_list))

# pegando os morfemas de cada palavra
all_words_in_text = Text(essays_in_one_string, 'pt').words
word_morphemes = [(w, w.morphemes) for w in all_words_in_text]

cont = 0
for t in unique_tokens:
    d = DWord()
    d.id = cont
    d.word = t
    stem = stemmer.stem(t)
    d.root = stem
    d.suffix = t[len(stem):]
    d.freq = frequency_dist[t]
    d.pos_tag = set([tt for (w, tt) in tagged_words if w == t])
    pos = 0
    for w in words_to_search_for_meaning:
        if t == w:
            d.meaning = meanings_list[pos]
            break
        pos += 1
    for (w, ms) in word_morphemes:
        if w == t:
            d.morphemes = ms
            break
    pos = 0
    for word in tokens:
        if word == t:
            d.occur_list.append(pos)
        pos += 1
    for o in d.occur_list:
        d.lemmas.add(lemmatized_words_n[o])
    if d.meaning == '':
        for l in d.lemmas:
            m = words_and_meanings[l]
            if m != '':
                d.meaning = m
                break
    cont += 1
    dword_list.append(d)

dword_list_1 = [x for x in dword_list if len(x.pos_tag) <= 1]
dword_list_mais_1 = [x for x in dword_list if len(x.pos_tag) > 1]
for e in dword_list_mais_1:
    for t in e.pos_tag:
        o = e
        o.pos_tag = set()
        o.pos_tag.add(t)
        dword_list_1.append(o)
dword_list = dword_list_1

# filehandler = open('arq.objs', 'wb')
# pickle.dump(dword_list, filehandler)

lemmas_list = list(set(lemmatized_words_n))

lemmas_and_their_tokens = []
for l in lemmas_list:
    o = dict()
    o['lemma'] = l
    o['tokens'] = set()
    lemmas_and_their_tokens.append(o)

for o in lemmas_and_their_tokens:
    for ind, lw in enumerate(lemmatized_words_n):
        if o['lemma'] == lw:
            o['tokens'].add((tokens[ind], frequency_dist[tokens[ind]]))

for lt in lemmas_and_their_tokens:
    if len(lt['tokens']) > 1:
        print(lt)

fileh = open('lista_bases.objs', 'wb')
pickle.dump(lemmas_and_their_tokens, fileh)
