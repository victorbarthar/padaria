#Variáveis Base
nomes_fila = ["Ana","Bia","Carol","Diogo","Elison","Flávio","Gabriel","Heitor","Hugo","Igor","João"]
idades_fila = [25, 17, 30, 15, 19, 18, 12, 22, 45, 16]
convidados_permitidos= []
for i in range(len(nomes_fila)):
    nome_atual= nomes_fila[i]
    idade_atual = idades_fila[i]
    if idade_atual >= 18:
        convidados_permitidos.append(nome_atual)
        
# Resultado
print(f" A fila tinha: {nomes_fila}")
print(f"Autorizados: {convidados_permitidos}")