a = inout()
b = input()
x = a/b
try:
    primeiro = float(a)
    segundo = float(b)
except ValueError:
    print("Erro:Você precisa digitar números.")
except ZeroDivisionError:
    if b == 0:
        print("Erro: 