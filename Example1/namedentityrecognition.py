import nltk
import ssl

# sirve para contestar preguntas de fuentes de datos no estructuiradas
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('maxent_ne_chunker')
nltk.download('words')

text = "The russian president Vladimir Putin is in the Kremlin"

tokenize = nltk.word_tokenize(text)
print(tokenize)
pos_tags = nltk.pos_tag(tokenize)
print(pos_tags)
nameEn = nltk.ne_chunk(pos_tags)
print(nameEn)
