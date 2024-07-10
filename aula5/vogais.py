palavra = input("Por favor, insira uma palavra: ")

contagem_vogais = 0
vogais = "aeiouAEIOU"

for i in palavra:
    if i in vogais:
        contagem_vogais += 1

print(f"O número total de vogais na palavra '{palavra}' é: {contagem_vogais}")