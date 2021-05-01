import nltk
import ssl

# sirve para categorizar las palabras en verbos , accionres , sustantivos , etc
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('averaged_perceptron_tagger')

words = "Learning python was such an amazing experience for me"

words_es = "The boy play with the ball"

world_tokenize = nltk.word_tokenize(words)

world_tokenize_esp = nltk.word_tokenize(words_es)

print(nltk.pos_tag(world_tokenize))

print(nltk.pos_tag(world_tokenize_esp))
