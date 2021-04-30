import nltk
import ssl

# First step download puntkt
# Tokenization  proccess of separating a paragraph into chunks or words
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')

from nltk.tokenize import word_tokenize,sent_tokenize

text = "Good morning, How  you doing? Are you coming tonight?"

# split text into Words and symbols
Tokenized = word_tokenize(text)

#split text into sentences

tokenized_sent = sent_tokenize(text)

print(Tokenized)
print(tokenized_sent)
