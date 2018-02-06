import pickle
import json
import nltk
import operator
import string
from colorama import Fore, Style

tags_dict = {
    'ADP': 'Adposição (Preposição)',
    '.': 'Pontuação',
    'ADV': 'Advérbio',
    'DET': 'Determinante',
    'NOUN': 'Substantivo',
    'VERB': 'Verbo',
    'NUM': 'Numeral',
    'PRT': 'Particle',
    'PRON': 'Pronome',
    'ADJ': 'Adjetivo',
    'CONJ': 'Conjunção',
    'CNT': 'Contração'
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

file = open('arq2.objs', 'rb')
dword_list2 = pickle.load(file)

words_in_list2 = set([dw.word for dw in dword_list2])
dword_list3 = [dw for dw in dword_list if dw.word not in words_in_list2]

dword_list3.extend(dword_list2)

fileh = open('lista_bases.objs', 'rb')
lemmas_and_their_tokens = pickle.load(fileh)

dword_list3.sort(key=operator.attrgetter('word'))
lemmas_and_their_tokens.sort(key=operator.itemgetter('lemma'))

while True:
    print("1 - Lista de Bases")
    print("2 - Lista de Palavras")
    print("3 - Sair")
    op = input("Escolha: ")
    if op == '1':
        print("\n" * 12, end='')
        while True:
            print("1 - Ver lista das palavras bases")
            print("2 - Ver lista das palavras bases que começam com '.'")
            print("3 - Consulta palavra")
            print("4 - Voltar")
            op2 = input("Escolha: ")
            if op2 == '1':
                print(Fore.BLUE)
                for i in lemmas_and_their_tokens:
                    print(i.get('lemma', ''))
                print(Style.RESET_ALL)
                continue
            if op2 == '2':
                letter = input("Letra: ")
                if letter not in string.ascii_letters:
                    print(Fore.RED)
                    print("Digite apenas 1 letra")
                    print(Style.RESET_ALL)
                    continue
                else:
                    print(Fore.BLUE)
                    for i in lemmas_and_their_tokens:
                        i_lemma = i.get('lemma', '')
                        if i_lemma != '':
                            if i['lemma'].startswith(letter):
                                print(i['lemma'])
                    print(Style.RESET_ALL)
                continue
            elif op2 == '3':
                palavra = input("Palavra: ")
                print(Fore.BLUE)
                found = False
                tks = {}
                for ind, i in enumerate(lemmas_and_their_tokens):
                    i_lemma = i.get('lemma', '')
                    if i_lemma == palavra:
                        tks = lemmas_and_their_tokens[ind]['tokens']
                        found = True
                        break
                if found:
                    print("A base " + Fore.GREEN +
                          palavra + Fore.BLUE + " aparece nas seguinte formas: ")
                    for ind, (t, f) in enumerate(tks, start=1):
                        print("     " + str(ind) + ". " + Fore.GREEN +
                              t + Fore.BLUE + " aparece " +
                              Fore.GREEN + str(f) + Fore.BLUE + " vez(es) no texto.")
                else:
                    print(Fore.RED)
                    print("Palavra não existente")
                    print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                continue
            elif op2 == '4':
                print("\n" * 12, end='')
                break
            else:
                print(Fore.RED)
                print("Escolha um número váliddo")
                print(Style.RESET_ALL)
    elif op == '2':
        print("\n" * 12, end='')
        while True:
            print("1 - Ver lista das palavras")
            print("2 - Ver lista das palavras que começam com '.'")
            print("3 - Consulta palavra")
            print("4 - Voltar")
            op3 = input("Escolha: ")
            if op3 == '1':
                print(Fore.BLUE)
                for dw in dword_list3:
                    print(dw.word)
                print(Style.RESET_ALL)
                continue
            if op3 == '2':
                letter = input("Letra: ")
                if letter not in string.ascii_letters:
                    print(Fore.RED)
                    print("Digite apenas 1 letra")
                    print(Style.RESET_ALL)
                else:
                    print(Fore.BLUE)
                    for dw in dword_list3:
                        if dw.word.startswith(letter):
                            print(dw.word)
                    print(Style.RESET_ALL)
                continue
            elif op3 == '3':
                palavra = input("Palavra: ")
                found = False
                found_words = []
                for dw in dword_list3:
                    if dw.word == palavra:
                        found_words.append(dw)
                        found = True
                if found:
                    for word in found_words:
                        print("----------------------------------------------------------------")
                        print(Fore.BLUE)
                        print("ID: " + Fore.GREEN + str(word.id) + Fore.BLUE)
                        print("Palavra: " + Fore.GREEN + word.word + Fore.BLUE)
                        print("Significado: " + Fore.GREEN + word.meaning + Fore.BLUE)
                        tag = word.pos_tag.pop()
                        print("Classe gramatical: " + Fore.GREEN + tags_dict.get(tag, '') + Fore.BLUE)
                        word.pos_tag.add(tag)
                        print("Frequência: " + Fore.GREEN + str(word.freq) + Fore.BLUE)
                        print("Ocorrências no texto: ")
                        print(Fore.GREEN)
                        for ind, oc in enumerate(word.occur_list, start=1):
                            print("     " + str(ind) + ". " + ' '.join(tokens[oc - 5:oc]) +
                                  Fore.RED + ' ' + tokens[oc] + ' ' + Fore.GREEN +
                                  ' '.join(tokens[oc + 1:oc + 6]))
                        print(Fore.BLUE)
                        print("Lemma: ")
                        print(Fore.GREEN)
                        for l in word.lemmas:
                            print("     " + l)
                        print(Fore.BLUE)
                        print("Raiz: " + Fore.GREEN + word.root + Fore.BLUE)
                        print("Sufixo: " + Fore.GREEN + word.suffix + Fore.BLUE)
                        print("Morfemas: ")
                        print(Fore.GREEN)
                        for m in word.morphemes:
                            print("     " + m)
                        print(Fore.BLUE)
                        if tag == 'NOUN':
                            print("Número: " + Fore.GREEN + numero_dict.get(word.numero, '') + Fore.BLUE)
                            print("Gênero: " + Fore.GREEN + genero_dict.get(word.genero, '') + Fore.BLUE)
                            print("Grau: " + Fore.GREEN + grau_dict.get(word.grau, '') + Fore.BLUE)
                        elif tag == 'ADJ':
                            print("Número: " + Fore.GREEN + numero_dict.get(word.numero, '') + Fore.BLUE)
                            print("Gênero: " + Fore.GREEN + genero_dict.get(word.genero, '') + Fore.BLUE)
                            print("Grau: " + Fore.GREEN + grau_dict.get(word.grau, '') + Fore.BLUE)
                        elif tag == 'VERB':
                            print(Fore.GREEN)
                            if word.pessoa == 'i' and word.numero == 'i' and word.tempo == 'i':
                                print("Verbo no infinitivo")
                                print(Fore.BLUE)
                            elif word.pessoa == 'g' and word.numero == 'g' and word.tempo == 'g':
                                print("Verbo no gerúndio")
                                print(Fore.BLUE)
                            elif word.pessoa == 'p' and word.numero == 'p' and word.tempo == 'p':
                                print("Verbo no particípio")
                                print(Fore.BLUE)
                            else:
                                print(Fore.BLUE)
                                print("Pessoa: " + Fore.GREEN + word.pessoa + "ª" + Fore.BLUE)
                                print("Número: " + Fore.GREEN + numero_dict.get(word.numero, '') + Fore.BLUE)
                                print("Tempo: " + Fore.GREEN + tempo_dict.get(word.tempo, '') + Fore.BLUE)
                        elif tag == 'PRON':
                            print("Número: " + Fore.GREEN + numero_dict.get(word.numero, '') + Fore.BLUE)
                            print("Pessoa: " + Fore.GREEN + word.pessoa + "ª" + Fore.BLUE)
                            print("Gênero: " + Fore.GREEN + genero_dict.get(word.genero, '') + Fore.BLUE)
                        print(Style.RESET_ALL)
                        print("----------------------------------------------------------------")
                        continue
                else:
                    print(Fore.RED)
                    print("Palavra não existente")
                    print(Style.RESET_ALL)
                    continue
            elif op3 == '4':
                print("\n" * 12, end='')
                break
            else:
                print(Fore.RED)
                print("Escolha um número válido")
                print(Style.RESET_ALL)
    elif op == '3':
        print("\n" * 12, end='')
        break
    else:
        print(Fore.RED)
        print("Escolha um número válido")
        print(Style.RESET_ALL)
