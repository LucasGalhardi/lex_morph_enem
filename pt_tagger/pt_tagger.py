import nltk
import pickle


def tag_sentences(text):
    tagger = pickle.load(open('pt_tagger/tagger.pkl', 'rb'))
    portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")
    sentences = portuguese_sent_tokenizer.tokenize(text)
    return [tagger.tag(nltk.word_tokenize(sentence)) for sentence in sentences]
