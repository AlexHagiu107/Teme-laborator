def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

cuvant = input("Introdu un cuvant: ")

if is_palindrome(cuvant):
    print(f"'{cuvant}' este un palindrom.")
else:
    print(f"'{cuvant}' nu este un palindrom.")
