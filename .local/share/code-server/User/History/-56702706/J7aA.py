#Conceitos Iniciais
nome_produto = input("Produto?")
quantidade_texto = input("Quantidade?")
quantidade_produto= float("Quantidade?")
preço_produto= float("Preço?")
custo_total= quantidade_produto*preço_produto

print("------------------------------")
print("PADARIA PEGA NO MEU CASSETINHO")
print("------------------------------")
print(f"Produto: {nome_produto}, Qtd: {quantidade_produto}, Preço: R$ {preço_produto}")
print(f"\nPREÇO FINAL: {custo_total}")

#descontos
if custo_total > 50:
    desconto = custo_total*0.2
    total_final= custo_total-desconto
    print("Parabéns, você é um cliente Vip e ganhou 20% de desconto")
    print(f"R$ {custo_total} - R$ {desconto:.2f}")
    print(f"R$ {total_final}")

elif custo_total > 20:
    desconto = custo_total*0.1
    total_final= custo_total-desconto
    print("Parabéns, você é um cliente Plus e ganhou 10% de desconto")
    print(f"R$ {custo_total} - R$ {desconto:.2f}")
    print(f"R$ {total_final}")

else:
    print("Pobre filha da puta")