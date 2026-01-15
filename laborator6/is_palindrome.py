text = input("Introdu textul: ")

cleaned_text = ""

for char in text:
    if char != " ":
        if "A" <= char <= "Z":
            cleaned_text += chr(ord(char) + 32)
        else:
            cleaned_text += char

left = 0
right = len(cleaned_text) - 1
is_palindrome = True

while left < right:
    if cleaned_text[left] != cleaned_text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print("Este palindrom?")
print(is_palindrome)
