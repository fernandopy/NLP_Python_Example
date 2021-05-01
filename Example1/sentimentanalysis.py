# pip install textblob

from textblob import TextBlob

joe_biden_tweet = "Small bussinesses need relief, " \
                  "but many were muscled out of the way by big companies last year"

happy = "I am very very happy"
joe = TextBlob(joe_biden_tweet)

h = TextBlob(happy)
#polarity -1, 1 with -1 ids very negative and +1 very positive
# subjectivity ranges 0, 1 se refiere a la opinion d elas personas emocion incluso el juicio
# mientras más grande el número más subjetivo es el texto
print(joe.sentiment)

print(h.sentiment)
