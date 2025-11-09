a = inout()
b = input()
x = a/b
try:
    primeiro = float(a)
    segundo = float(b)
except ValueError:
    print(f"{a} não é um número")