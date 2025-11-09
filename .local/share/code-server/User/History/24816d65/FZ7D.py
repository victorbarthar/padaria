ddd_mapa = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    # ... (etc)
}

print("--- Catálogo de DDDs ---")
# Use o 'for' com .items() para pegar a chave e o valor
for ddd, cidade in ddd_mapa.items():
    # Imprima a linha formatada
    print(f"DDD {ddd} é de {cidade}")