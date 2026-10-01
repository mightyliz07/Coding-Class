sentence = input("enter a sentence: ")
counts = {}

for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1

print(counts)