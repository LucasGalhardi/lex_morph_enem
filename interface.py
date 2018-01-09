import pickle
import json
import nltk
import operator

tags_dict = {
    'ADP': 'Adposição',
    '.': 'Pontuação',
    'ADV': 'Advérbio',
    'DET': 'Determinante',
    'NOUN': 'Substantivo',
    'VERB': 'Verbo',
    'NUM': 'Numeral',
    'PRT': 'Particle',
    'PRON': 'Pronome',
    'ADJ': 'Adjetivo',
    'CONJ': 'Conjunção'
}

numero_dict = {
    's': 'singular',
    'p': 'plural'
}

genero_dict = {
    'm': 'masculino',
    'f': 'feminino',
    'a': 'ambos',
    'u': 'uniforme'
}

grau_dict = {
    'b': 'original',
    'a': 'aumentativo',
    'd': 'diminutivo',
    'c': 'comparativo',
    's': 'superlativo'
}

tempo_dict = {
    'pass': 'passado',
    'pre': 'presente',
    'f': 'futuro'
}


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

fileh = open('lista_bases.objs', 'rb')
lemmas_and_their_tokens = pickle.load(fileh)

dword_list.sort(key=operator.attrgetter('word'))
lemmas_and_their_tokens.sort(key=operator.itemgetter('lemma'))

while True:
    print("1 - Lista de Bases")
    print("2 - Lista de Palavras")
    print("3 - Sair")
    op = int(input("Escolha: "))
    if op == 1:
        print("\n" * 12, end='')
        while True:
            print("1 - Ver lista das palavras bases")
            print("2 - Consulta palavra")
            print("3 - Voltar")
            op2 = int(input("Escolha: "))
            if op2 == 1:
                for i in lemmas_and_their_tokens:
                    print(i['lemma'])
            elif op2 == 2:
                palavra = input("Palavra: ")
                found = False
                tks = {}
                for ind, i in enumerate(lemmas_and_their_tokens):
                    if i['lemma'] == palavra:
                        tks = lemmas_and_their_tokens[ind]['tokens']
                        found = True
                        break
                if found:
                    print("A base " + palavra + " aparece nas seguinte formas: ")
                    for (t, f) in tks:
                        print(t + " aparece " + str(f) + " vezes no texto.")
                else:
                    print("Palavra não existente")
            elif op2 == 3:
                print("\n" * 12, end='')
                break
            else:
                print("Escolha um número válido")
    elif op == 2:
        print("\n" * 12, end='')
        while True:
            print("1 - Ver lista das palavras")
            print("2 - Consulta palavra")
            print("3 - Voltar")
            op3 = int(input("Escolha: "))
            if op3 == 1:
                for dw in dword_list:
                    print(dw.word)
            elif op3 == 2:
                palavra = input("Palavra: ")
                found = False
                word = DWord()
                for dw in dword_list:
                    if dw.word == palavra:
                        word = dw
                        found = True
                        break
                if found:
                    print("Palavra: " + word.word)
                    print("Significado: " + word.meaning)
                    print("Frequência: " + str(word.freq))
                    tag = word.pos_tag.pop()
                    print("Classe gramatical: " + tags_dict[tag])
                    word.pos_tag.add(tag)
                    print("Morfemas: ")
                    for m in word.morphemes:
                        print("     " + m)
                    print("Ocorrências no texto: ")
                    for ind, oc in enumerate(word.occur_list, start=1):
                        print("     " + str(ind) + ". " + ' '.join(tokens[oc - 5:oc + 6]))
                    print("Raiz: " + word.root)
                    print("Sufixo: " + word.suffix)
                    print("Lemmas: ")
                    for l in word.lemmas:
                        print("     " + l)
                    if tag == 'NOUN':
                        print("Número: " + numero_dict[word.numero])
                        print("Gênero: " + genero_dict[word.genero])
                        print("Grau: " + grau_dict[word.grau])
                    elif tag == 'ADJ':
                        print("Número: " + numero_dict[word.numero])
                        print("Gênero: " + genero_dict[word.genero])
                        print("Grau: " + grau_dict[word.grau])
                    elif tag == 'VERB':
                        if word.pessoa == 'i' and word.numero == 'i' and word.tempo == 'i':
                            print("Verbo no infinitivo")
                        elif word.pessoa == 'g' and word.numero == 'g' and word.tempo == 'g':
                            print("Verbo no gerúndio")
                        elif word.pessoa == 'p' and word.numero == 'p' and word.tempo == 'p':
                            print("Verbo no particípio")
                        else:
                            print("Pessoa: " + word.pessoa + "ª")
                            print("Número: " + numero_dict[word.numero])
                            print("Tempo: " + tempo_dict[word.tempo])
                    elif tag == 'PRON':
                        print("Número: " + numero_dict[word.numero])
                        print("Pessoa: " + word.pessoa + "ª")
                        print("Gênero: " + genero_dict[word.genero])
                else:
                    print("Palavra não existente")
            elif op3 == 3:
                print("\n" * 12, end='')
                break
            else:
                print("Escolha um número válido")
    elif op == 3:
        print("\n" * 12, end='')
        break
    else:
        print("Escolha um número válido")
