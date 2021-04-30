import nltk

words = ["men",  "teacher", "men", "woman"]
FreqDist = nltk.FreqDist(words)

for i,j in FreqDist.items():
    print(i, "---", j)