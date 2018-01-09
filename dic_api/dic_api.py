import requests
import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleanr2 = re.compile('_')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = re.sub(cleanr2, '', cleantext)
    return cleantext


def get_word_meaning(word):
    print(word)
    response = requests.get("http://dicionario-aberto.net/search-json/" + word)
    if response.status_code == 200:
        json_response = response.json()
        if 'entry' in json_response:
            significado = json_response['entry']['sense'][0]['def']
            return cleanhtml(significado)
        elif 'superEntry' in json_response:
            significado = json_response['superEntry'][0]['entry']['sense'][0]['def']
            return cleanhtml(significado)
        else:
            return ""
    else:
        return ""


with open('words_to_search_for_meaning.txt', 'r', encoding='utf-8') as f:
    words_to_search = f.read().splitlines()

file = open('meanings.txt', 'a', encoding='utf-8')
for w in words_to_search[1520:]:
    meaning = get_word_meaning(w)
    file.write(meaning + '\n')
file.close()
