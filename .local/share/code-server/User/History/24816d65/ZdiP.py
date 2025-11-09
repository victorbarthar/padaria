numero_secreto = 16
palpite = 0
while palpite != numero_secreto:
    try:
        palpite = int(input())
    except ValueError:
        
print("Parabéns, você acertou!")