carrinho = []
custo_total= 0

while True:
    nome_produto = input("Produto? ")
    while True:
        quantidadetry = input("Quantidade? ")
        try:
            quantidade_produto = float(quantidadetry)
            break
        except:
            print("Somente números são validos")
    while True:
    precotry = input("Preco? ")
        try:
            preco_quantidade = float(precotry)
            break
        except:
            print("Somente números são aceitos")
    novo_produto = {
        "nome": nome_produto,
        "quantidade": quantidade_produto,
        "preco": preco_produto
    }
    carrinho.append(novo_produto)
    total_do_item = preco_produto * quantidade_produto
    custo_total += total_do_item
    fim = input("Adicionar mais um produto?s ou n ")
    if fim != "s":
        break

for produto in carrinho:
    nome = produto["nome"]
    quantidade = produto["quantidade"]
    preco = produto["preco"]
    total_item = quantidade * preco
    print(f"Nome: {nome}, Qtd: {quantidade}, Preço: R$ {preco}, Total do item: R$ {total_item:.2f}")

print("-------------------")
print(f"PREÇO FINAL: R$ {custo_total:.2f}")
print("-------------------")

if custo_total > 200:
    desconto = custo_total * 0.2
    descontado = custo_total - desconto
    print(f"Parabéns você é rico e ganhou 20% de desconto\nR$ {custo_total} - R$ {desconto}\nPREÇO FINAL: R$ {descontado}")

elif custo_total > 50:
    desconto = custo_total * 0.1
    descontado = custo_total - desconto
    print(f"Parabéns você é pobre premium e ganhou 10% de desconto\nR$ {custo_total} - R$ {desconto}\nPREÇO FINAL: R$ {descontado}")

else:
    print("Pobre maldito")

