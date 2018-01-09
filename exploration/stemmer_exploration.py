import json
import nltk

# abre o arquivo json e coloca o conteúdo em uma variavel tipo dicionario
essays_dict = json.loads(open('../datasets/one_topic_essays.json', encoding='utf-8').read())

# transforma as redacoes em uma unica string tudo junta
essays_in_one_string = ""
# essays_in_one_string_normalized = ""
for e in essays_dict:
    essays_in_one_string += e['text']
    # for w in e['text']:
    #     if w.isalpha():
    #         essays_in_one_string_normalized += w.lower()

# lista de tokens a partir da string
initial_tokens = nltk.word_tokenize(essays_in_one_string)

tokens = [word.lower() for word in initial_tokens if word.isalpha()]

# palavras "stemmadas"
stemmer = nltk.stem.RSLPStemmer()
stemmed_words = [(w, stemmer.stem(w)) for w in tokens]

for (w, s) in stemmed_words:
    print(w.upper() + ": " + str(s))


only_stemmed = [s for (w, s) in stemmed_words]

pairs = []
for s_w in set(only_stemmed):
    for (w, s_w2) in stemmed_words:
        if s_w == s_w2:
            # print("STEM: " + s_w + " and WORD: " + w)
            pairs.append((s_w, w))
selected_pairs = []
for p1 in set(pairs):
    cont = 0
    for p2 in set(pairs):
        if p1[0] == p2[0]:
            cont += 1
    if cont > 1:
        selected_pairs.append(p1)
