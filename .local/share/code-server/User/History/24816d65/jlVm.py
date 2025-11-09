palavra = "vasco da gama o colossal e gigantesco da colina" # A palavra do 1049
contador_vogais = 0
vogais = "aeiou"

# Use um 'for' para inspecionar cada 'letra' em 'palavra'
for letra in palavra:
    # DENTRO do 'for', use um 'if' para checar
    if letra in vogais:
        contador_vogais += 1

print(f"A palavra '{palavra}' tem {contador_vogais} vogais")