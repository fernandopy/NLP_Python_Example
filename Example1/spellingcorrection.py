from textblob import TextBlob

text = "Smalle businesses neede reliefe"

texto = "eres mi pero faborito"

spelling_mistakes = TextBlob(text)

spanis_mistakes = TextBlob(texto)

print(spelling_mistakes.correct())

print(spelling_mistakes.detect_language())



print(spanis_mistakes.correct())

print(spanis_mistakes.detect_language())