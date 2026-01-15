def count_words_in_file(filename):
    file = open(filename, "r", encoding="utf-8")
    text = file.read()
    file.close()

    words = text.split()
    return len(words)


# Exemplu de utilizare
filename = "ex1.txt"
result = count_words_in_file(filename)
print("Numărul total de cuvinte este:", result)
