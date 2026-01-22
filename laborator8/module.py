import math

num = int(input("Introdu un număr: "))
angle = float(input("Introdu un unghi în grade: "))

# Rădăcina pătrată
sqrt_num = math.sqrt(num)

# Factorial
fact_num = math.factorial(num)

# Sinus (grade → radiani)
sin_angle = math.sin(math.radians(angle))

print(f"Rădăcina pătrată a {num} este {sqrt_num}")
print(f"Factorialul lui {num} este {fact_num}")
print(f"Sinusul unghiului de {angle} grade este {sin_angle}")
