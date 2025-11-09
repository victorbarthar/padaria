value = input()
x = value.split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
p = a+b+c
a = ((a+b)*c)/2
if (a + b) > c and (b + c) > a and (a + c) > b:
    print(f"Perimetro = {p:.1f}")
else:
    print(f"Area = {a:.1f}")