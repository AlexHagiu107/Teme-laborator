sentence = input("Introdu propoziția: ")

words = []
current_word = ""

for char in sentence:
    if char != " ":
        current_word += char
    else:
        if current_word != "":
            words.append(current_word)
            current_word = ""

if current_word != "":
    words.append(current_word)

reversed_sentence = ""
for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i]
    if i != 0:
        reversed_sentence += " "

print("Propoziția inversată este:")
print(reversed_sentence)
