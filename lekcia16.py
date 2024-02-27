#Testovanie lekcia 16

import math

class Kalkulacka:
    def sucet(self, a, b):
        return a + b

    def sucin(self, a, b):
        return a * b

    def delenie(self, a, b):
        if b == 0:
            return "Nemožno deliť nulou"
        else:
            return a / b

    def dlzka_odvesny(self, a, b):
        return math.sqrt(a**2 + b**2)

    def kvadraticka_rovnica(self, a, b, c):
        d = b**2 - 4*a*c
        if d < 0:
            return "Komplexné korene"
        elif d == 0:
            x = -b / (2*a)
            return [x, x]
        else:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            return [x1, x2]

# Testovanie funkcionality
kalkulacka = Kalkulacka()

print("Súčet: ", kalkulacka.sucet(5, 3))
print("Súčin: ", kalkulacka.sucin(5, 3))
print("Delenie: ", kalkulacka.delenie(6, 2))
print("Dĺžka odvesny: ", kalkulacka.dlzka_odvesny(3, 4))
print("Kvadratická rovnica: ", kalkulacka.kvadraticka_rovnica(1, -3, 2))

