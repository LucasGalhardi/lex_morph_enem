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

idd = input("Em qual numero vc parou?")
iddd = int(idd)
var = True
while var:
    o = dword_list[iddd]
    print("ID: " + str(o.id))
    print("Palavra: " + o.word.upper())
    if o.meaning == '':
        o.meaning = input("Significado?")
    if len(o.pos_tag) < 1:
        popped = input("Classe: ")
    else:
        popped = o.pos_tag.pop()
    if popped in {'NOUN', 'VERB', 'ADJ', 'PRON'}:
        r = input("É " + popped + "? (s, n)")
        if r == 'n':
            print("ocorrências: ")
            for oc in o.occur_list:
                print("1: " + ' '.join(tokens[oc-5:oc+5]))
            popped = input("Classe: ")
    print("\n" * 3, end='')
    if popped == 'NOUN':
        o.numero = input("Numero? (s, p)")
        o.genero = input("Gênero? (m, f, a)")
        o.grau = input("Grau? (b, a, d)")
    elif popped == 'ADJ':
        o.numero = input("Numero? (s, p)")
        o.genero = input("Gênero? (m, f, u)")
        o.grau = input("Grau? (b, c, s)")
    elif popped == 'VERB':
        o.genero = input("Pessoa? (1, 2, 3, 2/3)")
        o.numero = input("Numero? (s, p)")
        o.grau = input("Tempo? (pre, pass, f)")
    elif popped == 'PRON':
        o.numero = input("Numero? (s, p)")
        o.genero = input("Pessoa? (1, 2, 3, 2/3)")
        o.grau = input("Gênero? (m, f)")
    else:
        o.pos_tag.add(popped)
        dword_list[iddd] = o
        print("\n" * 10, end='')
        iddd = iddd + 1
        continue
    o.pos_tag.add(popped)
    dword_list[iddd] = o
    maisUm = input("Mais uma palavra? (s ou n ou m)")
    if maisUm == 'n':
        var = False
    elif maisUm == 'm':
        print("\n" * 10, end='')
        continue
    print("\n" * 10, end='')
    iddd = iddd + 1


# file = open('arq.objs', 'wb')
# pickle.dump(dword_list, file)


