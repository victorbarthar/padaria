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
        precotry = input("Preço? ")
        try:
            preco_produto = float(precotry)
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

with open("recibo.txt", "a") as r:


    for produto in carrinho:
        nome = produto["nome"]
        quantidade = produto["quantidade"]
        preco = produto["preco"]
        total_item = quantidade * preco
        r.write(f"Nome: {nome}, Qtd: {quantidade}, Preço: R$ {preco}, Total do item: R$ {total_item:.2f}\n")
        print(f"Nome: {nome}, Qtd: {quantidade}, Preço: R$ {preco}, Total do item: R$ {total_item:.2f}\n")

    r.write("-------------------\n")
    r.write(f"PREÇO FINAL: R$ {custo_total:.2f}\n")
    r.write("-------------------\n")
    print("-------------------\n")
    print(f"PREÇO FINAL: R$ {custo_total:.2f}\n")
    print("-------------------\n")

    if custo_total > 200:
        desconto = custo_total * 0.2
        descontado = custo_total - desconto
        r.write(f"Parabéns você é rico e ganhou 20% de desconto\nR$ {custo_total:.2f} - R$ {desconto:.2f}\nPREÇO FINAL: R$ {descontado:.2f}\n")
        print(f"Parabéns você é rico e ganhou 20% de desconto\nR$ {custo_total:.2f} - R$ {desconto:.2f}\nPREÇO FINAL: R$ {descontado:.2f}\n")

    elif custo_total > 50:
        desconto = custo_total * 0.1
        descontado = custo_total - desconto
        r.write(f"Parabéns você é pobre premium e ganhou 10% de desconto\nR$ {custo_total:.2f} - R$ {desconto:.2f}\nPREÇO FINAL: R$ {descontado:.2f}\n")
        print(f"Parabéns você é pobre premium e ganhou 10% de desconto\nR$ {custo_total:.2f} - R$ {desconto:.2f}\nPREÇO FINAL: R$ {descontado:.2f}\n")

    else:
        r.write("Pobre maldito")

