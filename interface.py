import pickle
import json
import nltk


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

file = open('arq.objs', 'rb')
dword_list = pickle.load(file)
