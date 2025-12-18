# Program pentru index inversat
n = int(input("Introdu numărul de documente: "))
documents = []
for i in range(n):
    doc = input(f"Document {i}: ")
    documents.append(doc)

index = {}
for i, doc in enumerate(documents):
    words = doc.lower().split()
    for word in words:
        if word in index:
            index[word].add(i)
        else:
            index[word] = {i}

print("Index inversat:", index)
