import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1 = float(input("Introdu x1: "))
y1 = float(input("Introdu y1: "))
x2 = float(input("Introdu x2: "))
y2 = float(input("Introdu y2: "))

# Calcularea distantei
distanta = distance(x1, y1, x2, y2)

print("Distanta dintre cele doua puncte este:", distanta)
