a = input()
b = input()
try:
    primeiro = float(a)
    segundo = float(b)
    resultado = primeiro / segundo
    print(resultado)
except ValueError:
    print("Erro: Você precisa digitar números.")
except ZeroDivisionError:
    if b == 0:
        print("Erro: Não é possível dividir por zero.")
else: 
    print("Programa finalizado.")