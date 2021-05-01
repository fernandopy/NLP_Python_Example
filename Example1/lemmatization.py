import nltk
import ssl
# Lematizar implica estandarizar, desambiguar, segmentar y,
# en caso de usar programas de lematización automática, también etiquetar
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download("wordnet")

from nltk.stem import WordNetLemmatizer

lem = WordNetLemmatizer()
print(lem.lemmatize("believes"))
print(lem.lemmatize("mesas"))
print(lem.lemmatize("stripes"))
print(lem.lemmatize("eramos"))

# si quieres obtener el verbo o el adjetivo de la palabra

print("------------------------------------")
print(lem.lemmatize("believes", pos="v"))
print(lem.lemmatize("mesas", pos="v"))
print(lem.lemmatize("stripes", pos="v"))
print(lem.lemmatize("beauty", pos="a"))
