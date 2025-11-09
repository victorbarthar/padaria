value = int(input())
for i in range(1, 1000):
    valor = int(input())
    if valor % 2 == 0 and valor != 0:
        if valor > 0:
            print("EVEN POSITIVE")
        elif valor < 0:
            print("EVEN NEGATIVE")
    elif valor % 2 != 0:
        if valor > 0:
            print("ODD POSITIVE")
        elif valor < 0:
            print("ODD NEGATIVE")
    elif valor == 0:
        print("NULL")
