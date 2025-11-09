value = input()
x = value.split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
a > b and  a > c
if a >= (b+c):
    print("NAO FORMA TRIANGULO")
elif a**2 == (b**2 + c**2):
    print("TRIANGULO RETANGULO")
elif a**2 > (b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")
elif a**2 < (b**2 + c**2):
    print("TRIANGULO ACUTANGULO")
    break
if a == b == c:
    print("TRIANGULO EQUILATERO")
elif b == c:
    print("TRIANGULO ISOSCELES")
    