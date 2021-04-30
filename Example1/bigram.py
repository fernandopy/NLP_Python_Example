import nltk



# ESTO ES MUY UTIL PARA IDENTIFICAR EL SPAM
words = "Learning python was such an amazing experience for me"
word_tokenize = nltk.word_tokenize(words)

print(list(nltk.bigrams(word_tokenize)))

print(list(nltk.trigrams(word_tokenize)))

print(list(nltk.ngrams(word_tokenize, 4)))

