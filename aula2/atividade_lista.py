#Passo 1: Crie uma tupla com 5 dados
listacompra = ("Cerveja", "Vinho", "Pinga", "Conhaque", "Tequila")

#Passo 2: Altere a tupla para uma lista
lista_mod = list(listacompra)

#Passo 3: Insira 2 dados extras a essa lista
lista_mod.append("Saque")
lista_mod.append("Gin")

#Passo 4: Remova o primeiro dado da lista
lista_mod.pop(0)

#Passo 5: Remova o último dado da lista
lista_mod.pop()

#Passo 6: Faça um print com o primeiro dado da lista
print("Primeiro dado da lista: ", lista_mod[0])

#Passo 7: Faça um print com a quantidade de dados da lista
print("Quanidade de dados da lista: ", len(lista_mod))

#Passo 8: Crie um dicionário com os seguintes dados: Nome, Idade, Profissão

bdpessoas = {

    "Nome": "André",
    "Idade": 39,
    "Profissão": "Mestre Cervejeiro"
}

#Passo 9: Imprima somente o valor contido na chave Nome do dicionário

print("Nome no dicionário: ", bdpessoas["Nome"])