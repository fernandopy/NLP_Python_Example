import nltk
import ssl

# First step download puntkt
# StopWords include commonly used word
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')

from nltk.corpus import stopwords

stopwords = stopwords.words("english")
print(stopwords)

Text = ["Good", "morning", "How", "you", "doing", "Are", "you", "coming", "tonight"]

for i in Text:
    if i not in stopwords:
        print(i)
