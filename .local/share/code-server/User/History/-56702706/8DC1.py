#Lista de Compras
nomes_dos_produtos = ["Pão","Queijo","Café","Brownie"]
quantidades= [50, 1, 5, 10]
precos= [0.75, 45, 6.5, 8]
custo_total = 0


#Caixa
print("CAIXA PADARIA PEGA NO MEU CASSETINHO:")
for i in range(len(nomes_dos_produtos)):
    nome = nomes_dos_produtos[i]
        quantidade = quantidades[i]
            preco = precos[i]
                total_do_item = quantidade * preco
                    print(f" \nNome: {nome}, Quantidade : {quantidade}, Preço: R$ {preco}, Total: R$ {total_do_item:.2f}")


                    #Recibo
                      print("\n PADARIA PEGA NO MEU CASSETINHO")
                    for i in range(len(nomes_dos_produtos)):
                        nome = nomes_dos_produtos[i]
                            quantidade = quantidades[i]
                                preco = precos[i]
                                    total_do_item = quantidade * preco
                                        #calc change
                                            custo_total += total_do_item
                                                print(f" \nNome: {nome}, Qtd : {quantidade}, Preço: R$ {preco}, Total: R$ {total_do_item:.2f}")

                                                print("---------------------")
                                                print(f"PREÇO TOTAL: {custo_total:.2f}")
                                                print("---------------------")

                                                #descontos
                                                if custo_total > 500:
                                                    desconto = custo_total*0.2
                                                        total_final= custo_total-desconto
                                                            print("Parabéns, você é um cliente Vip e ganhou 20% de desconto")
                                                                print(f"R$ {custo_total} - R$ {desconto:.2f}")
                                                                    print(f"R$ {total_final}")

                                                                    elif custo_total > 200:
                                                                        desconto = custo_total*0.1
                                                                            total_final= custo_total-desconto
                                                                                print("Parabéns, você é um cliente Plus e ganhou 10% de desconto")
                                                                                    print(f"R$ {custo_total} - R$ {desconto:.2f}")
                                                                                        print(f"R$ {total_final}")

                                                                                        else:
                                                                                            print("Pobre filha da puta")