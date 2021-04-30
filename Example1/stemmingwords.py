import nltk
import ssl

# First step download puntkt
# Stemming words
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')

from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["Loving", "Chocolate", "Soñando", "Retrieved", "Being"]

for i in words:
    print(ps.stem(i))
