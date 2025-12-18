import string

text = input("Introdu textul: ")

# Transformam textul la litere mici si eliminam punctuatia
text = text.lower().translate(str.maketrans('', '', string.punctuation))

words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Frecvența cuvintelor:", freq)
