a = input()
b = input()
resultado = a/b
try:
    primeiro = float(a)
    segundo = float(b)
    print(resultado)
except ValueError:
    print("Erro:Você precisa digitar números.")
except ZeroDivisionError:
    if b == 0:
        print("Erro: Não é possível dividir por zero.")
print("Programa finalizado.")