carrinho = []
custo_total= 0

while True
    nome_produto = input("Produto?")
    quantidade_produto = float(input("Quantidade?"))
    preco_produto = float(input("Preco?"))
    novo_produto = {
        "nome": nome_produto,
        "quantidade": quantidade_produto,
        "preco": preco_produto
    }
    carrinho.append(novo_produto)
    total_do_item = preco_produto * quantidade_produto
    custo_total += total_do_item
    fim = input("Adicionar mais um produto?s ou n")
    if fim != "s":
        break

for produto in carrinho:
    nome = produto["nome"]
    quantidade = produto["quantidade"]
    preco = produto["preco"]
    total_item = quantidade * preco
    print(f"Nome: {nome}, Qtd: {quantidade}, Preço: R$ {preco:.2f}, Total: R$ {total_item}
