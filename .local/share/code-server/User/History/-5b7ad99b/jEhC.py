#Variáveis Base
idades_fila = [25, 17, 30, 15, 19, 18, 12, 22, 45, 16]
convidados_permitidos= []
for idade in idades_fila:
    if idade >= 18:
        convidados_permitidos.append(idade)
        
# Resultado
print(f" A fila tinha: {idades_fila}")
print(f"Autorizados: {convidados_permitidos}")

