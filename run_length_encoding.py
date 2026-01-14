text = input("Introdu șirul de caractere: ")

if len(text) == 0:
    print("")
else:
    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1

    encoded += text[-1] + str(count)

    print("Șirul codificat este:")
    print(encoded)
