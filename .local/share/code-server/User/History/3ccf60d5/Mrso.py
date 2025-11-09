#Conceituação Inicial
nomes = []
quantidades= []
preco = []
custo_total= 0

while True:
    nome_produto= input("Produto? ")
    quantidade_texto= input("Quantidade? ")
    quantidade_numero= float(quantidade_texto)
    preco_texto= input("Preço? ")
    preco_numero= float(preco_texto)
    nomes.append(nome_produto)
    quantidades.append(quantidade_numero)
    preco.append(preco_numero)
    total_do_item= quantidade_numero * preco_numero
    custo_total += total_do_item
    fim= input("Adicionar mais itens? S OU N ")
    if fim != "S":
        break
#Recibo

print("PADARIA PEGA NO MEU CASSETINHO")
for i in range(len(nomes)):
    nomefinal = nomes[i]
    quantidadefinal= quantidades[i]
    precofinal= preco[i]
    total_item_recebido = quantidadefinal * precofinal
    print(f"\nNome: {nomefinal}, Qtd: {quantidadefinal}, Preço Unitário: R$ {precofinal}, Total do Item: R$ {total_item_recebido:.2f}")
print("-------------------")
print(f"PREÇO FINAL: R$ {custo_total:.2f}")
print("-------------------")


if custo_total> 200:
    desconto = custo_total*0.2
    descontado = custo_total-desconto
    print(f"Parabéns! Você ganhou 20% de desconto por compras acima de 200 reais")
    print(f"R$ {custo_total} - R$ {desconto:.2f}")
    print(f"Valor final: R$ {descontado:.2f}")

elif custo_total> 50:
    desconto = custo_total*0.1
    descontado = custo_total-desconto
    print(f"Parabéns! Você ganhou 10% de desconto por compras acima de 50 reais")
    print(f"R$ {custo_total} - R$ {desconto:.2f}")
    print(f"Valor final: R$ {descontado:.2f}")

else:
    print("Pobre filha duma puta")