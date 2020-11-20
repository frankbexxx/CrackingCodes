import math

mensagem = 'abcdefghijklmnopqrstuvwxyzabcd'
mensagem2 = 'common sense is not so common.'

men = len(mensagem2)

print("comp mensagem: ", men)

k = 8

lista = []

col = math.ceil(men / k)

print("num colunas: ", col)

for l in range(k):
    for c in range(col):
        if c * k + l < men:
            lista.append(c * k + l)

cripto = ''

for r in range(men):
    a = int(lista[r])
    cripto += mensagem2[a]

print(lista)

print(cripto)