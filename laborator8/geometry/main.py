from circle import aria_cercului, circumferinta_cercului
from rectangle import aria_dreptunghiului, perimetru_dreptunghiului

r = float(input("Introdu raza cercului: "))
l = float(input("Introdu lungimea dreptunghiului: "))
w = float(input("Introdu lățimea dreptunghiului: "))

print("Aria cercului:", aria_cercului(r))
print("Circumferința cercului:", circumferinta_cercului(r))

print("Aria dreptunghiului:", aria_dreptunghiului(l, w))
print("Perimetrul dreptunghiului:", perimetru_dreptunghiului(l, w))
