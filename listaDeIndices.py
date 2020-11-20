import math

colunas = 4 # int(input("colunas: "))

linhas = 8 # int(input("linhas: "))

comprimento = 30 # int(input("comprimento: "))

lista = list()

area = colunas * linhas

areaInutil = area - comprimento

print("area = ", area)
print("area inutil = ", areaInutil)

for i in range(colunas):
    conta = 1
    for e in range(linhas):
        a = i + e * colunas
        if e * colunas  > area - colunas * areaInutil:
            a -= conta
            conta += 1
        lista.append(a)
        if i == (colunas - 1) and e >= (linhas - areaInutil - 1):
            break

    print(lista)

print(lista)