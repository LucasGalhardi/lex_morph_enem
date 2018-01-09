import os


def lemmatize(tagged_sentences):
    word_list = []
    tag_list = []
    conversion_tags = {
        'ADP': 'n',
        '.': 'punc',
        'ADV': 'adv',
        'DET': 'art',
        'NOUN': 'n',
        'VERB': 'v',
        'NUM': 'num',
        'PRT': 'n',
        'PRON': 'pron',
        'ADJ': 'adj',
        'CONJ': 'n',
    }
    for t in tagged_sentences:
        for (w, tag) in t:
            word_list.append(w.lower())
            tag_list.append(conversion_tags[tag])

    file = open('lemmatizer/lista_palavras.txt', 'w', encoding='utf-8')
    for w in word_list:
        file.write(w + '\n')
    file.close()
    file = open('lemmatizer/lista_tags.txt', 'w', encoding='utf-8')
    for t in tag_list:
        file.write(t + '\n')
    file.close()

    tags_path = os.getcwd() + os.sep + "lemmatizer/lista_tags.txt"
    words_path = os.getcwd() + os.sep + "lemmatizer/lista_palavras.txt"
    lemmas_path = os.getcwd() + os.sep + "lemmatizer/lista_lemmas.txt"

    os.system('java -jar lemmatizer/lemmatizer.jar ' + words_path + ' ' + tags_path + ' ' + lemmas_path)

    with open('lemmatizer/lista_lemmas.txt', 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def atalho():
    with open('lemmatizer/lista_lemmas.txt', 'r', encoding='utf-8') as f:
        return f.read().splitlines()
