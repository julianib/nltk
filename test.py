import nltk
import re
import pprint
# nltk.download("punkt")
from nltk import word_tokenize
from nltk.probability import FreqDist
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()


# open and read
with open("raw_corpus.txt", "r") as f:
    corpus = f.readline()  # file is 1 line


# preprocessing
# lower
corpus = corpus.lower()
# no abbreviations
corpus = corpus.replace("n't", " not").replace("t's", "t is")
# no quotes
corpus = corpus.replace("\" ", "\n")
corpus = corpus.replace(" \"", "\n")
# no punctuation
corpus = corpus.replace("! ", "\n").replace(
    "? ", "\n").replace(". ", "\n").replace(", ", "\n")
# get sentences in a list
sentences = corpus.split("\n")


# save new corpus
with open("corpus.txt", "w") as f:
    f.write(corpus)


# print corpus
print(corpus)


# frequency distribution
joined_text = ' '.join(sentences)
tokenized_text = nltk.tokenize.word_tokenize(joined_text)
fdist = FreqDist(tokenized_text)


# show corpus stats
print(f"sentences: {len(sentences)}")

hapaxes = fdist.hapaxes()  # hapaxes = unique words
print(f"hapaxes: {len(hapaxes)}")

total_words = 0
for sentence in sentences:
    words_in_sentence = len(sentence.split())
    total_words += words_in_sentence

print(f"total words: {total_words}")

average_length = total_words / len(sentences)
print(f"average sentence length: {average_length}")

print(f"top 30 common words: {fdist.most_common(30)}")
