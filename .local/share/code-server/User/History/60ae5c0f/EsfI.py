value = input()
x = value.split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
if a >= (b+c):
    print("NAO FORMA TRIANGULO")
elif a**2 == (b**2 + c**2):
    print("TRIANGULO RETANGULO")
    if a == b and b == c and a == c:
        print("TRIANGULO EQUILATERO")
    elif b == c or a == b or a == c:
        print("TRIANGULO ISOSCELES")
elif a**2 > (b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")
    if a == b and b == c and a == c:
        print("TRIANGULO EQUILATERO")
    elif b == c or a == b or a == c:
        print("TRIANGULO ISOSCELES")
elif a**2 < (b**2 + c**2):
    if a == b and b == c and a == c:
        print("TRIANGULO EQUILATERO")
    elif b == c or a == b or a == c:
        print("TRIANGULO ISOSCELES")
